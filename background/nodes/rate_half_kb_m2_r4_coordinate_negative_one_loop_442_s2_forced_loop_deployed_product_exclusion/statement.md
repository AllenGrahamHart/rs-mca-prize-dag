# KoalaBear m2 r4 coordinate negative one-loop 442 S2 forced-loop deployed product exclusion

- **status:** PROVED
- **scope:** the forced-loop `S2` invariant cell in every common root-sign
  row, and hence the complete `S2` product frontier, in the live sextic
  common orbit `[9,10,12,13]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s2_forced_df_guarded_product_exclusion`
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_common_sign_product_transport`
- **consumer:** `rate_half_band_closure`

Force the loop record `-e^2=m`.  Every remaining product occurs in a full
signed pair, so the choice of square root of `-m` disappears and no
quadratic extension is required.  In outside variables `(d,f)`, the
residual binary sextic is

```text
H=(X^2-c^2d^2 Z^2)(X^2-d^2f^2 Z^2)
  (X^2+m f^2 Z^2).                            (KB41S2L-1)
```

The three uniform equations each have seven monomials.  Exact Buchberger
reduction in both cubic common components reaches the raw unit ideal after
seven S-pairs.  The common `b,c,m` data are identical in all four common
sign rows, so the deletion transports to every row.

Together with the preceding forced-colored, forced-`EF`, and forced-`DF`
exclusions, all sixteen `S2` product cells are empty.  The accepted
invariant-cell frontier falls from 28 to 24 and consists exactly of the six
`S0` cells in each common sign row.

This theorem does not delete an `S0` cell, impose outside `q` or full
interpolation, close the coordinate orientation or a row, or prove either
Prize result.

## Falsifier

A root of the three equations in either cubic component, a non-unit basis,
or a residual coefficient depending on a choice of square root of `-m`.
