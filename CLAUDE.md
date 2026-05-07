# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal "second brain" pipeline that turns YouTube videos into polished LaTeX educational notes. Not application code — it is a content/knowledge repository with thin Python automation around it. Domains covered: mathematics, physics, statistics, probability, data science, ML, AI, CS, quantitative finance.

## Pipeline architecture

The repo is organized around a four-layer pipeline. Understanding the flow matters more than any single file:

```
YouTube URL ──► sources/youtube/metadata/<slug>.yaml      (Skill: youtube_metadata_collector)
transcript ───► sources/youtube/transcripts/<slug>.md     (manual / inbox)
metadata + transcript ──► blueprints/<domain>/<slug>.md   (Skill: youtube_note_architect)
blueprint ────► notes/<domain>/<slug>/note.tex            (Skill: youtube_note_generator)
note.tex ─────► note.pdf                                  (make build)
```

Layers:

1. **Source layer** — `inbox/` (unprocessed captures), `sources/` (durable archive of metadata + transcripts).
2. **Generation layer** — `blueprints/` (structured plans), `latex/` (shared preamble, macros, environments, templates).
3. **Knowledge artifact layer** — `notes/<domain>/<slug>/` (self-contained final note folders).
4. **Second-brain layer** — `knowledge-base/` (indexes, concept cards, prerequisite map, maps of content, learning paths).

The three Skills under `youtube-metadata-collector/`, `youtube-note-architect/`, `youtube-note-generator/` are the canonical implementations. `youtube-notes-planner/` is an older/parallel version of the architect — prefer `youtube-note-architect`. `skills/` contains pointer docs only, not implementations.

## Note folder contract

Every final note under `notes/<domain>/<slug>/` is self-contained and uses canonical filenames:

```
README.md  metadata.yaml  transcript.md  blueprint.md  note.md  note.tex  note.pdf
figures/source/  figures/exported/  attachments/
```

`note.pdf` is intentionally **not** gitignored — finished PDFs are the learning artifacts. LaTeX aux files are gitignored (`*.aux`, `*.fls`, etc.) and `latex/builds/` is the scratch dir.

Rule: do not overwrite an existing note's `metadata.yaml`, `blueprint.md`, `transcript.md`, or `note.tex` unless the user explicitly asks for regeneration. Prefer additive edits and preserve source provenance.

## Common commands

All run via the `Makefile` (delegating to `scripts/*.py`, stdlib-only Python 3):

```bash
# Create source metadata YAML from a YouTube URL
make metadata URL="https://www.youtube.com/watch?v=..." DOMAIN=mathematics SUBDOMAIN=complex-analysis

# Scaffold a new note folder under notes/<domain>/<slug>/
make new-note TITLE="Gradient Descent Intuition" DOMAIN=machine-learning

# Validate every metadata.yaml under notes/ + sources/youtube/metadata/
make validate

# Compile a single note to PDF (latexmk + lualatex preferred, lualatex fallback)
make build TEX=notes/machine-learning/gradient-descent-intuition/note.tex

# Compile every notes/**/note.tex
make build-all

# Refresh knowledge-base/ indexes from notes/ metadata
make update-index

# Remove LaTeX aux files repo-wide
make clean
```

To validate one file directly: `python3 scripts/validate_metadata.py path/to/metadata.yaml`. To slugify a title: `python3 scripts/slugify.py "Some Title"`.

`scripts/build_latex.py` sets `TEXMFVAR` and `TEXMFCONFIG` to `latex/builds/texmf-{var,config}` to keep the LaTeX cache local. There is no test suite and no linter config — `validate_metadata.py` is the only correctness gate.

## Allowed domains

`config/domains.yaml` is the source of truth. `scripts/new_note.py` enforces this whitelist:

```
mathematics, physics, statistics, probability, data-science,
machine-learning, artificial-intelligence, computer-science,
quantitative-finance, other
```

`other/` is a temporary holding area — prefer one of the stable domains. Cross-domain notes pick a primary domain and record the rest in `topics`/`tags`/`related_notes` or a map of content.

