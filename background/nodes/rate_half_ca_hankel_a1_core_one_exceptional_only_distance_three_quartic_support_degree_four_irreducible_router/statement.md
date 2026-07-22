# `A=1` distance-three quartic support degree-four irreducible router

- **status:** PROVED
- **closure:** proof using a published subgroup-curve bound
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_antiweight_absorption`

Retain the remaining degree-four common-fiber branch. Thus a separable
base-field rational map `psi` contains at least `e-148` matched exceptional
pairs in its fibers. Then at least one of the following holds:

1. the off-diagonal coincidence divisor of `psi` is geometrically
   reducible; or
2. after a target Mobius transformation, and possibly the subgroup
   inversion `X |-> X^(-1)`, the map has the Laurent-end form

   ```text
   psi(X)=X^3+aX^2+bX+c+d/X,       d!=0,             (Q4R1)
   ```

   and its absolutely irreducible off-diagonal curve is

   ```text
   XY[X^2+XY+Y^2+a(X+Y)+b]-d=0.                    (Q4R2)
   ```

Every other absolutely irreducible degree-four map has fewer than
`2(e-148)` ordered off-diagonal subgroup collisions and cannot contain the
required pairs.

Hence the degree-four frontier consists only of a reducible coincidence
divisor or the explicit three-parameter Laurent-end curve `(Q4R2)`; the
irrelevant additive constant `c` does not enter that curve. This node does
not exclude either remaining branch.
