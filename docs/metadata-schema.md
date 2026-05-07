# Metadata Schema

Metadata is the routing layer for notes, indexes, maps, and future search.

## YouTube Source Metadata

Use `templates/video-metadata.yaml`.

Required fields:

- `title`: Original video title or a clear normalized title.
- `youtube_url`: Full YouTube URL.
- `canonical_youtube_url`: Normalized `https://www.youtube.com/watch?v=<video_id>` URL.
- `channel`: Channel name.
- `video_id`: YouTube video ID.
- `published_at`: Publication timestamp or date when fetched; empty if unknown.
- `duration`: Video duration when fetched; preferably ISO 8601.
- `description`: Video description when fetched; empty if unavailable.
- `thumbnail_url`: Best available thumbnail URL when fetched.
- `date_watched`: Date you watched or selected the video, `YYYY-MM-DD`.
- `date_processed`: Date transcript processing began or completed, `YYYY-MM-DD`.
- `domain`: Primary domain from `config/domains.yaml`.
- `subdomain`: More specific area, for example `optimization`.
- `topics`: Human-readable topic list.
- `tags`: Reusable lowercase kebab-case tags.
- `difficulty`: `beginner`, `intermediate`, `advanced`, or `research`.
- `prerequisites`: Concepts or notes needed first.
- `source_language`: Language of the video or transcript.
- `target_note_language`: Language of the final note.
- `status`: Processing status.
- `related_notes`: Existing note slugs or links.

Optional but useful:

- `summary`
- `notes.capture_context`
- `notes.processing_notes`

## Generated Note Metadata

Use `templates/note-metadata.yaml`.

Required fields:

- `title`: Final note title.
- `slug`: Folder slug.
- `domain`: Primary note domain.
- `subdomain`: More specific area.
- `topics`: Human-readable topic list.
- `tags`: Reusable tag list.
- `difficulty`: Intended reader level.
- `prerequisites`: Concepts or notes needed before this note.
- `source_type`: Usually `youtube`.
- `source_url`: URL of the source video.
- `source_title`: Source title.
- `source_channel`: YouTube channel.
- `created_at`: Note creation date, `YYYY-MM-DD`.
- `updated_at`: Last substantial update date, `YYYY-MM-DD`.
- `status`: Note status.
- `latex_file`: Usually `note.tex`.
- `pdf_file`: Usually `note.pdf`.
- `blueprint_file`: Usually `blueprint.md`.
- `transcript_file`: Usually `transcript.md`.
- `related_notes`: Linked notes.
- `concepts`: Important concepts for indexing.
- `summary`: One-paragraph description.

## Status Values

Recommended values:

- `metadata_created`
- `transcript_needed`
- `transcribed`
- `blueprint_created`
- `note_generated`
- `published`

Older project notes may still use draft/review statuses such as `note-drafted`, `needs-review`, or `reviewed`. For YouTube source metadata, prefer the source-intake status values above.

## Validation

Run:

```bash
make validate
```

The validator checks that required fields are present and that key routing fields are not empty.
