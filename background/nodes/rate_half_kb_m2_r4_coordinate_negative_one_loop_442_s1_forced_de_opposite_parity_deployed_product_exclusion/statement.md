# KoalaBear m2 r4 coordinate negative one-loop 442 S1 forced-DE opposite-parity deployed product exclusion

- **status:** PROVED
- **scope:** common root-sign row `(epsilon_1,epsilon_2)=(1,1)`, outside
  skeleton `S1`, singleton signs `(-1,-1,-1,1)`, and forced record `DE` in
  the live sextic common orbit `[9,10,12,13]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_de_deployed_product_exclusion`
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier`
- **consumer:** `rate_half_band_closure`

This is the `tau_1=-1` forced-`DE/DF` cell.  With `-de=m`, put
`e=-m/d`, `f=sd`.  Its scaled residual binary sextic is

```text
J_-=(dX-cmZ)(X+csdZ)(X+d^2Z)(X-sd^2Z)
    (X^2-m^2s^2Z^2).                              (KB41DO-1)
```

The uniform equations `E_0(J_-)=E_1(J_-)=E_2(J_-)=0` again have 25
`(d,s)` monomials.  In each of the two irreducible cubic components of the
representative deployed common quotient, exact Buchberger reduction reaches
the unit ideal after 79 S-pairs.  Thus this second canonical cell is empty
before guards.

Together with the `tau_1=+1` forced-`DE/DF` exclusion, both parity cells of
that forced-record type are deleted in common sign row `(1,1)`.  The accepted
four-row product frontier falls from 79 to 78 cells.

This theorem does not transport either deletion to another common root-sign
row, delete another forced-record type, impose outside `q` or interpolation,
close the coordinate orientation or a row, or prove either Prize result.

## Falsifier

A root of the three equations from `(KB41DO-1)` in either cubic component,
or a replay that does not reach `1` after 79 S-pairs.
