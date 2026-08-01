# KoalaBear m2 r4 coordinate negative one-loop 442 S1 common-sign product transport

- **status:** PROVED
- **scope:** all four common root-sign rows, outside skeleton `S1`, and the
  live sextic common orbit `[9,10,12,13]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_loop_deployed_product_exclusion`,
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_sextic_mate_coordinate_compiler`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier`
- **consumer:** `rate_half_band_closure`

Let `g_0,g_1` be the two deployed irreducible cubic factors of the common
sextic and put `K_j=F_p[B]/(g_j)`.  For every common root-sign row
`(epsilon_1,epsilon_2)`, the exact component map sending `b` to `B` sends
the reconstructed `c` and forced mate `m` to the same elements of `K_j`.
In coefficient triples these are

```text
j=0:
c=(165644906,1305134575,1484956850),
m=(1244418779,141852127,1677606574);

j=1:
c=(1190295236,1600338149,1091152148),
m=(368587486,183733761,1744133513).       (KB41T-1)
```

The product involution has coefficients

```text
Alpha=-b(c+b^2),
Beta=b^2(c-b^2-2bc),
Gamma=c+2b-b^2.                            (KB41T-2)
```

Consequently its binary-sextic action and every forced-record `S1`
residual form depend on the common sign row only through the data in
`(KB41T-1)`, which are row-independent.  The forced-loop extensions are
also identical because they are defined by `theta^2=-m`; `-m` is a
nonsquare in both components in every row.

Thus the ten deployed product ideals in each common sign row are identical,
under the component maps, to the ten already deleted in row `(1,1)`.  All
forty `S1` product cells are empty.  The accepted four-row invariant-cell
frontier falls from 70 to 40, consisting of the six `S0` and four `S2`
cells in each row.

This theorem does not delete an `S0` or `S2` cell, transport outside source
roots or `q` values, impose full interpolation, close the coordinate
orientation or a row, or prove either Prize result.

## Falsifier

A sign row/component in which `c` or `m` differs from `(KB41T-1)`, or an
`S1` product equation involving common-row data other than `b,c,m`.
