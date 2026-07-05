# e22_challenger_staircase_pricing

- **status:** CONDITIONAL
- **closure:** proof

## Statement

The mixed/full-petal E15 successor class has an exact quotient-coset
staircase count formula, compatible with the X-4 identification as
`L_B G(X^M)`-type locators, and the resulting challenger column is priced in
the list-side integer comparison alongside `planted_count`.

The deliverable is the explicit formula, its injectivity/no-overlap proof, and
the row-by-row comparison against the list threshold.

## Conditional decomposition

This node is conditional on:

- `e22_staircase_parametrization`
- `e22_staircase_injectivity`
- `e22_staircase_arithmetic_pricing`

## Falsifier

Two distinct staircase parameters yielding the same challenger word without
being quotient-equivalent, or a structured challenger subfamily not covered by
the formula.
