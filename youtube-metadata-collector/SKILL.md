---
name: youtube-metadata-collector
description: Create clean YouTube source metadata YAML files for the youtube_notes repository from a YouTube URL. Use when the user wants source intake, video metadata collection, metadata YAML generation, or the first step before youtube_note_architect and youtube_note_generator. Supports YouTube Data API, yt-dlp/oEmbed fallbacks, safe slug generation, educational field inference, and non-overwriting writes to sources/youtube/metadata.
---

# youtube_metadata_collector

Visible skill name: `youtube_metadata_collector`. The local package/frontmatter name is `youtube-metadata-collector` because local Skill packages use hyphen-case.

## Purpose

Create a source metadata YAML file for a YouTube video in:

```text
sources/youtube/metadata/
```

This is the source-intake step before:

1. `youtube_note_architect` creates a blueprint from transcript + metadata.
2. `youtube_note_generator` creates the final LaTeX note from the blueprint.

## Core Workflow

1. Extract the YouTube video ID from the provided URL.
2. Normalize `canonical_youtube_url`.
3. Prefer user-provided classification fields over inferred values.
4. Fetch public video metadata when possible:
   - first with `YOUTUBE_API_KEY` and the YouTube Data API,
   - then with `yt-dlp` if installed,
   - then with YouTube oEmbed,
   - finally URL-only fallback.
5. Infer educational fields from the title, fetched tags, description, transcript hints, and user hints.
6. Write a stable YAML file under `sources/youtube/metadata/`.
7. Do not silently overwrite existing files. Create a versioned file unless the user requests overwrite or missing-field update.
8. Return the created path, fetched fields, inferred fields, empty fields, and the next workflow step.

## Recommended Script

Use the bundled script for deterministic file creation:

```bash
python youtube-metadata-collector/scripts/create_youtube_metadata.py \
  "https://www.youtube.com/watch?v=yNpP11ffwVM&t=203s" \
  --domain mathematics \
  --subdomain complex-analysis \
  --target-note-language en \
  --output-dir sources/youtube/metadata
```

Useful options:

```bash
--title
--channel
--date-watched
--date-processed
--difficulty
--source-language
--target-note-language
--status
--slug
--topics
--tags
--prerequisites
--transcript-available
--dry-run
--allow-overwrite
--update-missing
```

Load `references/metadata-schema.md` when the field schema matters. Load `references/status-workflow.md` when deciding the correct `status`.

## API Key

If the user wants API mode, they must set:

```bash
export YOUTUBE_API_KEY="..."
```

Never hardcode, print, or commit API keys.

## Safety Rules

- Do not invent exact YouTube facts such as channel, publication date, duration, description, or thumbnail URL.
- It is acceptable to infer educational fields such as domain, subdomain, topics, tags, difficulty, and prerequisites.
- Prefer explicit user values over fetched values, and fetched values over inferred values.
- Use `status: "metadata_created"` by default.
- Use `status: "transcribed"` only when the transcript is actually saved or the user explicitly passes `--transcript-available`.
- Keep YAML human-editable and stable.

