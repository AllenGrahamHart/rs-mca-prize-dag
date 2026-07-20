# Budget-three deleted-pair torsion cyclotomic-norm decomposition

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_even_jacobi_norm_router`

Let `M` be a positive power of two and put

```text
J(w)=J_M^(-1/4,-1/2)(w),
H_M(z)=z^M J((z+z^(-1))/2).                         (TCN1)
```

The Laurent expression in `(TCN1)` is a reciprocal polynomial of degree
`2M` over `Q`. With the standard Jacobi, Chebyshev, and resultant
normalizations, define

```text
R_-=Res_w(J(w),T_(2M)(w)),
R_+=Res_w(J(w),U_(2M-1)(w)).                        (TCN2)
```

Then the exact norm identities are

```text
R_-^2=2^(2M(2M-1)) Res_z(Phi_(8M)(z),H_M(z)),       (TCN3)

R_+^2=2^(2M(2M-1))
       Res_z((z^(4M)-1)/(z^2-1),H_M(z)).            (TCN4)
```

Since `M` is dyadic, the second norm has the exact tower decomposition

```text
Res_z((z^(4M)-1)/(z^2-1),H_M)
 =product_(4<=d<=4M, d a power of two)
    Res_z(Phi_d,H_M).                               (TCN5)
```

All coefficients of `J` and `H_M` have denominator a power of two.
Consequently, for every odd prime `p`, rational `p`-adic valuation gives

```text
v_p(Res(Phi_(8M),H_M))=2v_p(R_-),                  (TCN6)

sum_(4<=d<=4M, d dyadic) v_p(Res(Phi_d,H_M))
 =2v_p(R_+).                                        (TCN7)
```

At the official value `M=2^35`, the minus branch is one real cyclotomic norm
at order `2^38`; the plus branch is the `36`-level tower at orders
`2^2,...,2^37`. Thus CR-002-J0 may screen odd official characteristics by
modular cyclotomic norms and may short-circuit the plus branch level by
level. It need not form either primitive integer resultant.

There is also an exact trace-polynomial form of the plus tower. If
`s=log_2 M`, then

```text
U_(2M-1)(w)=2M product_(j=0)^s T_(2^j)(w),           (TCN8)

R_+=(2M)^M product_(j=0)^s
       Res_w(J_M^(-1/4,-1/2),T_(2^j)).              (TCN9)
```

For `m=2^j` and `d=4m`, each trace factor is paired with one tower level by

```text
Res_z(Phi_d,H_M)
 =Res_w(J,T_m)^2/2^(2M(m-1)).                       (TCN10)
```

Hence an odd prime divides `R_+` exactly when it divides at least one of the
`36` trace resultants in `(TCN9)`. The largest torsion polynomial in that
list is `T_M`, of degree `M`, rather than `U_(2M-1)`, of degree `2M-1`.

The minus branch has a matching quadratic trace split. In
`K=Q(theta)`, `theta^2=2`, put

```text
S_-=Res_w(J,theta T_M-1),
S_+=Res_w(J,theta T_M+1).                            (TCN11)
```

Then

```text
T_(2M)=(theta T_M-1)(theta T_M+1),
R_-=S_-S_+,
Norm_(K/Q)(S_-)=(-1)^M R_-.                         (TCN12)
```

For official `M=2^35`, the sign in `(TCN12)` is positive. Every official
characteristic in this branch contains `theta`, so `R_-` may be screened by
the two degree-`M` modular resultants in `(TCN11)`. This lowers the largest
minus torsion degree from `2M` to `M` without changing total coverage.

This theorem supplies an exact compressed certificate interface. It does not
prove that any official characteristic is absent from either norm.
