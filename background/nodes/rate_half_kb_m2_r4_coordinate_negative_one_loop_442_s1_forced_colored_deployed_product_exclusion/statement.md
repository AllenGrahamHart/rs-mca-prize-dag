# KoalaBear m2 r4 coordinate negative one-loop 442 S1 forced-colored deployed product exclusion

- **status:** PROVED
- **scope:** common root-sign row `(epsilon_1,epsilon_2)=(1,1)`, outside
  skeleton `S1`, both outside parity cells, and forced colored record
  `CE/CF` in the live sextic common orbit `[9,10,12,13]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_de_opposite_parity_deployed_product_exclusion`
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier`
- **consumer:** `rate_half_band_closure`

Use the canonical signs `alpha=beta=gamma=-1` and
`delta in {+1,-1}`.  Forcing the colored record `CE` gives `-ce=m`, hence
`e=-m/c`.  The residual binary sextic is

```text
J_delta=(X+cfZ)(X+d^2Z)(X-dm/c Z)(X-delta*dfZ)
        (X^2-m^2f^2/c^2 Z^2).                    (KB41FC-1)
```

The two choices of `delta` are exactly the two `S1` parity cells of the
forced-`CE/CF` orbit type.  For either choice, the uniform equations
`E_0=E_1=E_2=0` have 23 monomials in `(d,f)`.  In each of the two irreducible
cubic components of the representative deployed common quotient, exact
Buchberger reduction reaches the unit ideal after 56 S-pairs.

Therefore both forced-colored parity cells are empty before guards.  Together
with the two forced-`DE/DF` deletions, four of the ten `S1` cells in common
sign row `(1,1)` are deleted, and the accepted four-row product frontier
falls from 78 to 76 cells.

This theorem does not transport a deletion to another common root-sign row,
delete the forced-loop or forced-`EF` types, impose outside `q` or full
interpolation, close the coordinate orientation or a row, or prove either
Prize result.

## Falsifier

A root of `(KB41FC-1)` and the three uniform equations in either cubic
component for either sign of `delta`, or a replay not reaching `1` after 56
S-pairs.
