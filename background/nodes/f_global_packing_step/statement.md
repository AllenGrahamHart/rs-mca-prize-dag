# Conjecture-F global packing step

- **status:** TARGET
- **consumer:** `f_dim_induction`

Work in every typed flat descriptor emitted by
`f_prize_consumer_flat_scope`. Apply the proved spread/rank-defect dichotomy,
strict sparse descent, paid tangent/quotient owners, and memoized
support-lattice termination. At every spread leaf the exact local estimate is

```text
#leaf <= binom(n_leaf,r_leaf)/binom(j_leaf,r_leaf).
```

Prove that the complete first-owner sum over all unpaid spread leaves is at
most

```text
n^B_F
```

for one explicit absolute exponent `B_F`, independent of the initial flat
dimension and of the descent path. The theorem must absorb the `n^r`-type
numerators; a polynomial number of states does not suffice when each state
has a dimension-dependent exponent.

The scope compiler must prove the quantitative relation between `r` and `j`
needed by this sum. Merely assuming `r<j` is insufficient. The full-space
case `r=j` is a known counterexample to the unqualified formulation.

## Falsifier

A sequence of accepted consumer descriptors and valid first-owner descent
leaves for which the exact summed spread bound exceeds `n^B` for every fixed
`B`, or a consumer descriptor that the scope compiler accepted without a
proved quantitative packing regime.

## Round-23b note (2026-08-07, coordinator-applied): METHOD-wall membership

The round-23b adjudication (mf_wall_adversary) identifies this
leaf's failure — "the theorem must absorb the n^r-type numerators;
a polynomial number of states does not suffice when each state has
a dimension-dependent exponent" — as the SAME METHOD wall as the
two FPC5 rate-half reds (identical anticode formula
binom(n,r)/binom(j,r); identical growing-dimension failure), and
as the open d = Theta(n) regime of the PROVED
l1_rootfree_rational_q_projective_packing. A dimension-uniform
split-locator max-to-mean theorem would serve all of them.
