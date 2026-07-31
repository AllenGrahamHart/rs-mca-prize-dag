# KoalaBear m2 r4 coordinate negative one-loop 442 S2 forced-colored deployed product exclusion

- **status:** PROVED
- **scope:** the forced-colored `S2` invariant cell in every common root-sign
  row of the live sextic common orbit `[9,10,12,13]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_common_sign_product_transport`
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_binary_sextic_invariance_compiler`
- **consumer:** `rate_half_band_closure`

The `S2` product records are

```text
CD+, CD-, EE, DF+, DF-, EF+, EF-.
```

Forcing `sigma*c*d=m` gives `d=sigma*m/c`; the opposite colored record is
`-m`, and the sign disappears from every remaining product.  In outside
variables `(e,f)`, the residual binary sextic is

```text
H=(X+mZ)(X+e^2 Z)
  (X^2-(m/c)^2 f^2 Z^2)(X^2-e^2 f^2 Z^2).       (KB41S2C-1)
```

The uniform equations `E_0,E_1,E_2` each have seven monomials.  Exact
Buchberger reduction in both cubic common components reaches the raw unit
ideal after seven S-pairs.  The exact `b,c,m` component data are identical
in all four common sign rows, so the same certificate transports to every
row.  All four forced-colored `S2` cells are empty, and the accepted
invariant-cell frontier falls from 40 to 36.

This theorem does not delete another `S2` cell or an `S0` cell, impose
outside `q` or full interpolation, close the coordinate orientation or a
row, or prove either Prize result.

## Falsifier

A root of the three equations in either cubic component, a non-unit basis,
or a common row in which the projected `b,c,m` data differ.
