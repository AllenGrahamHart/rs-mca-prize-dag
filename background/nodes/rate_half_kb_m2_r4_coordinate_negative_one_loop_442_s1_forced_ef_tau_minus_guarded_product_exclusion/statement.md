# KoalaBear m2 r4 coordinate negative one-loop 442 S1 forced-EF tau-minus guarded product exclusion

- **status:** PROVED
- **scope:** common root-sign row `(epsilon_1,epsilon_2)=(1,1)`, outside
  skeleton `S1`, parity `tau_1=-1`, and both forced records `EF+` and `EF-`
  in the live sextic common orbit `[9,10,12,13]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_ef_tau_plus_guarded_product_exclusion`
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier`
- **consumer:** `rate_half_band_closure`

Use canonical singleton signs `alpha=beta=gamma=-1`, `delta=+1`.  For
`sigma in {+1,-1}`, force `sigma*ef=m`, put `f=sigma*m/e`, and scale by
`e^2`.  The residual sextic is

```text
J_sigma=(eX+sigma*cmZ)(eX-sigma*dmZ)(X+ceZ)
        (X+d^2Z)(X+deZ)(X+mZ),                   (KB41EM-1)
```

where the second factor now reflects `delta=+1`.

For either `sigma`, the three uniform equations have 17 monomials in
`(d,e)`.  In both irreducible cubic common components, exact Buchberger
reduction completes after 435 S-pairs with a basis containing `e=0`.
Therefore both `tau_1=-1` forced-`EF` cells are empty after the mandatory
nonzero-representative guard.

All four forced-`EF` cells and the four forced colored/cross cells are now
deleted in common sign row `(1,1)`.  Only its two forced-loop `S1` cells
remain, and the accepted four-row product frontier falls from 74 to 72.

This theorem does not delete those loop cells, transport to another common
root-sign row, impose outside `q` or interpolation, close the coordinate
orientation or a row, or prove either Prize result.

## Falsifier

A solution with `e!=0` in either cubic component for either `sigma`, or a
completed basis not containing the guard equation `e=0`.
