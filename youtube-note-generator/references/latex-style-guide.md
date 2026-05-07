# LaTeX Style Guide

Use this reference when building the final `.tex` source.

## Package Policy

Default package set:

```latex
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{siunitx}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{array}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{cleveref}
\usepackage{enumitem}
\usepackage{geometry}
\usepackage{microtype}
\usepackage[most]{tcolorbox}
\usepackage{tikz}
\usepackage{pgfplots}
```

Use `physics` only when its commands genuinely simplify the document and do not conflict with preferred notation. Use `babel` or `polyglossia` when the target language requires it. Use `fontspec` only for XeLaTeX or LuaLaTeX.

## Writing Standards

- Use precise, readable mathematical prose.
- Introduce notation before first use.
- State assumptions near the result that depends on them.
- Give the learner signposts: goal, idea, derivation, interpretation, check.
- Keep paragraphs short enough for a study note.
- Avoid transcript-like phrasing, filler, or conversational detours.
- Prefer active explanations: "We substitute..." or "This term vanishes because..."
- Use optional enrichments only when marked or requested.

## Mathematical Formatting

- Use `align` for multi-line derivations.
- Use `aligned` inside boxes or displayed equations.
- Use `cases` for piecewise definitions.
- Use `\operatorname{}` for named operators not already defined.
- Use `\label{}` and `\cref{}` for important equations, figures, tables, definitions, and examples.
- Use `\boxed{}` sparingly for final formulas.
- Use `siunitx` for values with units.

## Box Conventions

Recommended semantic boxes:

- `definition` theorem environment for formal definitions.
- `proposition` or `theorem` for formal results.
- `example` theorem environment for worked examples.
- `intuitionbox` for conceptual explanations.
- `warningbox` for common mistakes and domain restrictions.
- `resultbox` for important final formulas.
- `summarybox` for section summaries or final takeaways.

Avoid turning every paragraph into a box. A polished note needs hierarchy, not decoration.
