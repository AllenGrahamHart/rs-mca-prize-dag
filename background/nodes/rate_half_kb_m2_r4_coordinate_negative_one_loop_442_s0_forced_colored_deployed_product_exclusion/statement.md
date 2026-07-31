# KoalaBear m2 r4 coordinate negative one-loop 442 S0 forced-colored deployed product exclusion

- **status:** PROVED
- **scope:** both parity cells of the forced-colored `S0` record type in
  every common root-sign row of the live sextic common orbit `[9,10,12,13]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s2_forced_loop_deployed_product_exclusion`
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_common_sign_product_transport`
- **consumer:** `rate_half_band_closure`

Choose canonical `S0` signs `alpha=beta=1` and `gamma=tau_0`, where
`tau_0 in {+1,-1}`.  Force the colored singleton `CE=m`, so `e=m/c`.
The residual binary sextic is

```text
H_tau=(X-cfZ)(X^2-(m/c)^2d^2 Z^2)
      (X^2-d^2f^2 Z^2)(X-tau_0(m/c)fZ).     (KB41S0C-1)
```

For either parity, the three uniform equations each have eleven monomials
in `(d,f)`.  Exact Buchberger reduction in both cubic common components
reaches the raw unit ideal after 29 S-pairs.  The common `b,c,m` data are
identical in all four common sign rows, so both parity deletions transport
to every row.

All eight forced-colored `S0` cells are empty.  The accepted invariant-cell
frontier falls from 24 to 16, consisting of the two forced-`EF` and two
forced-internal `S0` cells in each common sign row.

This theorem does not delete another `S0` cell, impose outside `q` or full
interpolation, close the coordinate orientation or a row, or prove either
Prize result.

## Falsifier

A root for either parity in either cubic component, or a common row in which
the projected `b,c,m` data differ.
