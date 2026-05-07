# Workflow

This is the standard end-to-end workflow for turning a YouTube video into a finished note.

## 1. Capture Video Metadata

Preferred automated path:

```bash
python youtube-metadata-collector/scripts/create_youtube_metadata.py \
  "https://www.youtube.com/watch?v=<video_id>" \
  --domain mathematics \
  --subdomain complex-analysis \
  --output-dir sources/youtube/metadata
```

Manual path: copy `templates/video-metadata.yaml` to:

```text
inbox/metadata/<slug>.yaml
```

Fill the video title, URL, channel, video ID, domain, topics, tags, difficulty, prerequisites, and status.

When the source is confirmed as worth processing, move it to:

```text
sources/youtube/metadata/<slug>.yaml
```

## 2. Add Transcript

Copy `templates/transcript-template.md` to:

```text
inbox/transcripts/<slug>.md
```

Paste the raw or cleaned transcript. Preserve timestamps when they are useful for checking the source.

When stable, move it to:

```text
sources/youtube/transcripts/<slug>.md
```

## 3. Generate Blueprint

Run `youtube_note_architect` with:

- topic or video title,
- cleaned transcript,
- source metadata,
- any personal instructions about emphasis or target depth.

Save the output to:

```text
blueprints/<domain>/<note-slug>.md
```

## 4. Create Note Folder

Use:

```bash
make new-note TITLE="Video Topic" DOMAIN=machine-learning
```

This creates:

```text
notes/<domain>/<note-slug>/
```

Copy the canonical source transcript into `transcript.md` and the architect blueprint into `blueprint.md`.

## 5. Generate LaTeX Note

Run `youtube_note_generator` with:

- the blueprint,
- source transcript when needed for fidelity checks,
- relevant metadata,
- the LaTeX conventions in `docs/latex-style-guide.md`.

Save the generated output to `note.tex`. Optionally keep a Markdown companion in `note.md`.

## 6. Compile PDF

Use:

```bash
make build TEX=notes/<domain>/<note-slug>/note.tex
```

The project prefers `latexmk` with LuaLaTeX. If `latexmk` is unavailable, the build script tries `lualatex`.

## 7. Review Quality

Use [note-quality-checklist.md](note-quality-checklist.md). Check conceptual clarity, notation consistency, derivations, examples, figures, metadata, and links.

## 8. Update Knowledge Base

Run:

```bash
make validate
make update-index
```

Then manually update:

- `knowledge-base/prerequisite-map.md`,
- relevant files in `knowledge-base/maps-of-content/`,
- `knowledge-base/learning-paths.md`,
- concept cards created from `templates/concept-card.md`.

## AI Agent Notes

Before editing an existing note, inspect the note folder. Do not overwrite `metadata.yaml`, `blueprint.md`, `transcript.md`, or `note.tex` unless the user explicitly wants regeneration. Prefer additive edits and preserve source provenance.
