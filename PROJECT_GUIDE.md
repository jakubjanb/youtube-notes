# Project Guide

This repository is organized around one principle: preserve the full learning chain from source video to polished knowledge artifact.

## Architecture

The project has four layers.

**Source Layer**

`inbox/` is for unprocessed captures. `sources/` is the durable archive for transcripts, video metadata, raw downloads, and non-YouTube references.

**Generation Layer**

`blueprints/` stores structured plans created by `youtube_note_architect`. `latex/` stores the shared LaTeX system used by generated notes.

**Knowledge Artifact Layer**

`notes/` stores final note folders. Each note folder is self-contained: metadata, transcript copy, blueprint copy, Markdown rendering, LaTeX source, PDF, figures, and attachments.

**Second-Brain Layer**

`knowledge-base/` stores indexes, concept cards, prerequisite maps, curated maps of content, and learning paths.

## Note Folder Contract

Every final note should use this structure:

```text
notes/<domain>/<note-slug>/
├── README.md
├── note.md
├── note.tex
├── note.pdf
├── metadata.yaml
├── blueprint.md
├── transcript.md
├── figures/
│   ├── source/
│   └── exported/
└── attachments/
```

`note.pdf` is intentionally not ignored by Git because finished PDFs are learning artifacts. LaTeX auxiliary files are ignored.

## Domain Organization

Use the configured domains in `config/domains.yaml` unless a topic clearly needs `notes/other/` temporarily. Prefer stable broad domains over overly narrow top-level folders. Use `subdomain`, `topics`, `tags`, and maps of content for finer structure.

## Metadata First

Metadata is the routing system of the second brain. Every source and final note should record:

- source identity,
- title,
- domain,
- subdomain,
- topics,
- tags,
- prerequisites,
- difficulty,
- related notes,
- status,
- important file paths.

The required fields are documented in [docs/metadata-schema.md](docs/metadata-schema.md).

## AI-Agent Operating Rules

Future AI agents should:

- inspect existing files before editing,
- create new note folders with `scripts/new_note.py` or `make new-note`,
- avoid overwriting existing note artifacts unless explicitly requested,
- preserve source references and transcript provenance,
- keep generated blueprints and final notes linked through metadata,
- update indexes after adding or renaming notes,
- store figures in the note-local `figures/` folder when they belong to one note,
- store reusable or cross-note figures in top-level `figures/`.

## Status Vocabulary

Recommended source and note statuses:

- `captured`
- `transcribed`
- `blueprint-drafted`
- `note-drafted`
- `needs-review`
- `reviewed`
- `published`
- `archived`

## Long-Term Maintenance

As the repository grows, periodically:

- merge duplicate tags,
- normalize concept names,
- convert repeated ideas into concept cards,
- update maps of content,
- repair stale links,
- revisit old notes when better explanations or sources appear.

