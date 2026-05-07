#!/usr/bin/env python3
"""Create youtube_notes source metadata YAML from a YouTube URL."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import OrderedDict
from datetime import date
from pathlib import Path
from typing import Any

from slugify import choose_slug_base, slugify


VALID_STATUSES = {
    "metadata_created",
    "transcript_needed",
    "transcribed",
    "blueprint_created",
    "note_generated",
    "published",
}

LIST_FIELDS = {"topics", "tags", "prerequisites", "related_notes"}


def split_csv(values: list[str] | None) -> list[str]:
    if not values:
        return []
    result: list[str] = []
    for raw in values:
        for item in raw.split(","):
            clean = item.strip()
            if clean:
                result.append(clean)
    return result


def extract_video_id(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    host = parsed.netloc.lower()
    path = parsed.path.strip("/")

    if host.endswith("youtu.be"):
        return path.split("/")[0]

    if "youtube.com" in host:
        query = urllib.parse.parse_qs(parsed.query)
        if query.get("v"):
            return query["v"][0]
        parts = path.split("/")
        for marker in ("shorts", "embed", "live", "v"):
            if marker in parts:
                index = parts.index(marker)
                if index + 1 < len(parts):
                    return parts[index + 1]

    match = re.search(r"(?:v=|youtu\.be/|shorts/|embed/|live/)([A-Za-z0-9_-]{6,})", url)
    return match.group(1) if match else ""


def canonical_url(video_id: str) -> str:
    return f"https://www.youtube.com/watch?v={video_id}"


def request_json(url: str, timeout: int = 15) -> dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": "youtube_metadata_collector/1.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_with_api(video_id: str, api_key: str) -> tuple[dict[str, Any], set[str]]:
    query = urllib.parse.urlencode(
        {
            "part": "snippet,contentDetails",
            "id": video_id,
            "key": api_key,
        }
    )
    url = f"https://www.googleapis.com/youtube/v3/videos?{query}"
    data = request_json(url)
    items = data.get("items", [])
    if not items:
        return {}, set()

    item = items[0]
    snippet = item.get("snippet", {})
    content = item.get("contentDetails", {})
    thumbnails = snippet.get("thumbnails", {})
    thumbnail_url = ""
    for key in ("maxres", "standard", "high", "medium", "default"):
        if key in thumbnails and thumbnails[key].get("url"):
            thumbnail_url = thumbnails[key]["url"]
            break

    metadata = {
        "title": snippet.get("title", ""),
        "channel": snippet.get("channelTitle", ""),
        "published_at": snippet.get("publishedAt", ""),
        "duration": content.get("duration", ""),
        "description": snippet.get("description", ""),
        "thumbnail_url": thumbnail_url,
        "source_language": snippet.get("defaultAudioLanguage") or snippet.get("defaultLanguage") or "",
        "_fetched_tags": snippet.get("tags", []),
    }
    return metadata, {key for key, value in metadata.items() if value and key != "_fetched_tags"}


def seconds_to_iso8601(seconds: int | float | str | None) -> str:
    if seconds in (None, ""):
        return ""
    try:
        total = int(float(seconds))
    except (TypeError, ValueError):
        return str(seconds)
    hours, remainder = divmod(total, 3600)
    minutes, secs = divmod(remainder, 60)
    result = "PT"
    if hours:
        result += f"{hours}H"
    if minutes:
        result += f"{minutes}M"
    if secs or result == "PT":
        result += f"{secs}S"
    return result


def upload_date_to_iso(upload_date: str) -> str:
    if re.fullmatch(r"\d{8}", upload_date):
        return f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}"
    return upload_date


def fetch_with_ytdlp(url: str) -> tuple[dict[str, Any], set[str]]:
    if not shutil.which("yt-dlp"):
        return {}, set()
    command = ["yt-dlp", "--dump-single-json", "--skip-download", "--no-warnings", url]
    try:
        completed = subprocess.run(command, capture_output=True, text=True, timeout=30, check=False)
    except (OSError, subprocess.TimeoutExpired):
        return {}, set()
    if completed.returncode != 0 or not completed.stdout.strip():
        return {}, set()
    try:
        data = json.loads(completed.stdout)
    except json.JSONDecodeError:
        return {}, set()

    metadata = {
        "title": data.get("title", ""),
        "channel": data.get("channel") or data.get("uploader", ""),
        "published_at": upload_date_to_iso(str(data.get("upload_date", "") or "")),
        "duration": seconds_to_iso8601(data.get("duration")),
        "description": data.get("description", ""),
        "thumbnail_url": data.get("thumbnail", ""),
        "source_language": data.get("language", ""),
        "_fetched_tags": data.get("tags", []) or [],
    }
    return metadata, {key for key, value in metadata.items() if value and key != "_fetched_tags"}


def fetch_with_oembed(url: str) -> tuple[dict[str, Any], set[str]]:
    query = urllib.parse.urlencode({"url": url, "format": "json"})
    endpoint = f"https://www.youtube.com/oembed?{query}"
    try:
        data = request_json(endpoint)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return {}, set()
    metadata = {
        "title": data.get("title", ""),
        "channel": data.get("author_name", ""),
        "thumbnail_url": data.get("thumbnail_url", ""),
    }
    return metadata, {key for key, value in metadata.items() if value}


def first_nonempty(*values: Any) -> Any:
    for value in values:
        if value not in ("", None, []):
            return value
    return ""


def infer_domain(text: str, user_value: str) -> str:
    if user_value:
        return user_value
    lower = text.lower()
    rules = [
        ("machine-learning", ["gradient", "neural", "loss", "backprop", "classification", "regression model"]),
        ("statistics", ["p-value", "confidence interval", "estimator", "hypothesis", "statistical"]),
        ("probability", ["probability", "random variable", "bayes", "distribution", "markov"]),
        ("physics", ["mechanics", "quantum", "lagrangian", "hamiltonian", "electric", "magnetic"]),
        ("computer-science", ["algorithm", "data structure", "complexity", "compiler", "database"]),
        ("mathematics", ["theorem", "proof", "geometry", "polynomial", "complex", "matrix", "calculus"]),
    ]
    for domain, keywords in rules:
        if any(keyword in lower for keyword in keywords):
            return domain
    return ""


def infer_subdomain(text: str, domain: str, user_value: str) -> str:
    if user_value:
        return user_value
    lower = text.lower()
    if "marden" in lower or "complex" in lower:
        return "complex-analysis"
    if "gradient" in lower or "optimization" in lower:
        return "optimization"
    if "bayes" in lower:
        return "bayesian-inference"
    if "linear algebra" in lower or "eigen" in lower or "matrix" in lower:
        return "linear-algebra"
    if domain == "mathematics" and "geometry" in lower:
        return "geometry"
    return ""


def title_topics(title: str) -> list[str]:
    topics: list[str] = []
    theorem_match = re.search(r"([A-Z][A-Za-z'’-]+(?:\s+[A-Z][A-Za-z'’-]+)*\s+Theorem)\b", title)
    if theorem_match:
        topics.append(theorem_match.group(1).replace("’", "'"))
    elif title:
        base = choose_slug_base(title)
        if base:
            topics.append(base)
    return topics


def infer_topics(title: str, description: str, subdomain: str, user_topics: list[str]) -> list[str]:
    if user_topics:
        return user_topics
    text = f"{title} {description} {subdomain}".lower()
    topics = title_topics(title)
    keyword_topics = [
        ("complex", "complex numbers"),
        ("polynomial", "polynomials"),
        ("ellipse", "ellipses"),
        ("geometry", "geometry"),
        ("gradient descent", "gradient descent"),
        ("loss", "loss functions"),
    ]
    for keyword, topic in keyword_topics:
        if keyword in text and topic not in topics:
            topics.append(topic)
    if "marden" in text or "complex-analysis" in text:
        for topic in ("complex numbers", "geometry", "polynomials"):
            if topic not in topics:
                topics.append(topic)
    return topics[:8]


def infer_tags(topics: list[str], fetched_tags: list[str], title: str, domain: str, subdomain: str, user_tags: list[str]) -> list[str]:
    if user_tags:
        return [slugify(tag, max_words=6) for tag in user_tags if slugify(tag, max_words=6)]
    candidates = [subdomain, domain, *topics]
    for tag in fetched_tags[:8]:
        if isinstance(tag, str) and len(tag) <= 40:
            candidates.append(tag)
    if title:
        candidates.extend(title_topics(title))
    tags: list[str] = []
    for candidate in candidates:
        slug = slugify(str(candidate), max_words=6)
        if slug and slug not in tags:
            tags.append(slug)
    return tags[:10]


def infer_difficulty(text: str, user_value: str) -> str:
    if user_value:
        return user_value
    lower = text.lower()
    if any(word in lower for word in ("theorem", "proof", "complex-analysis", "lagrangian", "bayesian")):
        return "intermediate"
    if any(word in lower for word in ("introduction", "beginner", "intuition", "explained")):
        return "beginner"
    return ""


def infer_prerequisites(text: str, subdomain: str, user_values: list[str]) -> list[str]:
    if user_values:
        return user_values
    lower = f"{text} {subdomain}".lower()
    prereqs: list[str] = []
    if "marden" in lower or "complex-analysis" in lower:
        prereqs.extend(["complex numbers", "polynomials", "ellipses"])
    elif "gradient" in lower:
        prereqs.extend(["functions", "derivatives", "vectors"])
    elif "bayes" in lower:
        prereqs.extend(["conditional probability", "basic probability"])
    return prereqs


def yaml_quote(value: Any) -> str:
    if value is None:
        value = ""
    text = str(value)
    text = text.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
    return f'"{text}"'


def render_yaml(metadata: OrderedDict[str, Any]) -> str:
    lines: list[str] = []
    for key, value in metadata.items():
        if key in LIST_FIELDS:
            items = value if isinstance(value, list) else []
            if not items:
                lines.append(f"{key}: []")
            else:
                lines.append(f"{key}:")
                for item in items:
                    lines.append(f"  - {yaml_quote(item)}")
        else:
            lines.append(f"{key}: {yaml_quote(value)}")
    return "\n".join(lines) + "\n"


def parse_existing_yaml(path: Path) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current_key: str | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and current_key:
            data.setdefault(current_key, [])
            if isinstance(data[current_key], list):
                data[current_key].append(line[4:].strip().strip('"'))
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            continue
        key, raw = match.groups()
        if raw == "[]":
            data[key] = []
            current_key = None
        elif raw == "":
            data[key] = []
            current_key = key
        else:
            data[key] = raw.strip().strip('"').replace("\\n", "\n")
            current_key = None
    return data


def find_repo_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "sources" / "youtube" / "metadata").exists():
            return candidate
    return start


def ensure_output_dir(output_dir: Path, repo_root: Path) -> Path:
    resolved = output_dir.resolve()
    expected = (repo_root / "sources" / "youtube" / "metadata").resolve()
    try:
        resolved.relative_to(expected)
    except ValueError as exc:
        raise ValueError(f"output directory must be inside {expected}") from exc
    resolved.mkdir(parents=True, exist_ok=True)
    return resolved


def versioned_path(path: Path) -> Path:
    if not path.exists():
        return path
    index = 2
    while True:
        candidate = path.with_name(f"{path.stem}-{index}{path.suffix}")
        if not candidate.exists():
            return candidate
        index += 1


def validate_metadata(metadata: OrderedDict[str, Any], output_path: Path, metadata_root: Path) -> list[str]:
    errors: list[str] = []
    for field in ("video_id", "youtube_url", "canonical_youtube_url", "date_processed"):
        if not metadata.get(field):
            errors.append(f"missing required field: {field}")
    if metadata.get("status") not in VALID_STATUSES:
        errors.append(f"invalid status: {metadata.get('status')}")
    for field in LIST_FIELDS:
        if not isinstance(metadata.get(field), list):
            errors.append(f"{field} must be a list")
    try:
        output_path.resolve().relative_to(metadata_root.resolve())
    except ValueError:
        errors.append(f"output path must be inside {metadata_root}")
    return errors


def build_metadata(args: argparse.Namespace) -> tuple[OrderedDict[str, Any], dict[str, set[str]]]:
    today = date.today().isoformat()
    video_id = extract_video_id(args.youtube_url)
    if not video_id:
        raise ValueError("could not extract a YouTube video ID from the URL")

    fetched: dict[str, Any] = {}
    fetched_fields: set[str] = set()
    api_key = os.environ.get("YOUTUBE_API_KEY", "")
    if api_key:
        try:
            fetched, fetched_fields = fetch_with_api(video_id, api_key)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            fetched, fetched_fields = {}, set()

    if not fetched:
        fetched, fetched_fields = fetch_with_ytdlp(args.youtube_url)
    if not fetched:
        fetched, fetched_fields = fetch_with_oembed(args.youtube_url)

    user_topics = split_csv(args.topics)
    user_tags = split_csv(args.tags)
    user_prerequisites = split_csv(args.prerequisites)

    title = first_nonempty(args.title, fetched.get("title", ""))
    channel = first_nonempty(args.channel, fetched.get("channel", ""))
    description = first_nonempty(args.description, fetched.get("description", ""))
    educational_text = " ".join(
        str(value)
        for value in [
            title,
            description[:1000],
            args.domain,
            args.subdomain,
            " ".join(user_topics),
            " ".join(user_tags),
            " ".join(user_prerequisites),
        ]
        if value
    )

    domain = infer_domain(educational_text, args.domain)
    subdomain = infer_subdomain(educational_text, domain, args.subdomain)
    topics = infer_topics(title, description, subdomain, user_topics)
    tags = infer_tags(topics, fetched.get("_fetched_tags", []), title, domain, subdomain, user_tags)
    difficulty = infer_difficulty(f"{educational_text} {subdomain}", args.difficulty)
    prerequisites = infer_prerequisites(f"{educational_text} {' '.join(topics)}", subdomain, user_prerequisites)
    source_language = first_nonempty(args.source_language, fetched.get("source_language", ""), "en")
    status = args.status
    if args.transcript_available and args.status == "metadata_created":
        status = "transcribed"

    metadata: OrderedDict[str, Any] = OrderedDict(
        [
            ("title", title),
            ("youtube_url", args.youtube_url),
            ("canonical_youtube_url", canonical_url(video_id)),
            ("channel", channel),
            ("video_id", video_id),
            ("published_at", fetched.get("published_at", "")),
            ("duration", fetched.get("duration", "")),
            ("description", description),
            ("thumbnail_url", fetched.get("thumbnail_url", "")),
            ("date_watched", args.date_watched or today),
            ("date_processed", args.date_processed or today),
            ("domain", domain),
            ("subdomain", subdomain),
            ("topics", topics),
            ("tags", tags),
            ("difficulty", difficulty),
            ("prerequisites", prerequisites),
            ("source_language", source_language),
            ("target_note_language", args.target_note_language),
            ("status", status),
            ("related_notes", split_csv(args.related_notes)),
        ]
    )
    if args.user_notes:
        metadata["user_notes"] = args.user_notes

    user_fields = {
        key
        for key, value in {
            "title": args.title,
            "channel": args.channel,
            "description": args.description,
            "domain": args.domain,
            "subdomain": args.subdomain,
            "topics": user_topics,
            "tags": user_tags,
            "difficulty": args.difficulty,
            "prerequisites": user_prerequisites,
            "source_language": args.source_language,
            "target_note_language": args.target_note_language,
        }.items()
        if value
    }
    inferred_fields = {
        key
        for key in ("domain", "subdomain", "topics", "tags", "difficulty", "prerequisites", "source_language")
        if metadata.get(key) not in ("", [], None) and key not in user_fields and key not in fetched_fields
    }
    sources = {
        "user": user_fields,
        "fetched": fetched_fields,
        "inferred": inferred_fields,
    }
    return metadata, sources


def output_summary(path: Path, metadata: OrderedDict[str, Any], sources: dict[str, set[str]], conflict_note: str) -> str:
    empty = [key for key, value in metadata.items() if value in ("", [], None)]
    lines = [
        f"metadata_file: {path}",
        f"video_id: {metadata['video_id']}",
        f"status: {metadata['status']}",
        f"user_fields: {', '.join(sorted(sources['user'])) or '(none)'}",
        f"fetched_fields: {', '.join(sorted(sources['fetched'])) or '(none)'}",
        f"inferred_fields: {', '.join(sorted(sources['inferred'])) or '(none)'}",
        f"empty_fields: {', '.join(empty) or '(none)'}",
    ]
    if conflict_note:
        lines.append(f"conflict_handling: {conflict_note}")
    lines.append("next_step: save the transcript, then run youtube_note_architect.")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("youtube_url")
    parser.add_argument("--output-dir", default="sources/youtube/metadata")
    parser.add_argument("--title", default="")
    parser.add_argument("--channel", default="")
    parser.add_argument("--description", default="")
    parser.add_argument("--date-watched", default="")
    parser.add_argument("--date-processed", default="")
    parser.add_argument("--domain", default="")
    parser.add_argument("--subdomain", default="")
    parser.add_argument("--topics", action="append")
    parser.add_argument("--tags", action="append")
    parser.add_argument("--difficulty", default="")
    parser.add_argument("--prerequisites", action="append")
    parser.add_argument("--source-language", default="")
    parser.add_argument("--target-note-language", default="en")
    parser.add_argument("--status", default="metadata_created", choices=sorted(VALID_STATUSES))
    parser.add_argument("--related-notes", action="append")
    parser.add_argument("--user-notes", default="")
    parser.add_argument("--slug", default="")
    parser.add_argument("--transcript-available", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--allow-overwrite", action="store_true")
    parser.add_argument("--update-missing", action="store_true")
    args = parser.parse_args()

    try:
        repo_root = find_repo_root(Path.cwd().resolve())
        output_dir = Path(args.output_dir)
        if not output_dir.is_absolute():
            output_dir = repo_root / output_dir
        metadata_root = ensure_output_dir(output_dir, repo_root)
        metadata, sources = build_metadata(args)

        slug_base = args.slug or choose_slug_base(str(metadata.get("title", "")))
        slug = slugify(slug_base) or slugify(str(metadata["video_id"]), max_words=1)
        output_path = metadata_root / f"{slug}.yaml"

        conflict_note = ""
        if output_path.exists() and not args.allow_overwrite and not args.update_missing:
            original = output_path
            output_path = versioned_path(output_path)
            conflict_note = f"{original.name} exists; created {output_path.name} instead"

        errors = validate_metadata(metadata, output_path, metadata_root)
        if errors:
            print("\n".join(errors), file=sys.stderr)
            return 1

        if args.update_missing and output_path.exists():
            existing = parse_existing_yaml(output_path)
            for key, value in metadata.items():
                if existing.get(key) in ("", [], None) and value not in ("", [], None):
                    existing[key] = value
            metadata = OrderedDict((key, existing.get(key, value)) for key, value in metadata.items())
            conflict_note = "updated missing fields only"

        yaml_text = render_yaml(metadata)
        if args.dry_run:
            print(yaml_text)
            print(output_summary(output_path, metadata, sources, conflict_note), file=sys.stderr)
            return 0

        output_path.write_text(yaml_text, encoding="utf-8")
        print(output_summary(output_path, metadata, sources, conflict_note))
        return 0
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
