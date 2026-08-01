# KoalaBear m2 r4 coordinate negative one-loop 442 S1 forced-EF tau-plus guarded product exclusion

- **status:** PROVED
- **scope:** common root-sign row `(epsilon_1,epsilon_2)=(1,1)`, outside
  skeleton `S1`, parity `tau_1=+1`, and both forced records `EF+` and `EF-`
  in the live sextic common orbit `[9,10,12,13]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_colored_deployed_product_exclusion`
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier`
- **consumer:** `rate_half_band_closure`

Use canonical singleton signs `alpha=beta=gamma=delta=-1`.  Let
`sigma in {+1,-1}` select forced record `EF+` or `EF-`; its forced equation
is `sigma*ef=m`.  Put `f=sigma*m/e` and multiply the residual sextic by
`e^2`.  The resulting binary form is

```text
J_sigma=(eX+sigma*cmZ)(eX-sigma*dmZ)(X+ceZ)
        (X+d^2Z)(X+deZ)(X+mZ).                   (KB41EP-1)
```

For either `sigma`, the uniform equations `E_0=E_1=E_2=0` have 19
monomials in `(d,e)`.  In both irreducible cubic common components, exact
Buchberger reduction completes after 435 S-pairs with a basis containing

```text
e=0.                                               (KB41EP-2)
```

The raw ideals are not unit, but every raw solution violates the mandatory
nonzero target-representative guard.  Hence both forced-`EF` cells of parity
`tau_1=+1` are empty after guard saturation.  The accepted four-row product
frontier falls from 76 to 74 cells.

This theorem does not delete the opposite-parity forced-`EF` cells, either
forced-loop cell, transport to another common root-sign row, impose outside
`q` or interpolation, close the coordinate orientation or a row, or prove
either Prize result.

## Falsifier

A solution with `e!=0` in either cubic component for either sign of `sigma`,
or a completed basis that does not contain `(KB41EP-2)`.
