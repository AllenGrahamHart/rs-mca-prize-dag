# conditional: e22_challenger_staircase_pricing

## Predicate nodes

- `e22_staircase_parametrization`
- `e22_staircase_injectivity`
- `e22_staircase_arithmetic_pricing`

## Claim

Conditional on the three predicate nodes, the structured E15-successor
challenger column is exact and usable by `worst_word_challenger_pricing`.

## Proof

The pricing obligation has three logically separate parts.

First, `e22_staircase_parametrization` identifies every mixed/full-petal
challenger with a quotient-coset staircase datum in the current sunflower
notation. This supplies coverage of the structured class left after
`e22_two_class_exhaustion`.

Second, `e22_staircase_injectivity` proves that the parameter map has exactly
the declared equivalences and no hidden overlap with planted words. Therefore
the parameter count is the codeword count, not merely an upper or lower bound.

Third, `e22_staircase_arithmetic_pricing` evaluates that exact column in the
list-side integer comparison alongside `planted_count`.

Together these predicates give the explicit formula, no-overlap proof, and
row-by-row comparison required by this node's statement.
