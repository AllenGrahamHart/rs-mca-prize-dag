# Budget-three fiber-two cycle boundary transfer

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_quotient_embedding`,
  `rate_half_list_budget_three_antipodal_reverse_residual_stratification`,
  `rate_half_list_budget_three_antipodal_pure_quartic_degree_rigidity`,
  `rate_half_list_budget_three_antipodal_fourth_root_gap_reduction`,
  `rate_half_list_budget_three_antipodal_generic_secondary_gap_reduction`,
  `rate_half_list_budget_three_antipodal_generic_two_window_square_reduction`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_parity_reduction`,
  `rate_half_list_budget_three_antipodal_generic_canonical_span_criterion`

Retain any of the three quartic-pencil strata from the fiber-two cycle router
at the prize maximum. Put

```text
N=2^40,       s=2^38,       r=s-1,
D_* product_i(U+c_iV)=Y^N-1,       sum_i c_i=0,       (F2B1)
```

where `D_*` is monic squarefree of degree four, `U` is monic of degree `r`,
`v=deg V<=r-1`, and the `c_i` are distinct. Let

```text
q=min{j in {2,3,4}:e_j(c_0,c_1,c_2,c_3)!=0},
h=r-v,
T=ND_*U-Y(D_*'U+4D_*U').                              (F2B2)
```

Then the parameter-uniform reverse-residual theorem gives

```text
deg T=r+4-qh.                                          (F2B3)
```

The two lowest nonpure boundaries have the exact doubled-order ledger

```text
generic q=2:
  v=2^37-2,       h=2^37+1,       deg T=1,

intermediate q=3:
  v=(2^39-5)/3,   h=(2^38+2)/3,   deg T=1.             (F2B4)
```

Thus both boundaries have the same primary fourth-root gap. If

```text
E(z)=z^4D_*(z^-1),       E^(-1/4)=sum_(m>=0)a_mz^m,
```

then

```text
a_(2^38)=a_(2^38+1)=0,       a_(2^38+2)!=0.           (F2B5)
```

On the generic boundary, the normalized secondary square root also satisfies

```text
[z^(2^37-1)]P=[z^(2^37)]P=0.                          (F2B6)
```

Equivalently, with `h=2^37+1`, the two-window theorem has

```text
N=8h-8,       r=2h-3,       deg C<=h-3=2^37-2,        (F2B7)
```

and its exact truncated square identity. If the four roots of `D_*` are two
antipodal pairs, the parity reduction applies with

```text
M=2^36,       N=16M,
F_(2M)(t)=0,       F_(2M+1)(t)!=0,       G_M(t)=0,
t in mu_(8M)\{1}.                                     (F2B8)
```

On the pure outer stratum `e_2=e_3=0`, one instead has

```text
v=r-1=2^38-2,                                         (F2B9)
```

together with the squarefreeness, one-point support-overlap cap, and linear
Wronskian residual of the pure-quartic theorem.

The generic canonical certifier also transfers, with one necessary change.
It computes `B,Q,Rbar,Cbar`, the unique scalars `alpha,beta,gamma`, and the
outer quartic

```text
W^4+alpha W^2+beta W+gamma.                            (F2B10)
```

For a fiber-two cycle solution, the four distinct roots of `(F2B10)` must be
one fractional-linear image of the four completion roots `rho_i`. Conversely,
that matching, the canonical span identity, and the cycle router's exact
`D_*`/exceptional-factor inventory reconstruct the quotient pencil and the
original cycle locator relation.

For `c=0`, this is the existing condition because `rho_i^2` are exactly the
four roots of `D_*`. For `c=1,2`, matching to square-root lifts of all four
denominator roots is the wrong condition; the completion-root matching above
is the correct one. Consequently the old one-parameter Mobius-ratio and norm
gates cannot be imported into the mismatch strata without a new coupling
derivation.

This theorem completes the doubled-order symbolic transfer through the
canonical certifier. It does not exclude any boundary, cover above-floor
solutions, or authorize the deferred `M=2^36` computation.
