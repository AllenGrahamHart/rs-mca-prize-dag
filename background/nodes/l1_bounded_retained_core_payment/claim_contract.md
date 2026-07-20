# Claim contract - L1 bounded retained-core payment

## Inputs

- one maximal-sunflower source chart and its ordered core;
- exact split defect and saturated numerator pairs;
- the L1 threshold, maximality, and polarized petal-support encoding.

## Output

Every fixed `(p,N-d)` box is polynomial per source chart with bound `(RC3)`.
Within the sub-Johnson tail, consumers may require both `p` and `N-d` to
escape arbitrary fixed caps.

## Falsifier

Two distinct degree-at-most-`d` numerators for one fixed defect locator and
one exact petal support with `h>d`, or a class `(RC2)` exceeding `(RC3)`.
