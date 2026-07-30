# KoalaBear m2 r2 dihedral degree-two source-star exclusion

- **status:** PROVED
- **scope:** the `n=2` factor case inside the residual actual
  `(m,r,delta)=(2,2,4)` row
- **dependencies:**
  `rate_half_kb_m2_r2_dihedral_degree5_source_star_exclusion` and the
  complete-source quartic defect gate
- **consumer:** `rate_half_band_closure`

At any one of the three generic order-five poles of the outer map `G`, the
degree-two dihedral quotient has two `Y` values and two `Z` values. The
incidence on the outer normalization is the complete bipartite graph
`K_(2,2)`: both `Z` values see the same pair of `Y` values.

Each `Y` value has two unramified endpoint source labels. For either `Z`
value, its two endpoint lifts and their degree-two complete-source pullbacks
contribute four source-star units. Birationality of the source normalization,
full V4 symmetry, and the diagonal lift force every star to be a cross edge
between the same two endpoint source pairs. Both `Z` values therefore put
eight units on only four possible star vertices.

For nonnegative integer weights with sum eight on four vertices,

```text
sum_v binom(w_v,2) >= 4,
```

with equality only at weights `(2,2,2,2)`. The complete-source defect budget
is at most three. Thus the `n=2` factor case is empty. Together with the
degree-five exclusion, the full-V4 row is reduced to

```text
n in {3,6}.                                         (KBM2D-1)
```

Neither remaining degree is deleted. No other `m=2` type, owner, payment,
`u=2`, endpoint, adjacent certificate, or Prize row is proved.

## Falsifier

A generic `D_2` quotient fiber whose two reflection partitions do not have
`K_(2,2)` incidence, a source-normalization fiber that does not select one
label from each `Y` pair, or an eight-unit/four-vertex defect below four.
