# KoalaBear m2 r4 coordinate negative one-loop 442 S0 forced-EF guarded product exclusion

- **status:** PROVED
- **scope:** both parity cells of the forced-`EF` `S0` record type in every
  common root-sign row of the live sextic common orbit `[9,10,12,13]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s0_forced_colored_deployed_product_exclusion`
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_common_sign_product_transport`
- **consumer:** `rate_half_band_closure`

Choose `alpha=beta=1`, `gamma=tau_0`, and force
`tau_0*e*f=m`, so `f=tau_0*m/e`.  Clearing the admissible denominator by
multiplying the residual sextic by `e^3` gives

```text
H~_tau=(X-ceZ)(eX-tau_0*cmZ)(X^2-d^2e^2 Z^2)
       (e^2X^2-m^2d^2 Z^2).                   (KB41S0E-1)
```

For either parity, the three uniform equations each have twelve monomials
in `(d,e)`.  In both cubic common components, exact Buchberger reduction
completes after 190 S-pairs with the monic basis element `e^2`.  Thus every
solution has `e=0`, contradicting the forced-substitution guard.

The common `b,c,m` data are identical in all four common sign rows, so both
guarded deletions transport to every row.  All eight forced-`EF` `S0` cells
are empty.  The accepted invariant-cell frontier falls from 16 to 8,
consisting of the two forced-internal parity cells in each row.

This theorem does not claim raw unit ideals, delete the forced-internal
`S0` cells, impose outside `q` or full interpolation, close the coordinate
orientation or a row, or prove either Prize result.

## Falsifier

An admissible root with `e!=0` for either parity in either component, or a
completed basis missing `e^2`.
