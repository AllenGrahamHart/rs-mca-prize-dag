# KoalaBear m2 r4 coordinate negative one-loop 442 complete-edge skeleton classifier

- **status:** PROVED
- **scope:** every complete negative one-loop `(4,4,2)` packet
- **dependencies:**
  `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature`,
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`, and
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate`
- **consumer:** `rate_half_band_closure`

Name the three outside `I` pairs `D,E,F`.  Let `r_D,r_E,r_F` count the two
colored `C-I` edge orbits, `l_D,l_E,l_F` the outside loops, and
`m_DE,m_DF,m_EF` the other five internal edge orbits.  Up to permuting
`D,E,F`, every complete packet has exactly one of

```text
S0: r=(0,1,1), l=(0,0,0), m=(2,2,1);
S1: r=(0,1,1), l=(1,0,0), m=(1,1,2);
S2: r=(2,0,0), l=(0,1,0), m=(0,2,2).             (KB41S-1)
```

Thus there is one loop-free split-colored skeleton, one split-colored
skeleton whose unique loop is on the uncolored pair, and one
concentrated-colored skeleton whose unique loop is on another pair.
Multiplicity two uses both signed products.  Exactly one internal orbit is
the `eta` record.

This theorem does not choose the `eta` type, impose products, q equations,
or full interpolation, delete a skeleton, classify another common matching
orbit, handle one-loop 433 or zero-loop, close the coordinate orientation,
move an owner/payment, close a row, or prove either Prize result.

## Falsifier

A complete one-loop 442 packet with an outside graph outside `(KB41S-1)`,
two outside loops, a different colored attachment pattern, or an internal
multiplicity above two.
