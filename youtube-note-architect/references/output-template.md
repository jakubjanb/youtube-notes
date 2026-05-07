# Output Template

Use this skeleton as the canonical Markdown blueprint. Keep the section order fixed.

## 1. Metadata

- Topic:
- Domain:
- Estimated audience level:
- Main learning goal:
- Prerequisites:
- Suggested rigor level:
- Suggested note length:
- Target language:
- Video metadata:
- Special user instructions:

## 2. Executive Summary

Write 5-10 sentences explaining the core idea, why it matters, what the learner should understand, the main examples or derivations, and the conceptual arc of the final note.

## 3. Concept Map

- Main concepts:
- Supporting concepts:
- Prerequisite concepts:
- Dependencies:
- Conceptual flow from intuition to formalism:

## 4. Recommended LaTeX Note Structure

For each proposed section or subsection:

- Proposed title:
- Purpose:
- Key content:
- Formulas or examples to include:
- Diagrams or visualizations to include:
- Pedagogical rationale:

Optimize for learning rather than copying transcript order.

## 5. Key Definitions and Notation

- Terms:
- Symbols:
- Variables:
- Functions:
- Parameters:
- Units or dimensions:
- Assumptions:
- Notation warnings:

State that every important symbol should be defined before first use.

## 6. Mathematical / Technical Core

Identify the technical heart of the note. Include formulas, theorems, identities, derivations, algorithms, statistical procedures, probability rules, optimization steps, machine learning concepts, physical laws, or modeling assumptions as relevant.

For every important equation:

- Source or motivation:
- Meaning:
- Applicability:
- Required assumptions:
- Explanation needed in the final note:

## 7. Step-by-Step Derivations and Calculation Plan

This section is mandatory.

### Derivation / Calculation: [Name]

- Transcript source idea:
- Goal:
- Starting point:
- Assumptions:
- Variables and notation:
- Step-by-step outline:
  1. ...
  2. ...
  3. ...
- Intermediate equations to show:
- Explanation needed between steps:
- Final result:
- Correctness checks:
- Common mistakes to warn about:
- Suggested LaTeX formatting:

Repeat for every derivation, equation, worked calculation, algorithm, proof sketch, numerical example, or procedure that appears in or is implied by the transcript.

## 8. Examples to Include

For each example:

- Example title:
- Educational purpose:
- Given information:
- Target result:
- Step-by-step solution plan:
- Calculations to show:
- Interpretation of the result:
- Correctness checks:
- Common mistakes:
- Possible extension or variation:

Clearly mark optional added examples as optional enrichment.

## 9. Visualizations and Diagrams

For each visualization:

- Title:
- Purpose:
- What it should show:
- Recommended implementation method:
- Required data, formula, or geometry:
- Suggested caption:
- Where it should appear:
- Why it improves understanding:

Use TikZ, pgfplots, matplotlib, tables, flowcharts, geometric diagrams, conceptual diagrams, probability trees, timelines, vector diagrams, distribution plots, or another suitable method.

## 10. Pedagogical Enhancements

- Transcript-derived intuition:
- Optional added intuition:
- Analogies:
- Conceptual checkpoints:
- Short exercises:
- Common misconceptions:
- Warnings:
- Edge cases:
- Alternative explanations:
- Links between intuitive and formal views:

Separate transcript-derived content from optional enrichments.

## 11. Transcript-to-Note Mapping

For each major transcript idea:

- Transcript idea:
- Target note section:
- Treatment: preserve, compress, expand, reorganize, or omit
- Reason:
- Related examples:
- Related derivations:

Use concise conceptual references instead of long transcript quotations.

## 12. Optional Enrichments

Each enrichment must be marked optional.

- Optional enrichment:
- Type:
- Why it helps:
- Where it fits:
- Constraint: explain how it preserves the video's focus.

Possible types include extra examples, historical notes, geometric interpretations, simulations, alternative derivations, limiting cases, practical applications, connections to other concepts, or short exercises with solution sketches.

## 13. Correctness Checks

Include checks for:

- Verify all derivations step by step.
- Recompute numerical examples independently.
- Check algebraic transformations.
- Check dimensions and units.
- Test special cases.
- Test limiting cases.
- Check notation consistency.
- Check assumptions.
- Check that each final formula follows from previous steps.
- Check that explanations match formulas.
- Check that visualizations correspond to correct formulas or data.
- Check signs, constants, exponents, indices, and boundary conditions.
- Check formulas' domains of validity.
- Check statistical, machine learning, physics, or algorithmic procedures for technical accuracy.

Required instruction to the final writer:

> Do not trust the transcript blindly. Reconstruct and verify the derivation before writing it into the final LaTeX note.

## 14. Final Generation Instructions

Give concise instructions for the future LaTeX-writing agent:

- Tone:
- Rigor level:
- Target language:
- LaTeX style:
- Mathematical formatting:
- Definition and notation policy:
- Step-by-step derivation policy:
- Worked example policy:
- Diagram policy:
- Citation or external-reference policy:
- Correctness verification policy:
- How to distinguish transcript-derived content from optional enrichment:
