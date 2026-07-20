# Claim contract - L1 fixed-support cross-determinant fiber bound

## Inputs

- one source chart, defect degree, and exact petal-support pattern;
- exact monic defect locators and saturated numerator pairs;
- the L1 polarity encoding and generated-field bound for the aggregate.

## Output

The fixed-support pair set injects into polynomials of degree at most
`r_cross=2d+v-t ell`, giving `(FB3)`. Every fixed `(p,r_cross)` box is
polynomial per source chart with explicit bound `(FB6)`.

## Consumer rule

Consumers may restrict a bounded-polarity per-chart counterfamily to
unbounded cross slack. They must retain non-intrinsic first-match chart
multiplicity and the growing-polarity branch.

## Falsifier

Two different exact saturated pairs with the same quotient `(FB4)`, a cross
determinant not divisible by every selected-support locator, or a fixed
`(p,r_cross)` per-chart family exceeding `(FB6)`.
