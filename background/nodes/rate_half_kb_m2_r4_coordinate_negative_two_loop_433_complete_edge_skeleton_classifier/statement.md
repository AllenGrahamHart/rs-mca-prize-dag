# KoalaBear m2 r4 coordinate negative two-loop 433 complete-edge skeleton classifier

- **status:** PROVED
- **scope:** every negative-parity coordinate packet in the two-loop
  `(4,3,3)` skeleton `(1,0,1;2,0,1)`
- **dependencies:**
  `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature`,
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`, and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_antipodal_label_atlas`
- **consumer:** `rate_half_band_closure`

Name the three antipodal `J` pairs `A,B,C`, with common-`K` degrees
`(4,3,3)` and loops at `A,C`.  Name the three antipodal `I` pairs `D,E,F`.
Every complete packet has exactly two outside `I-J` edge orbits and five
outside `I-I` edge orbits.

No outside `I-I` orbit is antipodal.  Moreover the two `I-J` orbits attach
to two distinct `I` pairs.  After permuting `D,E,F`, and assigning the two
deficient `J` pairs, the exact outside edge-type multiset is

```text
B-D, C-E, D-E, D-F(+), D-F(-), E-F(+), E-F(-).    (KB43S-1)
```

Here a single cross type such as `B-D` or `D-E` retains either signed
matching, while `(+)` and `(-)` mean both possible signed products occur.
Equivalently, if `r_i` is the number of `I-J` orbits incident to the `i`-th
`I` pair and `m_ij` counts internal cross-pair orbits, then, up to
permutation,

```text
(r_D,r_E,r_F)=(1,1,0),
(m_DE,m_DF,m_EF)=(1,2,2).                         (KB43S-2)
```

The `eta` record is one of the five `I-I` types in `(KB43S-1)`; the other
four lie in `L^c`, together with the two colored `I-J` types.  Thus complete
source-facet assembly has only the following location split:

```text
choose one of the five internal signed edge types for eta;
place the other six types over L^c, with B-D and C-E colored. (KB43S-3)
```

This theorem does not assign the actual `I` labels, pair edge types with
specific quotient labels, impose the outside-product involution or full
Mobius interpolation, solve the q/resultant equations, delete the skeleton,
close the coordinate orientation, move an owner/payment, close a row, or
prove either Prize result.

## Falsifier

An actual `(4,3,3)` packet with an outside loop, both colored orbits attached
to one `I` pair, or an outside edge skeleton not isomorphic to `(KB43S-1)`.
