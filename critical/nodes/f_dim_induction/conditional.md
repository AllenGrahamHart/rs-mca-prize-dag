# f_dim_induction conditional proof

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: CONDITIONAL]
- **closure:** proof from predicate nodes

## Predicate nodes

- `f_dim2_skeleton`
- `f_dual_distance_frame`
- `f_spread_moment_count`
- `f_sparse_descent_step`
- `f_many_sparse_structure`
- `f_descent_termination`

## Claim

Conditional on these predicates, the divisor-depth induction proves the
gcd-trivial `r`-flat case from the dimension-2 base: each excess dimension buys
one unit of shared-divisor depth, matching the `j - dim(P)` threshold shape.

## Proof

The base case is `f_dim2_skeleton`: gcd-trivial planes are controlled by the
pair-counting bound, and twin coincidences are tangent-paid by the gcd
reduction.

For higher dimension, use `f_dual_distance_frame` to translate trace
degeneracies into low-weight words in the flat's dual evaluation code.

If the dual distance is larger than the current dimension, the flat is
dually-spread. Then `f_spread_moment_count` applies the `r`-wise moment count,
giving the spread branch of the induction.

If a sparse dual word exists, `f_sparse_descent_step` gives the local
divisor-depth move: on the all-roots subflat the degree drops by `w` while the
dimension drops by at most `w-1`, so divisor depth increases by at least one.
On the complementary branch, the sparse support loses enough root budget to
continue the descent.

If sparse words proliferate, `f_many_sparse_structure` supplies the structural
split: the flat is tangent/pullback/dihedral-paid or remains descent-reducible.
Thus coincidences do not create an unpaid high-dimensional branch.

Finally, `f_descent_termination` guarantees that iterating these descent moves
has only polynomially many memoized support-lattice states, with spread/moment
leaf estimates. Therefore the induction over dimension closes conditionally on
the listed predicates.
