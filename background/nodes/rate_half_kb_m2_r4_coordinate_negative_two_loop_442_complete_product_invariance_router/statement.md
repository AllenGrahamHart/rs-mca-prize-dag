# KoalaBear m2 r4 coordinate negative two-loop 442 complete-product invariance router

- **status:** PROVED
- **scope:** complete-source lifts of the six q-compatible common-`K`
  product rows `(KB4P-3)--(KB4P-5)`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_exceptional_product_classifier`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_outside_product_involution_compiler`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_edge_skeleton_classifier`
- **consumer:** `rate_half_band_closure`

Let `D,E,F` be representatives of the three antipodal `I` pairs in the
horizontal `T` coordinate.  They are independent of the quotient-coordinate
parameter `l`: the `T` and source/quotient involutions were normalized by
independent projectivities.  Never substitute `D,E,F` by powers of `l`.

After changing the signs of `D,E,F`, the seven outside products have the
canonical multiset

```text
S_sigma={cD,cE,sigma DE,DF,-DF,EF,-EF},
sigma in {+1,-1}.                                 (KB44R-1)
```

The residual symmetry `D <-> E`, together with `F -> -F`, reduces the
possible edge type carrying the forced product `p_xi=N_r/H_r` to

```text
cD,       sigma DE,       DF.                     (KB44R-2)
```

These represent respectively either colored `C-I` edge, the unique `D-E`
type, and any of the four signed `D/E-F` types.

Fix one of the six common rows `r`, one sign `sigma`, and one type `s_xi`
in `(KB44R-2)`.  Impose the exact row ideal from `(KB4P-3)--(KB4P-5)` and
the forced-value equation

```text
H_r s_xi-N_r=0,                                   (KB44R-3)
```

where `N_r,H_r` are the three row-family formulas `(KB44O-4)`.  Remove the
chosen occurrence from `S_sigma` and form the binary sextic

```text
R(Y,Z)=product_(s in S_sigma minus {s_xi})(Y-sZ). (KB44R-4)
```

Let `(Gamma_r,Alpha_r,Beta_r)` be the exact cross product `(KB44O-3)` and
put

```text
R^iota(Y,Z)=R(Alpha_r Y+Beta_r Z,
               Gamma_r Y-Alpha_r Z).             (KB44R-5)
```

Every actual packet satisfies

```text
R^iota is projectively proportional to R,          (KB44R-6)
```

equivalently all 21 `2 x 2` coefficient minors vanish.  Product
distinctness makes `R` squarefree, and it must be coprime to the fixed-point
quadratic

```text
Gamma_r Y^2-2Alpha_r YZ-Beta_r Z^2.               (KB44R-7)
```

Conversely, squarefreeness, `(KB44R-6)`, and `(KB44R-7)` partition the six
residual products into the three free orbits of the exact product
involution.  Thus all complete paired-product possibilities lie in exactly

```text
6 common rows x 2 signs sigma x 3 xi types = 36 cells. (KB44R-8)
```

The two q orientations above each common product row do not change these
product cells and remain to be carried into the later q equations.  This
router replaces 540 sign-gauged residual perfect-matching cases by 36
invariant-form cells.

It does not assign quotient labels within the three outside pairs, choose
`eta`, prove full twelve-row Mobius interpolation, impose remaining q or
colored-resultant equations, delete a cell or common row, close the
coordinate orientation, move an owner/payment, close a row, or prove either
Prize result.

## Falsifier

An actual complete `442` packet outside the 36 cells, failure of the sign or
location quotient, or a squarefree fixed-point-free sextic satisfying the
paired-product gate but not `(KB44R-6)`.
