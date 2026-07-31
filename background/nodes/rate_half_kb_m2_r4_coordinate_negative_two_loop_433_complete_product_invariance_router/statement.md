# KoalaBear m2 r4 coordinate negative two-loop 433 complete-product invariance router

- **status:** PROVED
- **scope:** complete-source lifts of the exact `M2,M3` common-`K` ledgers
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_m2_m3_product_q_classifier`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_outside_product_involution_compiler`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_complete_edge_skeleton_classifier`
- **consumer:** `rate_half_band_closure`

Let `D,E,F` be representatives of the three antipodal `I` pairs in the
horizontal `T` coordinate.  They are independent of the quotient-coordinate
parameter `M`: the `T` and source/quotient involutions were normalized by
independent projectivities.  Never substitute `D,E,F in {1,M,M^2}`.

After changing the signs of `D,E,F`, the seven outside products in every
complete `(4,3,3)` packet have the canonical multiset

```text
S_tau={bD,cE,tau DE,DF,-DF,EF,-EF},       tau in {+1,-1}. (KB43R-1)
```

The forced `xi=-M` product from `(KB43O-6)` must be one of exactly five
canonical edge types

```text
bD,       cE,       tau DE,       DF,       EF.    (KB43R-2)
```

The omitted signs of `DF,EF` are equivalent by `F -> -F`.

Fix `epsilon in {-1,+1}`, `tau`, and one type `s_xi` in `(KB43R-2)`.
Impose the parent classifier and forced-value equation

```text
P_6=0,  4b^2+epsilon A b+4=0,  8c+bD_0+epsilon E_0=0,
H_epsilon s_xi-N_epsilon=0,                         (KB43R-3)
```

where `D_0,E_0` denote the parent locator polynomials, not the new pair
representatives `D,E`.

Remove `s_xi` from `S_tau` and form the squarefree binary sextic

```text
R(Y,Z)=product_(s in S_tau minus {s_xi})(Y-sZ).     (KB43R-4)
```

With `(Gamma,Alpha,Beta)` from `(KB43O-3)`, put

```text
R^iota(Y,Z)=R(Alpha Y+Beta Z, Gamma Y-Alpha Z).     (KB43R-5)
```

Every actual packet satisfies

```text
R^iota is projectively proportional to R,           (KB43R-6)
```

equivalently all 21 `2 x 2` minors of their seven coefficient vectors
vanish.  The sextic is also coprime to the fixed-point quadratic

```text
Gamma Y^2-2Alpha YZ-Beta Z^2.                       (KB43R-7)
```

Conversely, under product distinctness and `(KB43R-7)`, `(KB43R-6)` is
equivalent to partitioning the six residual products into three free orbits
of the exact product involution.  Thus all complete paired-product
possibilities lie in exactly

```text
2 cells M2/M3 x 2 signs tau x 5 xi types = 20 cells. (KB43R-8)
```

This router replaces 300 signed perfect-matching cases by 20 invariant-form
cells.  It does not assign quotient labels inside the three outside pairs,
choose `eta`, prove full twelve-row Mobius interpolation, impose q/resultant
equations, delete either cell, close the coordinate orientation, move an
owner/payment, close a row, or prove either Prize result.

## Falsifier

An actual `M2/M3` completion outside the 20 cells, failure of the sign gauge,
or a squarefree fixed-point-free sextic satisfying the paired-product gate
but not `(KB43R-6)`.
