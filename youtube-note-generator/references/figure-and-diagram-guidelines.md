# Figure and Diagram Guidelines

Use this when the blueprint calls for figures, plots, diagrams, tables, or supporting figure code.

## Implementation Choices

- Use TikZ for geometry, vectors, probability trees, timelines, conceptual diagrams, flowcharts, and lightweight schematics.
- Use pgfplots for analytic functions and small data plots that belong directly in LaTeX.
- Use external matplotlib code for simulation-heavy, empirical, or complex multi-panel figures when the user requests supporting code.
- Use tables with `booktabs` for notation summaries, comparisons, parameter values, numerical ledgers, and algorithm traces.
- Use figure placeholders only when the visual is important but exact data or geometry is unavailable.

## Figure Requirements

For every figure or table:

- Introduce it in the surrounding prose.
- Use a clear caption that explains the educational point.
- Label it with `\label{fig:...}` or `\label{tab:...}` when referenced later.
- Keep notation, units, axes, parameters, and colors consistent with the text.
- Explain any approximation or generated data.

## pgfplots Rules

- Set `\pgfplotsset{compat=1.18}` unless the environment requires another version.
- Label axes and include units when relevant.
- Specify parameter values used in plotted functions.
- Avoid overly dense plots.

## TikZ Rules

- Use simple, readable diagrams.
- Label important points, vectors, regions, or transitions.
- Define coordinate systems and sign conventions when relevant.
- Keep diagrams pedagogical rather than decorative.

## External Figure Code

When creating supporting code:

- Use deterministic inputs or set a random seed.
- Save figures to a predictable path.
- Reference saved files with `\includegraphics`.
- Include a brief comment explaining how to regenerate the figure.
