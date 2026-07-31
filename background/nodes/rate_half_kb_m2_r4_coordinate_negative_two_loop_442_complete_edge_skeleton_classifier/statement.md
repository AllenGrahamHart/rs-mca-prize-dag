# KoalaBear m2 r4 coordinate negative two-loop 442 complete-edge skeleton classifier

- **status:** PROVED
- **scope:** every negative-parity coordinate packet in the two-loop
  `(4,4,2)` skeleton `(1,1,0;1,1,1)`
- **dependencies:**
  `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature`,
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`, and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_antipodal_label_classifier`
- **consumer:** `rate_half_band_closure`

Name the `J` pairs `A,B,C`, with common-`K` degrees `(4,4,2)` and loops at
`A,B`.  Name the three `I` pairs `D,E,F`.  Every complete packet has no
outside antipodal `I-I` edge.  Its two colored `I-J` orbits both meet the
deficient pair `C`, but they attach to two distinct `I` pairs.  Up to
permuting `D,E,F`, the exact outside edge-type multiset is

```text
C-D, C-E, D-E, D-F(+), D-F(-), E-F(+), E-F(-).    (KB44S-1)
```

Equivalently the colored attachment and internal multiplicities are

```text
(r_D,r_E,r_F)=(1,1,0),
(m_DE,m_DF,m_EF)=(1,2,2).                         (KB44S-2)
```

Exactly one of the five internal signed edge types in `(KB44S-1)` lies over
`eta`.  The other four internal records and both colored `C-I` records lie
over `L^c`.

This theorem does not assign endpoint or quotient labels, choose the `eta`
type, impose the outside product involution or full interpolation, solve the
q/resultant equations, delete the skeleton, close the coordinate
orientation, move an owner/payment, close a row, or prove either Prize
result.

## Falsifier

An actual `(4,4,2)` packet with an outside loop, both colored records
attached to one `I` pair, or an outside skeleton not isomorphic to
`(KB44S-1)`.
