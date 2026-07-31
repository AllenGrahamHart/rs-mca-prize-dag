# KoalaBear m2 r4 coordinate negative one-loop 442 S2 forced-EF guarded product exclusion

- **status:** PROVED
- **scope:** the forced-`EF` `S2` invariant cell in every common root-sign
  row of the live sextic common orbit `[9,10,12,13]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s2_forced_colored_deployed_product_exclusion`
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_common_sign_product_transport`
- **consumer:** `rate_half_band_closure`

Force `sigma*e*f=m`, so `f=sigma*m/e`.  Since outside representatives are
nonzero, multiplying the residual sextic by `e^2` preserves its invariance
equations on the admissible locus.  The resulting polynomial form is

```text
H~=(X^2-c^2d^2 Z^2)(X+e^2 Z)
   (e^2X^2-m^2d^2 Z^2)(X+mZ).              (KB41S2E-1)
```

The three uniform equations each have seven monomials in `(d,e)`.  In both
cubic common components, exact Buchberger reduction completes after 28
S-pairs with a monic basis element `e^2`.  Thus every solution has `e=0`,
contrary to the outside-representative guard used in the forced
substitution.  The cell is guard-empty.

The exact common `b,c,m` data are identical in all four common sign rows,
so this guarded deletion transports to every row.  All four forced-`EF`
`S2` cells are empty and the accepted invariant-cell frontier falls from 36
to 32.

This theorem does not claim a raw unit ideal, delete another `S2` cell or an
`S0` cell, impose outside `q` or full interpolation, close the coordinate
orientation or a row, or prove either Prize result.

## Falsifier

An admissible root with `e!=0`, or failure of either completed basis to
contain the monic equation `e^2=0`.
