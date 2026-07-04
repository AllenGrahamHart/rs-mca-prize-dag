# f_many_sparse_structure conditional proof

## Predicate nodes

- `f_dual_distance_frame`
- `f_sparse_descent_step`
- `dihedral_quotient_stratum`
- `f_sparse_rank_split`

## Claim

Every many-sparse flat is paid by the enlarged taxonomy
(multiplicative/projective pullback, dihedral/Chebyshev quotient, tangent) or
is descent-reducible. In particular, no unpaid many-sparse branch remains once
the predicate nodes hold.

## Proof

The predicate `f_dual_distance_frame` translates many sparse trace
dependencies into low-weight words of the flat's dual evaluation code. This
puts every obstruction in sparse-dual language and gives the closure rule for a
minimal support.

Apply the predicate `f_sparse_rank_split` to the span of those sparse dual
words. In the bounded-rank branch, quotienting by the sparse span reduces to
the fixed-dimensional lattice/strip regime recorded in that predicate. In the
growing-rank branch, the split is by sparse-word weight. Abundant weight-2
supports are handled by the inverse theorem internal to the split, yielding a
pullback stratum; higher-weight accumulation is transported to the Face-4
configuration machinery rather than creating a new F-primitive class.

For a minimal sparse word of weight `w`, the predicate `f_sparse_descent_step`
gives the divisor-depth descent: the all-roots subflat drops degree by `w` and
dimension by at most `w-1`, while the complement branch has strictly less root
budget on the support. Thus any branch not immediately paid is
descent-reducible.

The predicate `dihedral_quotient_stratum` supplies the missing quotient class
exposed by reciprocal flats: `X^e g(X^M + alpha X^{-M})`. This absorbs the
Chebyshev/dihedral branch that is not contained in the multiplicative pullback
taxonomy.

The four cases exhaust the sparse-dual possibilities: bounded sparse rank,
growing rank with weight-2 abundance, growing rank with higher-weight
accumulation, and the explicit dihedral quotient correction. Therefore the
many-sparse structure statement follows conditionally from its predicate
nodes.
