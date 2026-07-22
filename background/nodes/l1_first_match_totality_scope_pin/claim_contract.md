# Claim contract - L1 first-match totality scope pin

## Inputs

- a finite set of distinct image-fiber contributors;
- at least one finite carrying chart record for every contributor;
- a total order on chart keys.

## Output

A canonical, disjoint, exhaustive first-owner partition and the exact
cardinality sum `(FT2)`. Any valid owner-cell bounds may be summed as in
`(FT3)` without cross-chart double counting.

## Consumer rule

Consumers may retire "missing first-match coverage" as an independent L1
obligation. They must retain the polynomial **aggregate payment** over all
realized internal non-intrinsic owner cells not covered by
`l1_general_first_layout_domination`. They may not infer a polynomial number
of keys, a per-cell bound, or a polynomial total from partition totality alone.

## Falsifier

A contributor with no carrying chart in the declared chart universe,
two different first owners for one contributor under a total order, overlap
between distinct owner cells, or failure of their union to equal the input
image-contributor set.
