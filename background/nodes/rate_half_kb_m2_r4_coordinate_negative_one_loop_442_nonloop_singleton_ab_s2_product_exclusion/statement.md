# KoalaBear m2 r4 coordinate negative one-loop 442 AB-singleton S2 product exclusion

- **status:** PROVED
- **scope:** all `S2` outside product cells over the finite common orbit
  `[3,6]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_ab_product_involution_compiler`
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier`
- **consumer:** `rate_half_band_closure`

For each of the two deployed `b` rows, remove the forced mate
`m=(18-5b)/22` from the seven `S2` products and impose invariance of the
residual binary sextic under the common product involution.  The four
canonical forced-record types give:

```text
forced CD:    raw unit ideal after 7 S-pairs;
forced EE:    raw unit ideal after 7 S-pairs;
forced DF:    completed basis contains d^2 and e^2;
forced EF:    completed basis contains e^2.       (KB41BS2-1)
```

Each system has three equations with seven monomials.  Outside
representatives are nonzero, so the latter two are guarded deletions.
Changing the sign of `c` does not change an `S2` system: `CD` occurs
as a full signed pair and the action coefficients use only `c^2`.
Therefore every `S2` product cell over all sixteen common packets is
empty.

This theorem does not classify `S0` or `S1`, impose outside q equations
or full interpolation, classify `[4,5,7,8]`, close the coordinate
orientation or a row, or prove either Prize result.

## Falsifier

A guarded `S2` product realization in either `b` row or `c` sign, a
forced-record orbit omitted from `(KB41BS2-1)`, or failure of the printed
unit/guard certificates.
