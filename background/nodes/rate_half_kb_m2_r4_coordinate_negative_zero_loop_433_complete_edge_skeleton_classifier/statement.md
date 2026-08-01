# KoalaBear m2 r4 coordinate negative zero-loop 433 complete-edge skeleton classifier

- **status:** PROVED
- **scope:** every complete negative zero-loop `(4,3,3)` packet
- **dependencies:**
  `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature`,
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`, and
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate`
- **consumer:** `rate_half_band_closure`

Name the common target pairs `A,B,C`, with degrees `(4,3,3)` and no loop.
Name the outside pairs `D,E,F`.  Let `r_i` count colored incidences at the
outside pair `i`, let `l_i` count outside loops, and put
`m=(m_DE,m_DF,m_EF)`.  Up to permuting `D,E,F`, every complete packet has
exactly one of

```text
Z0: r=(0,0,2), l=(0,1,0), m=(2,2,0);
Z1: r=(0,0,2), l=(1,1,0), m=(1,1,1);
Z2: r=(0,1,1), l=(0,0,0), m=(2,2,1);
Z3: r=(0,1,1), l=(1,0,0), m=(1,1,2);
Z4: r=(0,1,1), l=(1,0,1), m=(2,0,1).              (KBZ433S-1)
```

There are exactly 21 labeled solutions, in permutation orbits of sizes
`6,3,3,3,6` in the displayed order.  These records compile all signed
outside product forms without further graph choices: a loop contributes
`-D_i^2`, multiplicity two contributes both signed cross-products,
multiplicity one chooses either sign, and the two colored records attach
the deficient common pairs `B,C` according to `r`.

Exactly one of the five internal records lies over `eta`; the other four
internal and both colored records lie over `L^c`.

This theorem does not impose the product involution, assign quotient labels,
impose outside q or interpolation, delete a common cell, close the coordinate
orientation, close a Prize row, or prove either Prize result.

## Falsifier

A complete zero-loop 433 packet with a skeleton outside `(KBZ433S-1)`, or a
labeled degree solution outside the 21-cell census.
