# KoalaBear m2 r4 positive three-loop signed outside-Vieta atlas

- **status:** PROVED
- **scope:** the seven outside edge orbits of every positive coordinate
  three-loop packet
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_three_loop_common_placement_atlas`,
  `rate_half_kb_m2_r4_coordinate_positive_three_loop_complete_edge_skeleton_classifier`,
  and `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`
- **consumer:** `rate_half_band_closure`

Let `d` be the uncolored outside signed pair and `e,f` the two colored
outside pairs.  Target-sign gauge reduces the seven outside edges to

```text
colored:  a e, a' f;
internal: de,-de, df,-df, sigma ef,       sigma in {+1,-1}. (KBP3V-1)
```

Here products are printed; the corresponding squared sum for signed
representatives `r,t` and product `p` is

```text
s^2=r^2+t^2+2p.                                  (KBP3V-2)
```

For 442, `a=a'` is its low-degree common pair.  For 433, `a,a'` are its
two low-degree common pairs; their assignment to `e,f` is unique modulo
the simultaneous equal-degree swaps.  The three raw signs on the two
colored edges and the single `ef` edge have exactly two gauge orbits,
distinguished by their product `sigma`.  Together with the four common
placements, this gives exactly eight signed Vieta lanes.

For one edge record `(p,s^2)`, let `D=A_2`, `E=A_0` be reconstructed by the
common kernel and let `w` be its outside quotient label.  Its square-root-
free equations are

```text
P_p(w)=E(w)-pD(w)=0,
Q_p,s(w)=beta^2 w(w-1)^2-s^2D(w)^2=0.             (KBP3V-3)
```

They have degrees at most two and four.  Under

```text
beta D(w) w(w-1)(w-x^2)(w-y^2) != 0,             (KBP3V-4)
```

`(KBP3V-3)` is equivalent to the original product and sum rows for one of
the two source lifts above `w`.  The seven-label system additionally
requires pairwise distinct `w_i`.  Equivalently, it is the ideal generated
by the fourteen equations `(KBP3V-3)`, saturated by all factors in
`(KBP3V-4)`, all `w_i-w_j`, and the target-pair collision guards.  Each
edge also supplies the necessary scalar cut

```text
Res_w(P_p,Q_p,s)=0,                               (KBP3V-5)
```

but the resultant alone does not enforce the saturation.

This theorem does not prove any of the eight lanes empty, enforce the
remaining source-facet/outer-factor conditions, close positive parity, or
prove either Prize result.

## Falsifier

A third sign orbit, a ninth signed lane, an actual outside edge failing
`(KBP3V-1)--(KBP3V-4)`, or a saturated solution which cannot be lifted to
the seven original positive Vieta rows.