## Naming

- Slugs: lowercase ASCII kebab-case, no dates, no channel names — concept-first (`gradient-descent-intuition`, not `3blue1brown-gradient-descent-2023`).
- Tags: lowercase kebab-case; reuse before introducing near-duplicates (`neural-networks` vs `nn`).
- Final notes always live at `notes/<domain>/<slug>/` — never directly under `notes/`.

Full rules in `docs/naming-conventions.md`.

## Metadata

Metadata is the routing system of the second brain. Two schemas, both validated by `scripts/validate_metadata.py`:

- **Note metadata** (`notes/*/*/metadata.yaml`) — required: `title`, `slug`, `domain`, `subdomain`, `topics`, `tags`, `difficulty`, `prerequisites`, `source_type`, `source_url`, `source_title`, `source_channel`, `created_at`, `updated_at`, `status`, `latex_file`, `pdf_file`, `blueprint_file`, `transcript_file`, `related_notes`, `concepts`, `summary`.
- **Source metadata** (`sources/youtube/metadata/*.yaml`) — required: `title`, `youtube_url`, `canonical_youtube_url`, `channel`, `video_id`, `published_at`, `duration`, `description`, `thumbnail_url`, `date_watched`, `date_processed`, `domain`, `subdomain`, `topics`, `tags`, `difficulty`, `prerequisites`, `source_language`, `target_note_language`, `status`, `related_notes`.

Status vocabulary: `captured`, `transcribed`, `blueprint-drafted`, `note-drafted`, `needs-review`, `reviewed`, `published`, `archived`. The validator infers note vs source from presence of `source_type`/`slug` vs `youtube_url`/`video_id`.

Full schema: `docs/metadata-schema.md`.

## Skill semantics (important when invoking)

When working with the three Skills, treat their roles as strict:

- **`youtube_metadata_collector`** — never invents YouTube facts (channel, duration, description, thumbnails). Inferring educational fields (domain, topics, tags, difficulty, prerequisites) is fine. Does not silently overwrite — uses versioned filenames unless `--allow-overwrite` or `--update-missing`. Default status is `metadata_created`; only use `transcribed` when a transcript is actually saved.
- **`youtube_note_architect`** — produces a blueprint only, never the LaTeX. Required output sections (in order): Metadata, Executive Summary, Concept Map, Recommended LaTeX Note Structure, Key Definitions and Notation, Mathematical / Technical Core, Step-by-Step Derivations and Calculation Plan, Examples to Include, Visualizations and Diagrams, Pedagogical Enhancements, Transcript-to-Note Mapping, Optional Enrichments, Correctness Checks, Final Generation Instructions. The derivations section is mandatory and step-by-step — never collapse it. Mark anything beyond the transcript as "optional enrichment".
- **`youtube_note_generator`** — turns a blueprint into a single complete `.tex` document by default. Treats the blueprint as primary source; transcript only for fidelity checks. Verifies math before writing — does not blindly reproduce blueprint mistakes. Uses `latex/templates/{preamble,macros,environments}.tex` and the box environments documented in `docs/latex-style-guide.md` (`definitionbox`, `intuitionbox`, `warningbox`, `examplebox`, `resultbox`, `checkpointbox`).

`youtube-notes-planner/` is an older/parallel architect — do not edit notes through it; use `youtube-note-architect/`.

## LaTeX conventions (short version)

- Engine: LuaLaTeX via `latexmk` (preferred) or `lualatex` (fallback).
- Cross-references via `cleveref`. Label prefixes: `sec:`, `eq:`, `fig:`, `tab:`, `def:`, `thm:`, `ex:`.
- Figures: TikZ for diagrams, pgfplots for analytic plots, matplotlib for data-heavy plots. Note-local figures go under the note's `figures/source/` and `figures/exported/`; cross-note reusable figures go under top-level `figures/`.
- Use the shared box environments from `latex/templates/environments.tex` for structure, not decoration.

Full rules in `docs/latex-style-guide.md`.
