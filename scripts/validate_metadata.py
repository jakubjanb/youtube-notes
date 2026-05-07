#!/usr/bin/env python3
"""Validate required metadata fields for sources and generated notes."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


NOTE_REQUIRED = [
    "title",
    "slug",
    "domain",
    "subdomain",
    "topics",
    "tags",
    "difficulty",
    "prerequisites",
    "source_type",
    "source_url",
    "source_title",
    "source_channel",
    "created_at",
    "updated_at",
    "status",
    "latex_file",
    "pdf_file",
    "blueprint_file",
    "transcript_file",
    "related_notes",
    "concepts",
    "summary",
]

SOURCE_REQUIRED = [
    "title",
    "youtube_url",
    "canonical_youtube_url",
    "channel",
    "video_id",
    "published_at",
    "duration",
    "description",
    "thumbnail_url",
    "date_watched",
    "date_processed",
    "domain",
    "subdomain",
    "topics",
    "tags",
    "difficulty",
    "prerequisites",
    "source_language",
    "target_note_language",
    "status",
    "related_notes",
]

NOTE_NONEMPTY = ["title", "slug", "domain", "source_type", "created_at", "updated_at", "status"]
SOURCE_NONEMPTY = ["youtube_url", "canonical_youtube_url", "video_id", "date_processed", "status"]


def parse_scalar(value: str) -> object:
    value = value.strip()
    if value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [part.strip().strip("'\"") for part in inner.split(",")]
    return value.strip("'\"")


def parse_simple_yaml(path: Path) -> dict[str, object]:
    data: dict[str, object] = {}
    current_key: str | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if raw_line.startswith((" ", "\t")):
            item = raw_line.strip()
            if current_key and item.startswith("- "):
                value = item[2:].strip().strip("'\"")
                data.setdefault(current_key, [])
                if isinstance(data[current_key], list):
                    data[current_key].append(value)
            continue

        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", raw_line)
        if not match:
            continue
        key, value = match.groups()
        if value == "":
            data[key] = []
            current_key = key
        else:
            data[key] = parse_scalar(value)
            current_key = key if data[key] == [] else None

    return data


def metadata_kind(data: dict[str, object]) -> str:
    if "source_type" in data or "slug" in data:
        return "note"
    if "youtube_url" in data or "video_id" in data:
        return "source"
    return "unknown"


def validate_file(path: Path) -> list[str]:
    data = parse_simple_yaml(path)
    kind = metadata_kind(data)
    if kind == "note":
        required = NOTE_REQUIRED
        nonempty = NOTE_NONEMPTY
    elif kind == "source":
        required = SOURCE_REQUIRED
        nonempty = SOURCE_NONEMPTY
    else:
        return [f"{path}: could not infer metadata type"]

    errors: list[str] = []
    missing = [field for field in required if field not in data]
    empty = [field for field in nonempty if data.get(field) in ("", [], None)]
    if missing:
        errors.append(f"{path}: missing required fields: {', '.join(missing)}")
    if empty:
        errors.append(f"{path}: required fields are empty: {', '.join(empty)}")
    return errors


def collect_metadata(paths: list[str], notes: str | None, sources: str | None) -> list[Path]:
    files: list[Path] = []
    for path_text in paths:
        path = Path(path_text)
        if path.is_dir():
            files.extend(sorted(path.rglob("metadata.yaml")))
            files.extend(sorted(path.rglob("*.yaml")))
        elif path.exists():
            files.append(path)

    if notes:
        files.extend(sorted(Path(notes).glob("*/*/metadata.yaml")))
    if sources:
        files.extend(sorted(Path(sources).rglob("*.yaml")))

    seen: set[Path] = set()
    unique: list[Path] = []
    for path in files:
        resolved = path.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique.append(path)
    return unique


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="Metadata files or directories to validate.")
    parser.add_argument("--notes", help="Notes root to scan for notes/*/*/metadata.yaml.")
    parser.add_argument("--sources", help="Source metadata directory to scan recursively.")
    args = parser.parse_args()

    files = collect_metadata(args.paths, args.notes, args.sources)
    if not files:
        print("No metadata files found.")
        return 0

    errors: list[str] = []
    for path in files:
        errors.extend(validate_file(path))

    if errors:
        print("\n".join(errors))
        return 1

    print(f"OK: validated {len(files)} metadata file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
