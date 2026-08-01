# KoalaBear m2 r4 positive coordinate three-loop complete-edge skeleton classifier

- **status:** PROVED
- **scope:** every positive coordinate packet in either three-loop common
  profile `(4,4,2)` or `(4,3,3)`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_loop_ramification_gate` and
  `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature`
- **consumer:** `rate_half_band_closure`

The three common loops occupy both ramified quotient values and the unique
root of `B_1`.  Hence no outside quotient fiber can carry an antipodal edge.

Let `D,E,F` be the three outside signed target pairs.  Let `r_i` count the
two colored edge orbits incident to pair `i`, and let
`m=(m_DE,m_DF,m_EF)` count the five internal edge orbits.  Up to permuting
`D,E,F`, every complete packet has the unique record

```text
r=(0,1,1),       m=(2,2,1).                       (KBP3S-1)
```

Thus the two colored records attach to distinct outside pairs.  The
uncolored pair has both signed cross types to each colored pair, and the two
colored pairs have one signed cross type between them.  There are exactly
three labeled records, according to the choice of uncolored pair.

For profile `(4,4,2)`, both colored records attach the deficient common
pair to the two colored outside pairs.  For profile `(4,3,3)`, the two
distinct deficient common pairs supply one colored record each, in either
assignment.  All associated signs remain explicit.

This theorem does not impose the positive rank-five product map, classify
the common q weld, delete either three-loop profile, close positive parity,
close a Prize row, or prove either Prize result.

## Falsifier

An outside loop, a complete three-loop packet with colored incidences or
internal multiplicities different from `(KBP3S-1)`, or a valid concentrated
colored record with multiplicities `(3,1,1)`.
