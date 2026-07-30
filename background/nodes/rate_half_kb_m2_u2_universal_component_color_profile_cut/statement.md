# KoalaBear m2 u2 universal component-color profile cut

- **status:** PROVED
- **scope:** every actual residual `Q=6,s=6,u=2` source component
- **dependencies:**
  `rate_half_kb_m2_u2_universal_source_facet_census` and Corollary 9.28
  of the pinned equality-wall source theorem
- **consumer:** `rate_half_band_closure`

Let `J=I^c`, let `K` be the common five-set, and let `d_j` be the
incidence degree of `j in J` among the ten `J-J` component stars over the
five complete `K` fibers. Put

```text
c_j=4-d_j.
```

The four incidences outside `K` are exactly the four pole-graph edges
colored by the degree-two component. Hence `c_j` is the colored degree of
the left pole-graph vertex `j`. Since the pole graph is two-regular,

```text
0<=c_j<=2,       sum_(j in J)c_j=4.                (KBUC-1)
```

Consequently the first two profiles in the universal five-profile census
are impossible. Up to permutation of `J`, the exact surviving list is

```text
(2,2,4,4,4,4),
(2,3,3,4,4,4),
(3,3,3,3,4,4).                                    (KBUC-2)
```

In particular every `J` label occurs at least twice over `K`. Coordinate
involution symmetry separately removes the middle profile; no such removal
is asserted for the diagonal or trivial-stabilizer branch.

This theorem deletes two source-facet profiles, not a component,
stabilizer type, owner, payment, row, or Prize result.

## Falsifier

An actual residual degree-two component for which an outside-`K` `J`
incidence does not correspond to its uniquely colored pole-graph edge, a
left colored degree exceeds two, or a `K`-fiber degree profile lies outside
`(KBUC-2)`.
