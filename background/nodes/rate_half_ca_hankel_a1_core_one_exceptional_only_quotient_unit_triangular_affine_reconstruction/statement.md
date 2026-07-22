# `A=1` exceptional quotient unit triangular affine reconstruction

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_w_interpolation_normal_form`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_reciprocal_bezout_normalization`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_full_reciprocal_square_descent`

Expand

```text
F=sum_i f_iY^i,       L=sum_i l_iY^i,
W_0=sum_(k=0)^(r-1) w_k^0Y^k,
A_W=sum_(k=0)^(r-1) a_kY^k,
B_W=sum_(k=0)^(r-1) b_kY^k.                         (QTA1)
```

Then

```text
f_0=E q_bar,       l_0=Delta_inf,
gcd(f_0,l_0P_cl)=1.                                 (QTA2)
```

Suppose the coefficients below degree `k` of `W_vee` and `S` have already
been reconstructed. Put

```text
C_k^0=l_0 w_k^0
      +sum_(i=1)^k l_i w_(k-i)
      -sum_(i=1)^k f_i s_(k-i).                     (QTA3)
```

Let `rho_k` be the degree-less-than-`deg f_0` representative of

```text
rho_k=-C_k^0(l_0P_cl)^(-1) mod f_0.                 (QTA4)
```

For every `0<=k<r`, a corrected square requires

```text
deg rho_k<=1,       rho_k=t a_k+b_k,                (QTA5)
s_k=(C_k^0+l_0P_cl rho_k)/f_0.                      (QTA6)
```

Conversely, these recurrences uniquely determine every coefficient of
`A_W,B_W` and the first `r` coefficients of `S`. Afterward the remaining
unit equation is the deterministic exact-division and degree check

```text
S=(L W_vee-EY^N_sq)/F.                              (QTA7)
```

Thus neither correction polynomial remains a solver variable. Any
`rho_k` of degree at least two is an exact endpoint rejection certificate.
