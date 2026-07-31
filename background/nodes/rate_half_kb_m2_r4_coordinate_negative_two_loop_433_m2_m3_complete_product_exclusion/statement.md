# KoalaBear m2 r4 coordinate negative two-loop 433 M2/M3 complete-product exclusion

- **status:** PROVED
- **scope:** all twenty invariant-product cells over the exact `M2,M3`
  common-`K` ledgers
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_m2_m3_product_q_classifier`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_outside_product_involution_compiler`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_complete_edge_skeleton_classifier`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_complete_product_invariance_router`
- **consumer:** `rate_half_band_closure`

All twenty cells are empty over the deployed KoalaBear characteristic.

For `epsilon=-1` on `M2` and `epsilon=+1` on `M3`, use the parent notation
`P_6,A,D_0,E_0,N_epsilon,H_epsilon` and form the rank-twelve deployed base
algebra

```text
R_epsilon=F_p[M,b]/(P_6,
                     4b^2+epsilon A(M)b+4),
c=-(bD_0+epsilon E_0)/8,
p=N_epsilon/H_epsilon,                            (KB43V-1)
```

where `p=2130706433`.  The elements `b,c,p,Gamma,Alpha,Beta` are all units
in both algebras.

Write the seven outside products as

```text
X=bD,  Y=cE,  Z=tau DE=tau XY/(bc),
U=DF,  V=EF=bYU/(cX),
S={X,Y,Z,U,-U,V,-V}.                              (KB43V-2)
```

For each possible forced value `p`, the six residual products have one of
the following exact forms:

```text
X=p: (a,tau pa/(bc),x,-x,bax/(cp),-bax/(cp));
Y=p: (a,tau pa/(bc),x,-x,bpx/(ca),-bpx/(ca));
Z=p: (a,tau pbc/a,x,-x,tau pb^2x/a^2,-tau pb^2x/a^2);
U=p: (a,q,tau aq/(bc),-p,bpq/(ca),-bpq/(ca));
V=p: (a,q,tau aq/(bc),cpa/(bq),-cpa/(bq),-p).    (KB43V-3)
```

For each of the five forms and each of the fifteen perfect matchings,
substitute its three pairs into

```text
Gamma yz-Alpha(y+z)-Beta=0.                       (KB43V-4)
```

Clear denominators and eliminate the two intrinsic variables.  This gives
75 universal obstruction polynomials in the base constants.  Sharing the
first pair equation gives a nonzero obstruction in 60 templates; sharing
the second equation resolves the other 15 projection degeneracies.

Evaluate the obstructions at both `epsilon` values and both `tau` signs in
`R_epsilon`.  Every one of the resulting

```text
2 epsilon x 2 tau x 5 forced types x 15 matchings = 300   (KB43V-5)
```

elements is a unit.  The primary certificate tests this by the quadratic
norm and gcd with `P_6`.  Independent audit shards share the second pair
equation for all 75 templates and test invertibility by the rank of the
`12 x 12` multiplication matrix; all 300 ranks are twelve.

Hence neither `M2` nor `M3` has a complete paired-product lift.  Their
20-cell frontier is empty before full twelve-label interpolation or any
remaining q/colored-resultant equation.

This theorem does not treat the separate `X2,N1,L1` common-`K` ledgers,
close the whole `(4,3,3)` skeleton or coordinate orientation, close a Prize
row, or prove either Prize result.

## Falsifier

A guarded `M2/M3` complete-product packet; a nonunit protected denominator;
a nonunit obstruction in `(KB43V-5)`; or disagreement between the norm and
multiplication-matrix unit tests.
