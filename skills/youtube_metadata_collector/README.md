# youtube_metadata_collector

This folder is a project-level pointer for the `youtube_metadata_collector` workflow.

The implementation folder in this workspace is:

```text
youtube-metadata-collector/
```

Use the skill to create YouTube source metadata files stored at:

```text
sources/youtube/metadata/<note-slug>.yaml
```

Typical command:

```bash
python youtube-metadata-collector/scripts/create_youtube_metadata.py \
  "https://www.youtube.com/watch?v=yNpP11ffwVM&t=203s" \
  --domain mathematics \
  --subdomain complex-analysis \
  --output-dir sources/youtube/metadata
```
