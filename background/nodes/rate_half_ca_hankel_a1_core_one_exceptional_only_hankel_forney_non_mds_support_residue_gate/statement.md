# `A=1` exceptional non-MDS support-residue gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_non_mds_annihilating_pair_router`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_coefficient_biisotropic_plane`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_forney_numerator_normal_form`

Retain a non-MDS annihilating pair and its unnormalized numerators
`H_lambda,H_nu`. Since `A` divides their product, define

```text
K_lambda,nu=H_lambda H_nu/A in F_field[X].           (HNR1)
```

Let `Phi` be the Forney numerator and `B_T` the minimal quotient-support
locator. Then every valid endpoint packet satisfies

```text
sum_(B_T(t)=0) Phi(t)K_lambda,nu(t)
                  ------------------- =0.             (HNR2)
                   A(t)B_T'(t)
```

Equivalently, in `F_field[X]/(B_T)`,

```text
[X^(h-1)] rem_(B_T)(Phi K_lambda,nu A^(-1))=0,
h=deg B_T.                                           (HNR3)
```

There is an equivalent exceptional-side boundary identity:

```text
sum_(A(a)=0) beta_a q_1(a)K_lambda,nu(a)
 =[X^(h+2e-1)] Phi K_lambda,nu                       (HNR4)
 =Theta_2 lc(K_lambda,nu) if deg K_lambda,nu=2e+2,
 =0                         if deg K_lambda,nu<=2e+1. (HNR5)
```

Here `deg K_lambda,nu<=2e+2` follows from `deg_X Q=2e+1`.

If the common half-rank deficiency is `d`, choose numerator bases
`H_lambda_s` and `H_nu_t` for the two shortening spaces. Then
`(HNR1)--(HNR5)` hold for every

```text
K_s,t=H_lambda_s H_nu_t/A,       1<=s,t<=d.          (HNR6)
```

Thus deficiency `d` carries a `d`-by-`d` matrix of exact residue gates.

In the exact-half branch `A=D_uD_v`, writing
`H_lambda=D_uR_u` and `H_nu=D_vR_v` gives
`K_lambda,nu=R_uR_v`. In the excess-zero branch the same gate retains the
overlap factor. This is a necessary scalar certificate, not yet an exclusion
of either branch.
