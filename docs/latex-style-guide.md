# LaTeX Style Guide

The goal is readable professional notes, not decorative documents.

## Document Structure

Recommended structure:

1. Motivation and learning objectives.
2. Prerequisites and notation.
3. Definitions.
4. Main idea and intuition.
5. Formal derivation.
6. Worked examples.
7. Sanity checks and pitfalls.
8. Connections and follow-up topics.

## Equations

Use displayed equations for important relationships:

```latex
\begin{align}
  L(\theta) &= \frac{1}{n}\sum_{i=1}^{n} \ell(f_\theta(x_i), y_i).
\end{align}
```

Rules:

- Explain what each symbol means before using it heavily.
- Put short prose between derivation steps.
- Use `align` for multi-step derivations.
- Number only equations worth referencing.
- Label important equations with `\label{eq:descriptive-name}`.

## Derivations

A good derivation should state:

- assumptions,
- starting point,
- transformation at each step,
- reason for each non-obvious step,
- final result,
- sanity check or limiting case.

## Boxes

Use shared environments from `latex/templates/environments.tex`:

```latex
\begin{definitionbox}[title=Gradient]
...
\end{definitionbox}
```

Available boxes:

- `definitionbox`
- `intuitionbox`
- `warningbox`
- `examplebox`
- `resultbox`
- `checkpointbox`

Use boxes to clarify structure, not to decorate every paragraph.

## Figures

Prefer reproducible figures:

- TikZ for conceptual diagrams.
- pgfplots for mathematical plots.
- matplotlib for data-heavy plots.

Store note-specific figure sources in:

```text
notes/<domain>/<slug>/figures/source/
```

Store exported images in:

```text
notes/<domain>/<slug>/figures/exported/
```

Use labels:

```latex
\begin{figure}
  \centering
  \includegraphics[width=0.75\linewidth]{figures/exported/example.pdf}
  \caption{Descriptive caption.}
  \label{fig:descriptive-name}
\end{figure}
```

## References

Use `cleveref`:

```latex
As shown in \cref{eq:gradient-update}, ...
```

Label prefixes:

- `sec:`
- `eq:`
- `fig:`
- `tab:`
- `def:`
- `thm:`
- `ex:`

## Notation

Prefer notation that is standard in the relevant domain. If the video uses informal notation, normalize it in the note and mention any translation when needed.

Maintain a consistent choice for vectors, matrices, random variables, parameters, and operators within each note.

