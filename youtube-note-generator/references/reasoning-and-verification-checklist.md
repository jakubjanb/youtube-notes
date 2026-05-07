# Reasoning and Verification Checklist

Use this before committing formulas, derivations, calculations, algorithms, examples, or figures to the final LaTeX source.

## Step-by-Step Reasoning

For each technical item, include:

- Goal of the derivation or calculation.
- Definitions of variables, parameters, units, domains, and assumptions.
- Starting equation, definition, law, theorem, algorithm, or model.
- Intermediate equations.
- Explanation of every nontrivial algebraic transformation.
- Justification for substitutions, cancellations, limits, approximations, independence assumptions, or algorithmic updates.
- Final result.
- Interpretation of what the result means.

Do not skip from the starting point to the final result.

## Verification

Check whichever are relevant:

- Substitute the result into the original equation or definition.
- Check dimensions and units.
- Test special cases with known behavior.
- Test limiting cases such as zero, infinity, symmetry, independence, identical values, or small-parameter limits.
- Recompute numerical examples independently.
- Check signs, constants, exponents, indices, base cases, normalization factors, and boundary conditions.
- Confirm formulas are used only in their domain of validity.
- Confirm statistical or machine learning claims use the right assumptions and data split.
- Confirm algorithm descriptions include inputs, outputs, update rules, stopping conditions, and complexity only when justified.

## Handling Problems

If the blueprint appears wrong:

- Correct the result if the fix is clear and explain the correction briefly in an implementation note or footnote when useful.
- If the issue is ambiguous, state an assumption or include a caution in the note.
- Do not present uncertain or unverified math as definitive.
