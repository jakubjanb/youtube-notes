# YouTube Transcript to LaTeX Note Blueprint Reference

Use this reference when producing the final Markdown blueprint. Keep content concise but specific enough that a later LaTeX writer can produce a polished technical note without re-reading the transcript.

## Output Schema

```markdown
# Blueprint: <topic>

## 1. Metadata
- Topic:
- Domain:
- Estimated audience level:
- Main learning goal:
- Prerequisites:
- Source status: Transcript-derived plan, with optional enrichments clearly marked.

## 2. Executive Summary
Write 5-10 sentences summarizing what the final note should teach, why the concept matters, the main teaching route, and the expected conceptual payoff.

## 3. Concept Map
- Main concepts:
- Supporting concepts:
- Dependencies between concepts:

## 4. Recommended LaTeX Note Structure
For each proposed section or subsection, include:
- Title:
- Content:
- Pedagogical rationale:

## 5. Key Definitions and Notation
- Terms:
- Symbols:
- Units or dimensions, if relevant:
- Assumptions:

## 6. Mathematical / Technical Core
- Important formulas:
- Derivations:
- Algorithms or procedures:
- Modeling assumptions, physical laws, or statistical principles:
- Rigor notes:

## 7. Examples to Include
For each example, include:
- Source: Transcript-derived, improved from transcript, or optional addition.
- Purpose:
- Setup:
- Calculation or explanation flow:
- Expected result or takeaway:

## 8. Visualizations and Diagrams
For each visual, include:
- Purpose:
- What it should show:
- Recommended implementation method:
- Data or formula needed:
- Suggested caption:
- Why it improves understanding:

## 9. Pedagogical Enhancements
- Intuition:
- Analogies:
- Common misconceptions:
- Warnings:
- Edge cases:
- Conceptual checkpoints:

## 10. Transcript-to-Note Mapping
Map transcript ideas to note sections. Mention ideas conceptually without long quotes.

## 11. Optional Enrichments
List additional remarks, examples, references, or visuals that could improve the note. Clearly label each item as optional and not directly from the transcript.

## 12. Final Generation Instructions
Give concise instructions for the next AI agent: tone, rigor level, notation, formatting, theorem/definition/example environments, visualization expectations, and constraints about transcript fidelity.
```

## Visualization Guidance

- Use TikZ for geometric constructions, directed graphs, timelines, commutative diagrams, vector diagrams, probability trees, and conceptual schematics.
- Use pgfplots for analytic function plots, distributions, convergence curves, loss curves, residual plots, and small reproducible plots that belong directly in LaTeX.
- Use matplotlib when the visual needs generated data, simulations, many points, heatmaps, numerical experiments, or preprocessing before inclusion.
- Use tables for comparisons, notation summaries, assumptions, algorithm steps, confusion matrices, or small numerical results.
- Do not suggest visuals for decoration. Every visual must carry a learning purpose.
- Include formulas, parameter values, axes, labels, and captions when the later LaTeX writer would need them.

## Quality Checklist

Before finalizing, verify that the blueprint:

- Produces a plan, not the final LaTeX note.
- Keeps transcript-derived content separate from optional enrichment.
- Removes filler, sponsorships, repeated wording, and casual noise.
- Preserves the core explanatory sequence or improves it with clear rationale.
- States definitions, notation, assumptions, formulas, and derivation steps clearly.
- Includes examples and visuals only when educationally useful.
- Flags uncertainty when the transcript is incomplete or ambiguous.
- Avoids unsupported advanced claims unless marked optional.
- Gives the next LaTeX-writing agent concrete generation instructions.

## Example Input

```text
Topic: Gradient descent intuition
Audience: Undergraduate data science students
Transcript: Today we are going to understand gradient descent. Imagine standing on a hill in fog...
The loss function tells us how wrong our model is. The gradient points uphill, so we step in the
negative gradient direction. If the learning rate is too large, we overshoot; if too small, training
is slow. For a simple quadratic J(w) = (w - 3)^2, the derivative is 2(w - 3)...
```

## Example Output Skeleton

```markdown
# Blueprint: Gradient Descent Intuition

## 1. Metadata
- Topic: Gradient descent intuition
- Domain: Machine learning / optimization
- Estimated audience level: Undergraduate data science students
- Main learning goal: Understand gradient descent as iterative loss minimization using local slope information.
- Prerequisites: Functions, derivatives, basic algebra, idea of model error.

## 2. Executive Summary
The final note should introduce gradient descent as a practical method for minimizing a loss function...

## 3. Concept Map
- Main concepts: loss function, gradient, update rule, learning rate, convergence behavior.
- Supporting concepts: derivative sign, step size, local versus global information.
- Dependencies between concepts: define loss before gradient; define gradient before update rule; discuss learning rate after update rule.

## 4. Recommended LaTeX Note Structure
- Title: Motivation: learning as loss minimization
  Content: Explain why training can be framed as reducing an error measure.
  Pedagogical rationale: Gives purpose before formulas.

## 5. Key Definitions and Notation
- `J(w)`: loss as a function of parameter `w`.
- `\eta`: learning rate.

## 6. Mathematical / Technical Core
- Update rule: `w_{t+1} = w_t - \eta \nabla J(w_t)`.
- Quadratic example: for `J(w) = (w - 3)^2`, use `J'(w) = 2(w - 3)`.

## 7. Examples to Include
- Source: Transcript-derived.
  Purpose: Show one-dimensional gradient descent numerically.

## 8. Visualizations and Diagrams
- Purpose: Show descent along a quadratic bowl.
  What it should show: Curve `J(w) = (w - 3)^2` with successive iterates.
  Recommended implementation method: pgfplots.
  Data or formula needed: `J(w) = (w - 3)^2`, chosen `w_0`, `\eta`.
  Suggested caption: "Gradient descent iterates move against the local slope toward the minimum."
  Why it improves understanding: Connects the update formula to visible movement.

## 9. Pedagogical Enhancements
- Warning: The gradient points uphill; the update uses the negative gradient.

## 10. Transcript-to-Note Mapping
- Hill-in-fog analogy -> motivation and intuition section.
- Large versus small learning rate -> learning-rate warning section.

## 11. Optional Enrichments
- Optional: Add a short note distinguishing convex and non-convex loss landscapes.

## 12. Final Generation Instructions
Write a clear undergraduate-level LaTeX note with definitions, one worked quadratic example, one pgfplots figure, and concise warnings about learning-rate choice. Do not turn optional enrichments into central claims.
```
