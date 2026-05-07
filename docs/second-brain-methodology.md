# Second-Brain Methodology

This repository should grow as a scientific knowledge system, not a pile of generated files.

## Atomic Notes

Final video notes can be long, but concepts should become atomic when they recur. If `gradient`, `expected value`, `convexity`, or `eigenvector` appears across many notes, create a concept card using `templates/concept-card.md`.

Atomic concept cards should answer:

- What does this concept mean?
- Why does it matter?
- What are the prerequisites?
- Where does it appear?
- What should I learn next?

## Maps Of Content

Maps of content are curated entry points. They should not be exhaustive dumps. A good map tells you what matters, in what order, and why.

Update maps when:

- a note becomes central to a topic,
- a gap becomes obvious,
- a prerequisite chain changes,
- several related notes need an overview.

## Links And Relationships

Every mature note should record:

- prerequisites,
- related notes,
- follow-up topics,
- important concepts,
- maps of content it belongs to.

Use links in both directions when possible. If a new note depends on an old note, consider updating the old note's `related_notes`.

## Learning Paths

Learning paths are sequences for future study. They should include checkpoints and transitions, not only links.

Example:

```text
vectors -> matrix multiplication -> gradients -> gradient descent -> backpropagation
```

## Avoiding Duplication

Before creating a new concept card or map, search for existing names and synonyms. Prefer improving an existing card over creating a duplicate.

Useful commands:

```bash
rg "expected value" knowledge-base notes
rg "gradient-descent" .
```

## Updating Old Notes

Old notes should evolve. When a better explanation appears:

- update `updated_at`,
- add a short maintenance note in the note README,
- preserve the original source transcript,
- avoid silently changing source claims without noting the reason.

## Review Rhythm

Occasionally run:

```bash
make validate
make update-index
```

Then inspect the generated indexes for messy tags, missing concepts, duplicate topics, and thin learning paths.

