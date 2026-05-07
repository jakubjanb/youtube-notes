# Related Skills

This repository is designed to work with three main ChatGPT Skills:

- `youtube_metadata_collector`
- `youtube_note_architect`
- `youtube_note_generator`

## `youtube_metadata_collector`

Role: take a YouTube URL and create a source metadata YAML file.

Expected output location:

```text
sources/youtube/metadata/<note-slug>.yaml
```

This is the first source-intake step. It extracts the video ID, normalizes the canonical YouTube URL, fetches public metadata when possible, infers educational fields, and avoids silently overwriting existing metadata.

## `youtube_note_architect`

Role: turn a YouTube topic, title, metadata, and transcript into a structured educational blueprint.

Expected output location:

```text
blueprints/<domain>/<note-slug>.md
```

The blueprint should plan objectives, prerequisites, sections, derivations, examples, figures, notation, and quality checks.

## `youtube_note_generator`

Role: turn the architect blueprint into a polished LaTeX note.

Expected output location:

```text
notes/<domain>/<note-slug>/note.tex
```

The generated note should follow the LaTeX conventions in `docs/latex-style-guide.md` and preserve source provenance through `metadata.yaml`, `blueprint.md`, and `transcript.md`.

## Existing Skill Implementations

This workspace already contains top-level folders named:

- `youtube-note-architect/`
- `youtube-note-generator/`
- `youtube-metadata-collector/`
- `youtube-notes-planner/`

Those are preserved as existing skill implementations or references. The `skills/` folder documents how this repository uses the skills; it does not reimplement them.
