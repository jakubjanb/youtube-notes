---
name: youtube-notes-planner
description: Transform a provided YouTube video topic and transcript into a structured educational LaTeX note plan, outline, blueprint, scenario, or notes-writing plan. Use when the user provides or references an already available YouTube transcript for mathematics, physics, statistics, data science, machine learning, or related technical fields and asks to plan a polished educational note rather than write the final LaTeX document.
---

# YouTube Notes Planner

## Purpose

Create a Markdown blueprint for a future LaTeX note from a user-provided YouTube transcript. Preserve the video's strongest teaching logic, remove noise, reorganize for clarity when helpful, and produce a plan suitable for a separate LaTeX-writing step.

Do not write the final LaTeX document. Do not download videos, transcribe audio, or browse the web unless the user explicitly asks for external enrichment or verification.

## Workflow

1. Parse the input for topic/title, transcript, domain, audience level, language preference, metadata, and special instructions.
2. Identify the core concept, learning goal, prerequisites, conceptual sequence, examples, formulas, derivations, diagrams, warnings, and implied assumptions.
3. Clean the transcript mentally: ignore sponsorships, filler, repeated phrasing, casual detours, calls to action, and irrelevant remarks.
4. Reorganize the material into the clearest educational progression while preserving the transcript's main teaching arc.
5. Add missing context only when it improves learning and stays faithful to the topic. Mark anything not directly supported by the transcript as optional enrichment.
6. Suggest visualizations only when they add explanatory value. Prefer TikZ for geometric or schematic diagrams, pgfplots for analytic plots in LaTeX, matplotlib for generated data-heavy plots, and tables for structured comparisons.
7. Return a structured Markdown blueprint using the required section order. For the exact schema, example input, output skeleton, visualization rules, and quality checklist, read `references/blueprint-template.md`.

## Planning Standards

- Treat the transcript as source material, not as a script to copy.
- Prefer didactic clarity over exhaustive coverage.
- Preserve useful intuition, examples, analogies, definitions, and derivation logic from the transcript.
- Distinguish transcript-derived content from optional AI-added enrichments.
- Avoid hallucinating advanced claims, edge cases, references, or formulas not grounded in the transcript unless clearly marked optional.
- Use mathematical notation consistently and state assumptions before using them.
- Include warnings, common mistakes, edge cases, and conceptual checkpoints where they help the future note teach better.
- Keep long quotations out of the plan; mention transcript fragments conceptually instead.

## Required Output

Produce a Markdown blueprint with these sections, in this order:

1. `Metadata`
2. `Executive Summary`
3. `Concept Map`
4. `Recommended LaTeX Note Structure`
5. `Key Definitions and Notation`
6. `Mathematical / Technical Core`
7. `Examples to Include`
8. `Visualizations and Diagrams`
9. `Pedagogical Enhancements`
10. `Transcript-to-Note Mapping`
11. `Optional Enrichments`
12. `Final Generation Instructions`

If the transcript is too thin, noisy, or missing key details, still produce the blueprint, but explicitly flag uncertainty and list the missing information that the LaTeX-writing agent should not invent.
