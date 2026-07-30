# KoalaBear m2 r4 diagonal c2 (2,0,2) defect exclusion

- **status:** PROVED
- **scope:** every actual diagonal `(a,b,c)=(2,0,2)` component
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_facet_mixing_obstruction` and
  `rate_half_kb_m2_v4_outer_recurrence_router`
- **consumer:** `rate_half_band_closure`

The `(2,0,2)` crossing-orbit row is empty.

The forced quartic in `(KBDM-8)` is `P_(J_1)^2`. Its two reduced component
stars are therefore the same `J_1-J_1` edge and contribute a star vertex of
weight at least two. Whole-fiber diagonal transport makes the paired
quartic the square on `tau(J_1) subset I`; its two reduced stars give a
second, distinct weight-at-least-two vertex. These cost defect at least two.

The four labels in `K_0=K intersect tau(K)` contribute eight further reduced
stars, all edges on the four-label set `J_0`. They occupy at most six
vertices and cost defect at least two. Hence every proposed packet has

```text
Delta_star=sum_v binom(weight(v),2) >= 2+2=4,       (KBD2-1)
```

contradicting the complete-source defect budget `Delta_star<=3`.

Thus

```text
(a,b,c)!=(2,0,2)                                  (KBD2-2)
```

for every actual diagonal component, in both source-subfield branches and
with or without source ramification. Four orbit rows remain. This theorem
does not delete `(1,1,2)`, either `c=4` row, the surviving `c=6` row, the
diagonal orientation, an owner, payment, row, or Prize result.

## Falsifier

An actual diagonal `(2,0,2)` component; a forced square fiber whose two
reduced factors are not the printed edge; or eight reduced edges on four
labels with collision defect below two.
