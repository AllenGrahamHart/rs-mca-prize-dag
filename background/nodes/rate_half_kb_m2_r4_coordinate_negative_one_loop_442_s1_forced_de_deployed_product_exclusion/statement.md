# KoalaBear m2 r4 coordinate negative one-loop 442 S1 forced-DE deployed product exclusion

- **status:** PROVED
- **scope:** common root-sign row `(epsilon_1,epsilon_2)=(1,1)`, outside
  skeleton `S1`, singleton signs `(1,-1,-1,1)`, and forced record `DE` in
  the live sextic common orbit `[9,10,12,13]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_sextic_quotient_classifier`,
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_sextic_mate_coordinate_compiler`,
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_binary_sextic_uniform_row_selector`
- **consumer:** `rate_half_band_closure`

Let `m` be the forced mate.  The forced equation is `-de=m`.  Put
`e=-m/d`, `f=sd`, and multiply the residual monic sextic by the nonzero
scalar `d`.  The resulting binary form is

```text
J=(dX+cmZ)(X+csdZ)(X+d^2Z)(X-sd^2Z)
  (X^2-m^2s^2Z^2).                                (KB41DX-1)
```

Reduce the uniform equations `E_0(J)=E_1(J)=E_2(J)=0` in the representative
rank-six common quotient.  Each has 25 monomials in `(d,s)` with coefficient
vectors in the quotient.

Over the deployed field, the sextic common factor splits into two
irreducible cubics

```text
b^3+674394299b^2-1005684111b+1057281976,
b^3-674394301b^2+424510262b+414697007.            (KB41DX-2)
```

In each cubic field component, exact two-variable Buchberger reduction of
the three equations reaches `1` after 79 S-pairs.  Hence `(KB41DX-1)` has no
solution even before imposing nonzero or injectivity guards.  The specified
canonical forced-record cell is empty and is deleted from the accepted
product frontier, reducing that frontier from 80 to 79 cells.

This theorem does not delete another forced-record or common sign cell,
assign the seven outside source fibers, impose outside `q` rows or full
interpolation, close the coordinate orientation or a row, or prove either
Prize result.

## Falsifier

A root of the three reduced equations in either cubic component, failure of
the factorization `(KB41DX-2)`, or a replay where the exact Buchberger basis
does not reach the unit ideal.
