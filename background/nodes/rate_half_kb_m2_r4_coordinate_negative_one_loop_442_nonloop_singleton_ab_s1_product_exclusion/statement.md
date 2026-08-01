# KoalaBear m2 r4 coordinate negative one-loop 442 AB-singleton S1 product exclusion

- **status:** PROVED
- **scope:** all `S1` outside product cells over the finite common orbit
  `[3,6]`, and consequently its complete outside-product frontier
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_ab_s0_product_exclusion`,
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_ab_product_involution_compiler`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier`
- **consumer:** `rate_half_band_closure`

For both deployed `b` rows, the ten canonical `S1` forced-record cells
give the following exact certificates:

```text
forced DE/DF:  two raw units, 25 terms, 79 S-pairs;
forced CE/CF:  two raw units, 23 terms, 56 S-pairs;
forced EF:     four bases containing s, 17/19 terms, 435 S-pairs;
forced loop:   two raw units, 17 terms, 55/57 S-pairs. (KB41BS1-1)
```

The forced-`EF` coordinate `s` is a nonzero outside representative.
For the loop cells, `-m` is already a square in the deployed base field:

```text
row 0: 101399882^2=-893470876,
row 1: 592085280^2=-1479361290.                  (KB41BS1-2)
```

The simultaneous outside sign changes transporting `c -> -c` preserve
the `S1` parity and permute the residual products.  Hence every `S1`
product cell is empty.  Together with the preceding `S0` and `S2`
exclusions, all `6+10+4=20` canonical forced-record cells are empty in
every common packet.  The common matching orbit `[3,6]` is closed at
product level; do not run its outside q or interpolation stages.

This theorem does not classify `[4,5,7,8]`, close all one-loop 442,
close the coordinate orientation or a row, or prove either Prize result.

## Falsifier

A guarded `S1` product realization in any forced type, parity, `b` row,
or `c` sign; an incorrect loop square root; or a product cell omitted from
the `6+10+4` census.
