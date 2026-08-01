# KoalaBear m2 r4 coordinate negative one-loop 433 complete-edge skeleton classifier

- **status:** PROVED
- **scope:** every complete negative one-loop `(4,3,3)` packet
- **dependencies:**
  `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature`,
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`, and
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate`
- **consumer:** `rate_half_band_closure`

Name the common target pairs `A,B,C`, with degrees `(4,3,3)` and the loop
at `A`.  Name the outside pairs `D,E,F`.  The two colored outside records
are one `B-I` and one `C-I` orbit.  Up to permuting `D,E,F`, every complete
packet has exactly one of

```text
S0: r=(0,1,1), l=(0,0,0), m=(2,2,1);
S1: r=(0,1,1), l=(1,0,0), m=(1,1,2);
S2: r=(2,0,0), l=(0,1,0), m=(0,2,2).              (KB433S-1)
```

Here `r` counts colored incidences, `l` outside loops, and
`m=(m_DE,m_DF,m_EF)`.  There are twelve labeled solutions, in permutation
orbits of sizes `3,3,6`.

For target representatives `A=1,B=b,C=c`, sign gauges give the exact
outside product forms

```text
S0: {alpha bD,beta cE,gamma DE,+/-DF,+/-EF};
S1: {alpha bE,beta cF,-D^2,gamma DE,delta DF,+/-EF};
S2: {alpha bD,beta cD,-E^2,+/-DF,+/-EF}.           (KB433S-2)
```

All displayed Greek letters are independent signs.  One of the five
internal records is `eta`; the other four internal and both colored records
lie over `L^c`.

This theorem does not impose the product involution, choose the `eta` type,
assign quotient labels, impose q or interpolation, delete a common cell,
close the coordinate orientation, close a Prize row, or prove either Prize
result.

## Falsifier

A complete one-loop 433 packet with a skeleton outside `(KB433S-1)`, a
missing sign form in `(KB433S-2)`, or a labeled degree solution outside the
twelve-cell census.
