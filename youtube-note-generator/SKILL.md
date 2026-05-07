---
name: youtube-note-generator
description: Generate a complete, polished LaTeX educational document from a structured Markdown blueprint produced by youtube_note_architect. Use when the user provides a note architecture, blueprint, plan, scenario, or LaTeX-writing brief for mathematics, physics, statistics, probability, data science, machine learning, computer science, quantitative finance, or related technical domains and asks for final LaTeX source, a compilable .tex note, worked derivations, examples, diagrams, exercises, or supporting figure code. Treat the blueprint as the primary source; use any transcript only for clarification or fidelity checks.
---

# youtube_note_generator

Visible skill name: `youtube_note_generator`. The local package/frontmatter name is `youtube-note-generator` because the validator requires hyphen-case.

## Purpose

Generate a complete, polished, modern educational LaTeX note from the structured blueprint produced by `youtube_note_architect`. Write the final `.tex` document unless the user asks for a multi-file LaTeX project or supporting figure files.

Treat the blueprint as the primary source of structure, pedagogy, notation, derivations, examples, visuals, and correctness requirements. Use an original transcript, when provided, only to clarify missing details, recover context, or check fidelity.

## Workflow

1. Parse the blueprint sections: metadata, summary, concept map, recommended structure, definitions, technical core, derivation plan, examples, visuals, pedagogy, mappings, optional enrichments, correctness checks, and final generation instructions.
2. Apply user preferences for target language, audience level, rigor, length, visual style, exercises, summaries, output format, and LaTeX engine.
3. Verify mathematical and technical content before writing final formulas, derivations, examples, algorithms, or results. Do not reproduce blueprint mistakes blindly.
4. Build a complete LaTeX source document with a clean preamble, title, optional table of contents, sections, definitions, derivations, worked examples, figures or placeholders, summaries, warnings, exercises when useful, conclusion, and optional appendices.
5. Define notation before use and keep notation consistent across the document.
6. Write derivations and calculations step by step with explanatory prose between equation blocks.
7. Mark optional enrichments carefully when they go beyond the transcript or blueprint.
8. If producing files in a workspace, create a single `.tex` file by default. Add figure source files only when requested or clearly needed.
9. If compilation is requested or feasible in the active task, compile with the requested engine or a suitable default and fix errors.

Load `references/latex-note-template.tex` when a reusable preamble and document skeleton is useful.

## Mathematical Reasoning Standard

For every derivation, proof sketch, equation transformation, physical law, statistical formula, algorithm, numerical example, worked example, probability calculation, machine learning procedure, data science workflow, or technical calculation:

- State the goal.
- Define variables, notation, assumptions, units, and domains of validity.
- Present the starting equation, definition, model, or principle.
- Show intermediate equations in readable `align`, `aligned`, `split`, `cases`, table, or pseudocode form.
- Explain each transformation, substitution, simplification, limit, approximation, or algorithmic update.
- Highlight the final result only after the reasoning path is complete.
- Interpret the result in plain language.
- Check correctness when possible.

Never jump from the starting point to the final result without the reasoning path. Load `references/reasoning-and-verification-checklist.md` for technical or calculation-heavy notes.

## LaTeX Style

Use modern scientific LaTeX practices:

- Clean typography, readable section hierarchy, and restrained visual style.
- `amsmath`, `amssymb`, `amsthm`, `mathtools`, `microtype`, `geometry`, `hyperref`, `cleveref`, `enumitem`, `booktabs`, `array`, `graphicx`, `xcolor`, `tcolorbox`, `tikz`, and `pgfplots` when appropriate.
- `siunitx` for units and numerical formatting when relevant.
- Avoid unnecessary packages; include `physics` only if its commands are useful and compatible with the document's notation.
- Use definition, theorem/proposition, intuition, warning, example, result, and exercise boxes only when they improve clarity.
- Prefer cross-references over repeated labels such as "the equation above" in longer notes.
- Keep figures pedagogical, captioned, and tied to the text.

Load `references/latex-style-guide.md` for the package policy, box conventions, and writing standards.

## Correctness Requirements

Before finalizing the LaTeX:

- Check algebraic consistency.
- Check dimensional and unit consistency.
- Check notation consistency.
- Check signs, constants, exponents, indices, assumptions, and domains of validity.
- Recompute numerical examples independently.
- Test symbolic results by substitution, dimensional analysis, special cases, limiting cases, alternative derivation, or sanity check when appropriate.
- Check that examples, figures, tables, and captions match the formulas or data they illustrate.

If the blueprint seems incorrect, incomplete, or ambiguous, correct it when confidence is high and note the correction briefly. Otherwise, include a clearly marked note or assumption instead of pretending certainty.

## Output

By default, output one complete `.tex` source document. If writing a file, use a descriptive filename derived from the topic. If the user requests inline output, provide the LaTeX in one fenced `latex` block.

When supporting figure code is requested, provide it as separate files or clearly separated code blocks and reference them from the LaTeX.

For blueprint-to-document mapping guidance, load `references/blueprint-to-latex-map.md`. For visualization implementation details, load `references/figure-and-diagram-guidelines.md`.
