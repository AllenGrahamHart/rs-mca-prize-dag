# conditional: e22_staircase_injectivity

## Predicate nodes

- `e22_fixed_scale_staircase_injectivity`
- `e22_cross_scale_planted_degeneracy_control`

## Claim

Conditional on cross-scale and planted-degeneracy control, the E22 staircase
parametrization is injective up to the declared equivalences and has no hidden
overlap with planted words.

## Proof

The fixed-scale predicate proves that once the quotient modulus `M` is fixed,
the locator `L_B(X)G(X^M)` determines the tail `B` and the selected quotient
fibers uniquely. Thus there are no unpriced multiplicities inside a single
staircase scale.

The remaining predicate handles exactly the cases not covered by fixed-scale
root-set recovery: duplicate representations across different quotient
moduli, declared quotient-equivalence degeneracies, and possible overlap with
the planted core locator.

Together these predicates imply that equality of two generated codewords
forces equality of their staircase parameters modulo the declared
equivalences, and that no nondegenerate staircase parameter set yields a
planted sunflower codeword.
