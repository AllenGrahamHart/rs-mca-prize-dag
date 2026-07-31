# KoalaBear m2 r4 coordinate negative one-loop 442 S2 forced-DF guarded product exclusion

- **status:** PROVED
- **scope:** the forced-`DF` `S2` invariant cell in every common root-sign
  row of the live sextic common orbit `[9,10,12,13]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s2_forced_ef_guarded_product_exclusion`
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_common_sign_product_transport`
- **consumer:** `rate_half_band_closure`

Force `sigma*d*f=m`, so `f=sigma*m/d`.  Clearing the admissible denominator
by multiplying the residual sextic by `d^2` gives

```text
H~=(X^2-c^2d^2 Z^2)(X+e^2 Z)(X+mZ)
   (d^2X^2-m^2e^2 Z^2).                     (KB41S2D-1)
```

The three uniform equations each have seven monomials in `(d,e)`.  In both
cubic common components, exact Buchberger reduction completes after 28
S-pairs with monic basis elements `d^2` and `e^2`.  In particular every
solution has `d=0`, contradicting the guard used in the forced substitution.
The cell is guard-empty.

The exact common `b,c,m` data are identical in all four common sign rows,
so this guarded deletion transports to every row.  All four forced-`DF`
`S2` cells are empty and the accepted invariant-cell frontier falls from 32
to 28.

This theorem does not claim a raw unit ideal, delete the forced-loop `S2`
cell or an `S0` cell, impose outside `q` or full interpolation, close the
coordinate orientation or a row, or prove either Prize result.

## Falsifier

An admissible root with `d!=0`, or failure of either completed basis to
contain the monic equation `d^2=0`.
