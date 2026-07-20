# Claim contract - L1 fixed-support defect Johnson bound

## Inputs

- one maximal-sunflower source chart with an ordered `(k-1)`-point core;
- one exact labelled petal-support pattern disjoint from that core;
- exact split defect locators and saturated numerator pairs;
- the L1 list-threshold and petal-polarity accounting.

## Output

Distinct defect sets intersect in at most `r_J=2d-h`. Every cell with
`d^2>(k-1)r_J` has the explicit Johnson bound `(JB4)`, and all such cells are
polynomial per source chart at fixed petal polarity.

## Consumer rule

Consumers may restrict a bounded-polarity per-chart counterfamily to
`(k-1)(e-1)>=d^2`. They must retain the non-intrinsic first-match chart
multiplier and the growing-polarity branch.

## Falsifier

Two distinct exact saturated pairs with defect intersection greater than
`2d-h`, or a positive-denominator fixed-support family violating `(JB4)`.
