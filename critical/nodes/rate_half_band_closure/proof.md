# rate_half_band_closure proof status

No proof is currently known in this node folder.

The former AQB proof route is refuted: averaging is a convex combination of
single-box fiber counts and cannot create the required box-sharing gain.

The former P6 dihedral-sibling proof route is also refuted.  The local refutation
is recorded in `nodes/dihedral_sibling_window_certificate/proof.md`: the claimed
packet size is not a Chebyshev top-degree drop, true Dickson fibers are too
small in the first band, and the endpoint fixed-point sibling still fails the
degree audit.

The live full-determination target remains: cover the rate-`1/2` band
`2^33 < sigma <= 8,592,912,738` by a new priced mechanism.  A bracket-grade
obstruction for some band radius is a separate partial-result outcome, not a
proof of this node.

---

## WAVE-9 PIN BODY (proof addendum, 2026-07-17)


## Retraction of the fixed edge

The former target asserted safety at agreement

```text
k+8,592,912,738+1.
```

It is false. The dependency `rate_half_cyclic_rotated_prefix_floor` is valid
for every residual prefix size `1<=s<c`, and its list lower bound is
independent of `s`. Taking its maximal legal prefix `s=c-1`, with
`c=2^22` and `d=2048`, gives the same list at excess

```text
sigma_0=dc+c-1=8,594,128,895.
```

The quantitative conversion in
`rate_half_cyclic_simple_pole_mca_floor` then proves

```text
epsilon_ca,epsilon_mca>2^-83>2^-128
```

at `sigma_0` and, by radius monotonicity, at every positive excess below it.
The old proposed safe point lies strictly inside that interval.

This is not a numerical falsifier or an ordinary-list surrogate. It is the
same exact simple-pole slope count already proved in the dependency, with the
residual-prefix parameter used at its full stated range.

## Proved progress retained

The generalized pole theorem gives the uniform lower bracket

```text
a_RH(q)>=k+8,594,128,896
```

for every admissible field. The list/interleaved-list branch remains separate
and retains its proved cyclic lower floor. No list-safe or MCA-safe claim is
inferred from that lower floor.

The exact sparsification theorem
`rate_half_mca_sparse_layer_reduction` further reduces an upper certificate
at any later candidate to the conjunction of a far-pair CA bound and a sparse
mutual-layer bound. This identity is lossless; it does not estimate either
term.

The proved `rate_half_sparse_pinning_rigidity` theorem resolves the first
structural layer of the sparse term. Tangencies are at most `r` and are paid
whenever `q>=2^168`. Every remaining sparse slope is pinned to one nonzero
ambiguity polynomial and must obey the shared root, cofactor-degree, and
active-match budget printed in that node. Counting those coupled objects is
still open.

## Remaining proof

The node remains TARGET. One must locate a field-dependent agreement
`a_RH(q)` at or beyond the proved bracket, prove both terms of the exact safe
split are at most `floor(q/2^128)`, and prove the immediately preceding
agreement unsafe. The generic deep theorem and imported half-distance pincer
do not reach this near-capacity region.
