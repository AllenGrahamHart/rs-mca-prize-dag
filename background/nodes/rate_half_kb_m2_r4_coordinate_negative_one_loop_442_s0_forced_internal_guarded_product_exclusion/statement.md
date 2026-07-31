# KoalaBear m2 r4 coordinate negative one-loop 442 S0 forced-internal guarded product exclusion

- **status:** PROVED
- **scope:** both parity cells of the forced-internal `S0` record type in
  every common root-sign row, and hence the complete 80-cell invariant-
  product frontier of the live sextic nonloop-singleton common orbit
  `[9,10,12,13]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s0_forced_ef_guarded_product_exclusion`
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_common_sign_product_transport`
- **consumer:** `rate_half_band_closure`

Choose `alpha=beta=1`, `gamma=tau_0`, and force one signed internal record
`d*e=m`, so `e=m/d`.  Clearing the admissible denominator by multiplying
the residual sextic by `d^2` gives

```text
H~_tau=(dX-cmZ)(X-cfZ)(X+mZ)(X^2-d^2f^2 Z^2)
       (dX-tau_0*mfZ).                         (KB41S0I-1)
```

For either parity, the three uniform equations each have fourteen
monomials in `(d,f)`.  In both cubic common components, exact Buchberger
reduction completes after 406 S-pairs with the monic basis element `f`.
Thus every solution has `f=0`, contrary to the nonzero outside-
representative guard.

The common `b,c,m` data are identical in all four common sign rows, so both
guarded deletions transport to every row.  All eight forced-internal `S0`
cells are empty.  Together with the preceding forced-colored and
forced-`EF` exclusions, all twenty-four `S0` cells are empty; together with
the `S1` and `S2` closes, all eighty invariant-product cells in this common
orbit are empty.  Its accepted product frontier falls from 8 to 0.

This theorem does not classify or delete another common matching orbit,
close every one-loop 442 case, close the coordinate orientation or a row,
or prove either Prize result.

## Falsifier

An admissible root with `f!=0` for either parity in either component, or an
unaccounted forced-record orbit among the proved `6+10+4` cells per row.
