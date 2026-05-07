# Visualization Guidelines

Suggest visuals only when they improve understanding, not as decoration.

## Choose the Method

- Use TikZ for geometric constructions, vector diagrams, causal diagrams, probability trees, timelines, and schematic concepts.
- Use pgfplots for analytic function plots that can be generated directly in LaTeX.
- Use matplotlib for data-heavy, simulation-based, empirical, or multi-panel plots that are easier to generate outside LaTeX.
- Use tables for comparisons, notation summaries, calculation ledgers, parameter choices, or before/after transformations.
- Use flowcharts for algorithms, proof strategies, data pipelines, and decision processes.
- Use annotated equations when the main visual value is explaining the role of terms in a formula.

## For Each Visual

Include:

- Title.
- Pedagogical purpose.
- What it should show.
- Recommended implementation method.
- Required formula, data, geometry, or algorithm state.
- Suggested caption.
- Target location in the note.
- Why the visual improves understanding.

## Quality Rules

- Prefer one clear teaching point per visual.
- Keep notation consistent with the text.
- State any parameter values used in plots.
- Mention if axes, units, scales, or normalizations are required.
- Use labels and captions that explain the idea, not merely the object.
- For probability or statistics visuals, specify distributions, parameters, sample sizes, and random variables.
- For physics visuals, specify coordinate systems, vectors, forces, fields, units, and sign conventions.
- For machine learning visuals, specify data, model, loss, parameters, and update or decision boundaries.
