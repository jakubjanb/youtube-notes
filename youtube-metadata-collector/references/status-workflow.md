# Status Workflow

Valid statuses:

```yaml
status: "metadata_created"
status: "transcript_needed"
status: "transcribed"
status: "blueprint_created"
status: "note_generated"
status: "published"
```

## Defaults

Use:

```yaml
status: "metadata_created"
```

when creating metadata from only a URL.

Use:

```yaml
status: "transcript_needed"
```

when the user explicitly wants the metadata to mark that transcript capture is still pending.

Use:

```yaml
status: "transcribed"
```

only when the transcript is actually saved or the user explicitly says the transcript already exists.

## Next Steps

After metadata creation:

1. Save transcript to `sources/youtube/transcripts/<slug>.md`.
2. Run `youtube_note_architect` to create `blueprints/<domain>/<slug>.md`.
3. Run `youtube_note_generator` to create `notes/<domain>/<slug>/note.tex`.

