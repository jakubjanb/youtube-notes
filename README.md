# YouTube Notes

A personal "second brain" pipeline that turns educational YouTube videos into polished, durable LaTeX study notes — organized by domain, linked by prerequisites, indexed for long-term retrieval.

> **Heads-up:** this is a personal project. The repo is open in case the workflow, LaTeX setup, or conventions are useful to you, but it isn't a product and isn't actively supported. Fork freely.

## Why

Most great explainers on YouTube get watched once and forgotten. The goal here is the opposite: take a video worth watching twice, run it through a structured pipeline, and end up with a self-contained note — metadata, transcript, blueprint, LaTeX source, and a compiled PDF — that lives in a long-term knowledge base.

Domains covered: mathematics, physics, statistics, probability, data science, machine learning, AI, computer science, quantitative finance.

## Sample notes

To see what the pipeline actually produces:

- [Marden's theorem](notes/mathematics/mardens-theorem/note.pdf) — complex analysis, Steiner inellipse, electrostatic interpretation
- [Envelope curves](notes/mathematics/envelope-curves/note.pdf) — analytic and geometric envelopes

Each note folder ships its full provenance: source metadata, full transcript, generation blueprint, LaTeX source, and the compiled PDF.

## How the pipeline works

```text
YouTube URL ──► sources/youtube/metadata/<slug>.yaml      (Skill: youtube_metadata_collector)
transcript ───► sources/youtube/transcripts/<slug>.md     (manual / inbox)
metadata + transcript ──► blueprints/<domain>/<slug>.md   (Skill: youtube_note_architect)
blueprint ────► notes/<domain>/<slug>/note.tex            (Skill: youtube_note_generator)
note.tex ─────► note.pdf                                  (make build)
```

Three Claude Skills do the heavy lifting:

- **`youtube_metadata_collector`** — fetches structured YouTube facts (channel, duration, description, thumbnails) and infers educational metadata (domain, prerequisites, difficulty). Never invents source facts.
- **`youtube_note_architect`** — converts a transcript into a structured blueprint with concept map, definitions, derivations, examples, and visualization plans. Plan only, no LaTeX.
- **`youtube_note_generator`** — turns a blueprint into a complete LuaLaTeX document, verifying math along the way and using a shared library of box environments for definitions, intuition, warnings, examples, and results.

## Repository layout

```text
config/          Project vocabularies and LaTeX settings.
inbox/           Staging area for new captures.
sources/         Long-term archive of transcripts and source metadata.
blueprints/      Structured plans produced by youtube_note_architect.
notes/           Final note folders, grouped by domain.
latex/           Shared preamble, macros, environments, and templates.
figures/         Reusable figure source files and exports.
knowledge-base/  Indexes, concept maps, prerequisite graphs, learning paths.
templates/       Markdown / YAML / LaTeX scaffolding.
scripts/         Stdlib-only Python automation.
docs/            Workflow, naming, schemas, LaTeX style guide.
```

## Quickstart

Create source metadata from a YouTube URL:

```bash
make metadata URL="https://www.youtube.com/watch?v=..." DOMAIN=mathematics SUBDOMAIN=complex-analysis
```

Scaffold a new note folder:

```bash
make new-note TITLE="Gradient Descent Intuition" DOMAIN=machine-learning
```

Compile a note to PDF:

```bash
make build TEX=notes/machine-learning/gradient-descent-intuition/note.tex
```

Validate every metadata file in the repo:

```bash
make validate
```

Refresh knowledge-base indexes from notes metadata:

```bash
make update-index
```

## Requirements

- Python 3 (stdlib only — no pip dependencies for the automation scripts).
- A LuaLaTeX toolchain. `latexmk` is preferred; bare `lualatex` works as a fallback. Builds keep their TeX cache local under `latex/builds/`.
- Optional: `YOUTUBE_API_KEY` in the environment for richer metadata fetching. Without it, the metadata collector falls back to scraping public fields.

## Conventions in one paragraph

Slugs are lowercase ASCII kebab-case and concept-first (`gradient-descent-intuition`, never `3blue1brown-gradient-descent-2023`). Domains are fixed in `config/domains.yaml`. Every note and source file carries metadata validated by `scripts/validate_metadata.py`. Cross-references in LaTeX go through `cleveref` with prefixed labels (`sec:`, `eq:`, `fig:`, `def:`, `thm:`, `ex:`). Final notes live at `notes/<domain>/<slug>/`, never directly under `notes/`. Full rules in `docs/`.

## Further reading

- [PROJECT_GUIDE.md](PROJECT_GUIDE.md) — architecture and the note-folder contract.
- [docs/workflow.md](docs/workflow.md) — end-to-end editorial workflow.
- [docs/metadata-schema.md](docs/metadata-schema.md) — required metadata fields.
- [docs/latex-style-guide.md](docs/latex-style-guide.md) — LaTeX conventions and box environments.
- [docs/naming-conventions.md](docs/naming-conventions.md) — slug, tag, and label rules.

## A note on content

The notes here are personal study artifacts derived from third-party YouTube material. The underlying video content remains the property of the original creators, who are credited in each note's `metadata.yaml` (`source_url`, `source_channel`, `source_title`).
