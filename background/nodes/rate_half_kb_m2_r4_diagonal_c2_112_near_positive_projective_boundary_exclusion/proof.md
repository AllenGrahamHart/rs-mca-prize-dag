# Proof

Use homogeneous endpoint coordinates and orient the endpoint sent to the
forced source branch as `eta=infinity`. Then

```text
w=tau(eta)=0,       q_hom(T,Y)=Y(T-dY).
```

Its affine coefficient vector is `(-d,1,0)`. The repaired ramified formulas
therefore give

```text
V(T,W)=(-d,1+W,-dW),
z=(d-2)/(2-4d).                                      (1)
```

For the positive reciprocal coefficient vector `(x_0,...,x_4)`, membership
`U(T,0) in <q_hom>` is exactly

```text
x_2=0,             x_0+d x_3=0.                    (2)
```

Together with the three equations fixing `U(T,z)` from the chosen adjacent
internal edges, `(2)` is an invertible `5 x 5` system on the admissible open
set. This gives one reconstructed `U` for each of fixed-moving and
moving-moving.

Put `G=U^2-WV^2`. The projective roots of `q_hom` are `d` and infinity, so

```text
Res_T(q_hom,G)=G(d,W) * coeff_(T^4) G(T,W).          (3)
```

Both factors in `(3)` are divisible by `W^2`, exactly as required by the
ramified repair. Let their quadratic quotients be `R_d,R_infinity`. For each
relative `xi` orbit, passage requires

```text
R_d R_infinity ~ ((W-1/xi)(W-1/d))^2.               (4)
```

Compare the four nonleading coefficients in `(4)` after cross-multiplying by
the observed leading coefficient. This avoids dividing by a conjectural
generic factor. The fixed-moving systems for `xi=2,1/2,b` have unit full
forbidden saturations over `F_2130706433`.

For moving-moving and `xi=2,1/2`, every cross-multiplied equation is a
reciprocal degree-eight polynomial in `b`. Dividing by `b^4` and putting
`s=b+1/b` is exact. The endpoint/J0 collision and target-degree factors become

```text
d^2-ds+1,           ds-2,
```

respectively. Both trace systems have unit full-forbidden saturation.

For the other orbit, represent `xi=b`. If `C_d,C_infinity` and
`L_d,L_infinity` are the constant and leading coefficients of the two
residual quadratics, the constant-to-leading equation in `(4)` is

```text
(bd C_d C_infinity)^2=(L_d L_infinity)^2.           (5)
```

The characteristic is odd, so `(5)` splits into its two signs. Intersect
each sign equation with the remaining three coefficient equations. Both
full forbidden saturations are unit. Inversion `b->1/b` covers the other
representative of this reciprocal `xi` orbit.

The saturation product contains every denominator of `(1)--(4)`, all
endpoint/J0 and reciprocal collisions, `d=0,+/-1`, and the reconstruction
fixed-point factor `5d-4`. In moving-moving it also contains

```text
b^2d-2b+d,
```

whose vanishing makes the observed q-slice degree below four and hence
fails `(4)` before saturation. No admissible boundary point is removed.

The seven unit ideals have no geometric points over the base field's
algebraic closure, hence none over `F_(2130706433^6)`. QED.
