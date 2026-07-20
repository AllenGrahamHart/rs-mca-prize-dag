# Claim contract - L1 background-quotient Johnson bound

## Inputs

- one maximal-sunflower source chart, defect degree, and exact petal support;
- the degree-`<k` codeword model and L1 list threshold;
- the generated-field, petal-polarity, and lower-cutoff bounds.

## Output

The fixed cell injects into a degree-`c` RS list on the `b`-point background
with agreement at least `u`. Positive Johnson denominator gives `(BQ3)`, and
all such cells are polynomial per chart at fixed petal polarity.

## Consumer rule

Consumers may impose `(BQ5)` in addition to `(BQ6)` on the bounded-polarity
tail. Equality in `(BQ5)` must be retained.

## Falsifier

A positive-denominator derived-background list exceeding `(BQ3)`, or failure
of the exact transformation `(1)--(3)`.
