# Derivation Quality Checklist

Use this checklist when the transcript contains formulas, proofs, calculations, algorithms, physics laws, statistics procedures, numerical examples, or machine learning steps.

## Extraction

- List every explicit equation, formula, identity, theorem, law, algorithm, and numerical calculation from the transcript.
- Add implied derivations only when the transcript relies on them for understanding.
- Preserve the transcript's intended result, but do not assume its correctness without reconstruction.
- Flag missing steps or unclear assumptions.

## Reconstruction

For each derivation or calculation, plan:

- Context and motivation before the first equation.
- Starting equation, definition, model, or principle.
- Variables, parameters, functions, indices, units, domains, and assumptions.
- Each algebraic, logical, probabilistic, geometric, algorithmic, or computational step.
- Substitutions and why they are valid.
- Simplifications and what conditions make them valid.
- Limits, approximations, or asymptotic arguments and their regimes.
- Intermediate equations that should appear in `align` or equivalent LaTeX environments.
- A final result that follows visibly from previous lines.

## Verification

Recommend appropriate checks:

- Substitute the result back into the starting relation.
- Perform dimensional or unit analysis.
- Test a special case with a known answer.
- Test a limiting case such as zero, infinity, symmetry, independence, identical variables, or small-parameter behavior.
- Recompute numerical examples independently.
- Check signs, constants, exponents, indices, normalization factors, base cases, and boundary conditions.
- Confirm the result is used only in its valid domain.
- For algorithms, check inputs, outputs, invariants, update rules, stopping conditions, and complexity claims.
- For statistics or machine learning, check assumptions, estimator definitions, loss functions, gradients, data leakage risks, and train/test distinctions.

## Presentation

Instruct the final writer to:

- Use `align`, `aligned`, `cases`, tables, pseudocode, or annotated equations as appropriate.
- Add short explanatory prose between equation blocks.
- Avoid jumping from a starting equation to the final result.
- Define symbols before first use.
- State assumptions near the derivation, not only in the introduction.
- Box or otherwise emphasize only the final result after the reasoning path is complete.
- Add a warning when a common incorrect shortcut is tempting.
