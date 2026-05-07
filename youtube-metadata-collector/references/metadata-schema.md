# YouTube Source Metadata Schema

The Skill creates YAML files in:

```text
sources/youtube/metadata/<slug>.yaml
```

## Fields

- `title`: Video title. Fetched from API, yt-dlp, oEmbed, or user input.
- `youtube_url`: Original user-provided URL.
- `canonical_youtube_url`: Normalized `https://www.youtube.com/watch?v=<video_id>` URL.
- `channel`: Video channel title when fetched or provided.
- `video_id`: YouTube video ID extracted from the URL.
- `published_at`: Publication timestamp or date when fetched.
- `duration`: Duration when fetched, preferably ISO 8601 from the YouTube Data API.
- `description`: Description when fetched.
- `thumbnail_url`: Best available thumbnail URL.
- `date_watched`: User-provided date or today's date.
- `date_processed`: User-provided date or today's date.
- `domain`: User-provided or inferred broad domain.
- `subdomain`: User-provided or inferred subdomain.
- `topics`: User-provided or inferred human-readable topics.
- `tags`: User-provided or inferred lowercase kebab-case tags.
- `difficulty`: User-provided or inferred learning level.
- `prerequisites`: User-provided or inferred prerequisites.
- `source_language`: User-provided, fetched audio/default language, or default `en`.
- `target_note_language`: User-provided or default `en`.
- `status`: Workflow status.
- `related_notes`: Existing note links or slugs.
- `user_notes`: Optional source-intake notes from the user.

## Required Validation

The Skill must ensure:

- `video_id` is present.
- `youtube_url` is present.
- `canonical_youtube_url` is present.
- `date_processed` is present.
- `status` is valid.
- list fields are emitted as YAML lists.
- output is inside `sources/youtube/metadata/`.

## Empty Values

Use `""` for unknown scalar facts and `[]` for empty lists. Do not invent factual YouTube metadata.

