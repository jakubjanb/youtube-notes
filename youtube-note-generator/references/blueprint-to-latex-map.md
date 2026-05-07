# Blueprint-to-LaTeX Map

Use this mapping to transform a `youtube_note_architect` blueprint into a final `.tex` document.

## Metadata

- Title becomes `\title{...}`.
- Topic, domain, source, and target audience can appear in the abstract or a short source note.
- Rigor and length guide the density of proofs, examples, and appendices.
- Target language controls all visible prose and headings.

## Executive Summary

Turn into the abstract, introduction, and final conclusion. Do not paste it verbatim if it reads like planning prose.

## Concept Map

Use it to order the introduction and section transitions. Convert dependencies into prerequisite reminders or "roadmap" paragraphs.

## Recommended LaTeX Note Structure

Use as the section/subsection backbone, with sensible adjustments for flow. Preserve the pedagogical rationale through transitions and examples, not as meta-commentary.

## Key Definitions and Notation

Turn into formal definitions, notation paragraphs, and a notation table if there are many symbols. Define every important symbol before use.

## Mathematical / Technical Core

Turn formulas, laws, algorithms, procedures, and modeling assumptions into the main explanatory sections. State where each result comes from, what it means, when it applies, and what assumptions it needs.

## Step-by-Step Derivations and Calculation Plan

Turn each item into a fully written derivation with prose, intermediate equations, final result, interpretation, and checks. Use appendices for long derivations when the main flow would suffer.

## Examples to Include

Turn each into a worked example with given information, step-by-step solution, interpretation, and common mistake notes when useful.

## Visualizations and Diagrams

Implement visuals directly in TikZ/pgfplots when practical. Otherwise insert a clear LaTeX figure placeholder or reference supporting figure code requested by the user.

## Pedagogical Enhancements

Turn intuition, warnings, checkpoints, exercises, and misconceptions into concise boxes, paragraphs, or exercises. Mark optional additions if they go beyond the transcript.

## Transcript-to-Note Mapping

Use this only for fidelity. Do not include a mapping table in the final note unless the user explicitly asks for it.

## Optional Enrichments

Include optional enrichments only when they support the learning goal and do not distort the original video's focus. Label them as optional, aside, or extension when appropriate.

## Correctness Checks

Use these as a private verification plan and as occasional visible sanity checks in the note. Do not include a long checklist in the final document unless the user asks.

## Final Generation Instructions

Treat this as binding style and scope guidance unless it conflicts with the user's latest instructions.
