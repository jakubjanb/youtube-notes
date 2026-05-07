#!/usr/bin/env python3
"""Create a new self-contained note folder from project templates."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from string import Template

from slugify import slugify


DOMAINS = {
    "mathematics",
    "physics",
    "statistics",
    "probability",
    "data-science",
    "machine-learning",
    "artificial-intelligence",
    "computer-science",
    "quantitative-finance",
    "other",
}


def render_curly_template(text: str, values: dict[str, str]) -> str:
    rendered = text
    for key, value in values.items():
        rendered = rendered.replace("{{" + key + "}}", value)
    return rendered


def write_file(path: Path, content: str, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"{path} already exists; use --force to overwrite it")
    path.write_text(content, encoding="utf-8")


def note_metadata(values: dict[str, str]) -> str:
    return Template(
        """title: "$title"
slug: "$slug"
domain: "$domain"
subdomain: "$subdomain"
topics: []
tags: []
difficulty: "$difficulty"
prerequisites: []
source_type: youtube
source_url: "$source_url"
source_title: "$source_title"
source_channel: "$source_channel"
created_at: "$created_at"
updated_at: "$created_at"
status: "$status"
latex_file: note.tex
pdf_file: note.pdf
blueprint_file: blueprint.md
transcript_file: transcript.md
related_notes: []
concepts: []
summary: "$summary"
"""
    ).substitute(values)


def note_markdown(values: dict[str, str]) -> str:
    return Template(
        """# $title

## Summary

$summary

## Key Ideas

- TODO

## Important Equations

```tex
% Add key equations here.
```

## Related Notes

- TODO
"""
    ).substitute(values)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title", help="Human-readable note title.")
    parser.add_argument("--domain", default="other", choices=sorted(DOMAINS))
    parser.add_argument("--subdomain", default="")
    parser.add_argument("--slug", default="", help="Override the generated slug.")
    parser.add_argument("--source-url", default="")
    parser.add_argument("--source-title", default="")
    parser.add_argument("--source-channel", default="")
    parser.add_argument("--difficulty", default="")
    parser.add_argument("--status", default="note-drafted")
    parser.add_argument("--force", action="store_true", help="Overwrite existing template files.")
    args = parser.parse_args()

    title = args.title.strip()
    if not title:
        parser.error("title is required")

    root = Path(__file__).resolve().parents[1]
    slug = args.slug.strip() or slugify(title)
    if not slug:
        parser.error("could not create a valid slug from title")

    note_dir = root / "notes" / args.domain / slug
    if note_dir.exists() and any(note_dir.iterdir()) and not args.force:
        raise SystemExit(f"{note_dir} already exists and is not empty; use --force to overwrite template files")

    (note_dir / "figures" / "source").mkdir(parents=True, exist_ok=True)
    (note_dir / "figures" / "exported").mkdir(parents=True, exist_ok=True)
    (note_dir / "attachments").mkdir(parents=True, exist_ok=True)

    today = date.today().isoformat()
    values = {
        "title": title,
        "slug": slug,
        "domain": args.domain,
        "subdomain": args.subdomain,
        "status": args.status,
        "source_title": args.source_title or title,
        "source_url": args.source_url,
        "source_channel": args.source_channel,
        "difficulty": args.difficulty,
        "created_at": today,
        "summary": "TODO: Write a concise summary of the note.",
    }

    templates = root / "templates"
    latex_template = root / "latex" / "templates" / "note-template.tex"

    readme = render_curly_template((templates / "final-note-readme.md").read_text(encoding="utf-8"), values)
    transcript = render_curly_template((templates / "transcript-template.md").read_text(encoding="utf-8"), values)
    blueprint = render_curly_template((templates / "blueprint-template.md").read_text(encoding="utf-8"), values)
    tex = render_curly_template(latex_template.read_text(encoding="utf-8"), values)

    write_file(note_dir / "README.md", readme, args.force)
    write_file(note_dir / "metadata.yaml", note_metadata(values), args.force)
    write_file(note_dir / "transcript.md", transcript, args.force)
    write_file(note_dir / "blueprint.md", blueprint, args.force)
    write_file(note_dir / "note.md", note_markdown(values), args.force)
    write_file(note_dir / "note.tex", tex, args.force)
    write_file(note_dir / "figures" / "source" / ".gitkeep", "# Keep note-local figure sources in version control.\n", args.force)
    write_file(note_dir / "figures" / "exported" / ".gitkeep", "# Keep note-local figure exports in version control.\n", args.force)
    write_file(note_dir / "attachments" / ".gitkeep", "# Keep note-local attachments in version control.\n", args.force)

    print(note_dir.relative_to(root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
