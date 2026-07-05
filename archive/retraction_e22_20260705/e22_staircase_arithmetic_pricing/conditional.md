# conditional: e22_staircase_arithmetic_pricing

## Predicate nodes

- `e22_staircase_parametrization`
- `e22_staircase_injectivity`
- `dyadic_profile_evaluation`

## Claim

Conditional on the E22 formula and multiplicity predicates, the arithmetic
part of the staircase-pricing leaf is already an exact integer computation.

## Proof

The parametrization predicate identifies every structured E22 challenger with
the quotient-coset staircase form. The injectivity predicate says this
parametrization has exactly the declared quotient equivalences and no hidden
overlap with planted sunflower words. Therefore the challenger contribution is
not an unknown list family: it is the explicit quotient staircase column.

For dyadic official rows, `dyadic_profile_evaluation` proves that this
quotient staircase column is the finite divisor sum

```text
Q_H = sum_{M | n, M > t} binom(n/M - 1, floor(A/M)).
```

It also verifies the deciding-scale values and the first-scale dominance used
by the row comparison, all with exact integers. The planted column has its
usual sunflower count from the same local construction; adding this integer
column to the exact staircase column gives the planted-plus-challenger count
with no floating decision.

Thus, once the formula and injectivity predicates are supplied, this node
contains no further mathematical search: it is the exact arithmetic consumer
of the staircase column.
