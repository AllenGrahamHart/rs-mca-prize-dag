# KoalaBear m2 r4 diagonal c2 (1,1,2) saturated-defect classifier

- **status:** PROVED
- **scope:** the saturated cases of the diagonal `(a,b,c)=(1,1,2)` row
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_facet_mixing_obstruction`,
  `rate_half_kb_m2_v4_outer_recurrence_router`, and
  `rate_half_kb_m2_r4_diagonal_source_subfield_dichotomy`
- **consumer:** `rate_half_band_closure`

Assume either `L=I` or `tau(eta) in K`, so `(KBDM-9)` applies. Put
`q=P_(J_1)`. The square quartic and its reciprocal partner give two distinct
star vertices `q` and `tau(q)` of weight exactly two. They consume two of
the three complete-source defect units:

```text
weight(q)=weight(tau(q))=2,       Delta_remaining<=1. (KBS2-1)
```

The four stars over the internal `K` orbit are reduced `J_0-J_0` edges.
The four stars in the two common-`K` quartics transported to `L^c` are all
reduced `J_0-J_1` edges; each label of `J_1` occurs in exactly two of them.
No `J_1-J_1` factor is possible, because it would be a third occurrence of
`q` and force total defect at least four. Thus

```text
four pure J_0 edges + four mixed J_0-J_1 edges,
collision_defect(pure)+collision_defect(mixed)<=1. (KBS2-2)
```

In particular, at most one of these eight edge vertices is repeated, and no
vertex has weight three. The possible `J_0` incidence profiles are exactly

```text
(2,2,4,4),       (2,3,3,4),       (3,3,3,3).      (KBS2-3)
```

There are exactly `1,560` labeled pairs of pure/mixed edge multisets obeying
`(KBS2-2)--(KBS2-3)`, in `123` orbits under the order-16 relabeling group
that preserves the two `tau` pairs of `J_0` and may swap the labels of
`J_1`.

In the source-line branch, individual-star equivariance sharpens the list.
The four pure edges are a union of two `tau`-edge orbits. A repeated mixed
edge would force its transported `I-J` partner to repeat as well, spending
two remaining defect units, so all four mixed edges are distinct. Exactly

```text
96 labeled packets in 12 matching-preserving orbits               (KBS2-4)
```

remain. Their four transported partners are the four `I-J` stars of the
universal category census.

These are combinatorially admissible packets, not realized components. The
theorem does not delete a saturated packet, the exceptional unsaturated
orbit `(KBDM-10)`, either source-subfield branch, the `(1,1,2)` row, the
diagonal orientation, an owner, payment, row, or Prize result.

## Falsifier

A saturated actual packet violating `(KBS2-1)--(KBS2-3)`; a source-line
packet outside `(KBS2-4)`; or an independently replayed packet count other
than `1560/123` and `96/12` at the printed scopes.
