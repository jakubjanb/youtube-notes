---
name: youtube-note-architect
description: Transform a provided YouTube video topic and transcript into a high-quality Markdown architecture for a future educational LaTeX note. Use when the user provides a transcript for mathematics, physics, statistics, probability, data science, machine learning, computer science, quantitative finance, or related technical domains and asks for a note plan, blueprint, scenario, or LaTeX-writing brief with explicit step-by-step derivation and correctness-check planning. This skill plans the note only; it does not write the final LaTeX document.
---

# youtube_note_architect

Visible skill name: `youtube_note_architect`. The local package/frontmatter name is `youtube-note-architect` because the validator requires hyphen-case.

## Purpose

Create a structured Markdown blueprint for a future educational LaTeX note from a YouTube transcript. Preserve the video's best teaching ideas, remove noise, reorganize for learning, and prepare clear instructions for a later LaTeX-writing agent.

Do not write the final LaTeX note. Do not download videos, transcribe audio, or browse externally unless the user explicitly asks for enrichment or verification.

## Workflow

1. Parse the topic/title, transcript, domain, audience level, target language, metadata, desired LaTeX style, rigor level, and special instructions.
2. Identify the main learning goal, inferred audience, prerequisites, central concepts, definitions, notation, formulas, derivations, algorithms, examples, visuals, warnings, and assumptions.
3. Remove filler, sponsorships, repeated phrasing, casual detours, calls to action, and irrelevant remarks.
4. Reconstruct the pedagogical sequence, then reorganize it when a clearer written explanation would teach better.
5. Treat the transcript as source material, not as something to quote or copy. Use concise conceptual references instead of long transcript quotations.
6. Mark optional enrichments clearly when adding explanations, examples, diagrams, exercises, edge cases, or alternative derivations beyond the transcript.
7. Plan every formula, derivation, proof sketch, algorithm, physical law, statistical result, worked example, numerical calculation, and procedure step by step.
8. Add correctness checks that force the final LaTeX-writing agent to verify the math and technical claims independently.
9. Return the required Markdown blueprint sections in order. Load `references/output-template.md` when the exact schema is useful.

## Derivations and Calculations

The `Step-by-Step Derivations and Calculation Plan` section is mandatory. For every derivation, equation, algorithm, proof sketch, numerical example, or worked calculation in or implied by the transcript:

- Name the source idea from the transcript.
- State the target result and starting point.
- Define assumptions, variables, notation, units, and domains of validity before use.
- Show the intended reasoning path line by line, including substitutions, transformations, simplifications, limits, approximations, and intermediate equations.
- Explain why each major step follows from the previous one.
- Include checks for algebra, units, dimensions, signs, constants, indices, edge cases, limiting cases, and numerical recomputation when relevant.
- Warn about likely mistakes.
- Suggest final LaTeX formatting, such as `align`, boxed final results, tables, TikZ diagrams, pgfplots figures, pseudocode, or annotated equations.

Load `references/derivation-quality-checklist.md` for a stricter checklist when the transcript is calculation-heavy.

## Blueprint Standards

- Optimize the structure for learning, not for preserving transcript order.
- Define every important symbol before using it.
- Keep notation consistent across the whole blueprint.
- Specify where formulas come from, what they mean, when they apply, and what assumptions they require.
- Preserve useful intuition, analogies, examples, and teaching moves from the video.
- Compress repetitive or conversational material.
- Flag thin, ambiguous, or missing transcript details so the final writer does not invent unsupported content.
- Suggest visuals only when they add pedagogical value. Load `references/visualization-guidelines.md` when planning diagrams, plots, tables, or flowcharts.

## Required Output

Produce a Markdown blueprint with these sections, in this order:

1. `Metadata`
2. `Executive Summary`
3. `Concept Map`
4. `Recommended LaTeX Note Structure`
5. `Key Definitions and Notation`
6. `Mathematical / Technical Core`
7. `Step-by-Step Derivations and Calculation Plan`
8. `Examples to Include`
9. `Visualizations and Diagrams`
10. `Pedagogical Enhancements`
11. `Transcript-to-Note Mapping`
12. `Optional Enrichments`
13. `Correctness Checks`
14. `Final Generation Instructions`

Use `references/output-template.md` as the canonical output skeleton. Use `references/example-blueprint.md` only when a compact example would help calibrate the level of detail.

## Correctness Requirements

In the `Correctness Checks` section, explicitly instruct the final LaTeX-writing agent:

> Do not trust the transcript blindly. Reconstruct and verify the derivation before writing it into the final LaTeX note.

Include checks for dimensional consistency, variable consistency, algebraic validity, signs, constants, exponents, indices, assumptions, edge cases, numerical recomputation, formulas' domains of validity, statistical or machine learning procedure accuracy, and consistency between final results and intermediate steps.

## Final Writer Brief

End with concise instructions for the next AI agent: tone, rigor, language, LaTeX style, mathematical formatting, definitions, step-by-step derivations, worked examples, diagrams, citations or references if requested, correctness verification, and how to distinguish transcript-derived content from optional enrichment.
