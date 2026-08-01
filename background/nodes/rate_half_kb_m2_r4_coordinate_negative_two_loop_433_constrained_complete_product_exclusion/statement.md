# KoalaBear m2 r4 coordinate negative two-loop 433 constrained complete-product exclusion

- **status:** PROVED
- **scope:** all thirty complete-product cells over `X2,N1,L1`, and hence
  the remaining `(4,3,3)` two-loop frontier
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_constrained_product_q_classifier`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_constrained_outside_product_involution_compiler`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_m2_m3_complete_product_exclusion`
- **consumer:** `rate_half_band_closure`

All thirty constrained cells are empty over the deployed KoalaBear
characteristic.  Together with the `M2/M3` parent, the entire `(4,3,3)`
two-loop skeleton is impossible at the necessary complete paired-product
gate.

Use the exact rank-eight base algebras

```text
R_X =F_p[M,c]/(P_8,(c^2+1)(M+1)^2-c(M-1)^2),
R_N =F_p[M,c]/(P_8,(c^2+1)(M+1)^2+c(M-1)^2),
R_L =F_p[c,M]/(2c^4+3c^2+2,M^2+1).              (KB43Y-1)
```

In each algebra insert the compiler's exact `b=-c^3`, forced product `p`,
and `(Gamma,Alpha,Beta)`.  Write the seven outside products as

```text
X=bD, Y=cE, Z=tau XY/(bc), U=DF, V=bYU/(cX).
```

For forced types `X,Y,Z,U,V`, the residual sextics are respectively

```text
(a,tau pa/(bc),x,-x,bax/(cp),-bax/(cp));
(a,tau pa/(bc),x,-x,bpx/(ca),-bpx/(ca));
(a,tau pbc/a,x,-x,tau pb^2x/a^2,-tau pb^2x/a^2);
(a,q,tau aq/(bc),-p,bpq/(ca),-bpq/(ca));
(a,q,tau aq/(bc),cpa/(bq),-cpa/(bq),-p).         (KB43Y-2)
```

For each form and each of fifteen perfect matchings, clear its three
involution equations and eliminate the two intrinsic variables.  There are
75 universal obstruction templates.  The first projection is nonzero in 60
templates and the second resolves the other 15.

Evaluation in `(KB43Y-1)` gives exactly

```text
3 ledgers x 2 tau x 5 forced types x 15 matchings = 450 (KB43Y-3)
```

unit obstructions.  The primary certificate uses quadratic norm and gcd in
each rank-eight algebra.  Independent shards share the second pair equation
for every template and verify rank eight for every obstruction's
multiplication matrix.  All 450 alternate checks pass.

No constrained cell reaches full twelve-label interpolation or any
remaining q/colored-resultant equation.  Since `X1,N2,Z1,M1` were already
deleted and `M2,M3` have no complete-product lift, the full `(4,3,3)`
skeleton is closed.

This theorem does not close another coordinate skeleton, the complete
coordinate orientation, a Prize row, or either Prize result.

## Falsifier

A guarded constrained complete-product packet, a nonunit obstruction in
either projection order, a deficient multiplication matrix, or a surviving
`(4,3,3)` common row omitted from the parent census.
