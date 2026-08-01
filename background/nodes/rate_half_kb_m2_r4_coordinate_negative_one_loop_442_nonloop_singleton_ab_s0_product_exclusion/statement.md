# KoalaBear m2 r4 coordinate negative one-loop 442 AB-singleton S0 product exclusion

- **status:** PROVED
- **scope:** all `S0` outside product cells over the finite common orbit
  `[3,6]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_ab_s2_product_exclusion`,
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_ab_product_involution_compiler`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier`
- **consumer:** `rate_half_band_closure`

For both deployed `b` rows and both `S0` parities, remove the forced mate
and impose residual binary-sextic invariance.  The three canonical
forced-record types give

```text
forced CE/CF:  raw unit ideal after 29 S-pairs;
forced EF:     completed basis contains s^2 after 190 S-pairs;
forced DE/DF:  completed basis contains s after 406 S-pairs. (KB41BS0-1)
```

The three systems have respectively `11`, `12`, and `14` monomials
per equation.  In the latter two cells `s` is a nonzero outside
representative, so they are guarded deletions.  Replacing `c` by `-c`
and simultaneously changing the signs of the two colored outside
representatives permutes each residual product multiset and preserves its
parity.  Thus every `S0` product cell over all common packets is empty.

Together with the preceding `S2` exclusion, only `S1` remains at product
level for cells `[3,6]`.  This theorem does not impose outside q equations
or interpolation, classify `[4,5,7,8]`, close the coordinate orientation
or a row, or prove either Prize result.

## Falsifier

A guarded `S0` product realization in any row/parity, a missing
forced-record type, failure of a printed basis certificate, or failure of
the `c`-sign transport.
