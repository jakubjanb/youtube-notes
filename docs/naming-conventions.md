# Naming Conventions

Consistent names keep the repository searchable and easy for AI agents to operate.

## Slugs

Use lowercase kebab-case:

```text
gradient-descent-intuition
eigenvalues-and-eigenvectors
bayesian-updating
lagrangian-mechanics-intuition
```

Rules:

- ASCII lowercase letters and numbers.
- Words separated by single hyphens.
- No dates unless needed for disambiguation.
- No channel names unless the topic alone is ambiguous.
- Prefer concept names over clickbait titles.

Use:

```bash
python3 scripts/slugify.py "Gradient Descent Intuition"
```

## Note Folders

Final notes live at:

```text
notes/<domain>/<note-slug>/
```

Do not put final notes directly under `notes/`.

## Files

Use canonical names inside note folders:

- `README.md`
- `metadata.yaml`
- `transcript.md`
- `blueprint.md`
- `note.md`
- `note.tex`
- `note.pdf`

## Domains

Use the domain keys in `config/domains.yaml`. If a note crosses domains, choose the primary domain and record the others in `topics`, `tags`, `related_notes`, or a map of content.

## Tags

Use lowercase kebab-case:

```text
gradient-descent
linear-algebra
bayesian-inference
energy-methods
```

Prefer reusable tags. Avoid near-duplicates such as `neural-network`, `neural-networks`, and `nn` unless there is a specific reason.

## Concept Cards

Concept cards should be named by the concept slug:

```text
knowledge-base/concepts/expected-value.md
knowledge-base/concepts/convexity.md
```

If a concept cards folder is introduced later, keep it separate from final video notes.

## Maps Of Content

Maps of content live at:

```text
knowledge-base/maps-of-content/<topic-slug>.md
```

Use broad topic names such as `linear-algebra.md`, `optimization.md`, or `statistical-inference.md`.

