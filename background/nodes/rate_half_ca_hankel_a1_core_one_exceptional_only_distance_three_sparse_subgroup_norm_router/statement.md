# `A=1` core-one distance-three sparse subgroup-norm router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_resultant_power_equivalence`

Retain the pair-Lagrange data and put

```text
I(z)=product_i(z-xi_i),
R_D(z)=Res_X(X^N-1,Q(z;X)),
H(z)=Res_X(C,Q),       r=2e+1.                         (SSN1)
```

For a root `a` in the matched pair `D_i`, define

```text
c_a=B(a)(lambda_i/xi_i)(A/D_i)(a),
Delta_0=product_i(-xi_i),
Delta_i=product_(j!=i)(xi_i-xi_j),                    (SSN2)

kappa_0=
 [product_(a in R_A)c_a] [product_(t in T)A(t)] /
 [Delta_0^3 product_i Delta_i^2].                     (SSN3)
```

Every displayed factor is nonzero. Without assuming an external design, the
full subgroup norm has the exact sparse factorization

```text
z R_D(z)=
 kappa_0 Q(z;s)Q(z;x_0)(z I(z))^r H(z).              (SSN4)
```

Consequently the external split design exists if and only if the row
squarefreeness gate from the dependency holds and there is a monic squarefree
split degree-`3e` polynomial `P_Z` with

```text
z R_D(z)=
 kappa_0 L Q(z;s)Q(z;x_0)
 (z I(z)P_Z(z))^r,                                   (SSN5)
```

where `L=Res_X(C,[z^e]Q)`. The factor

```text
P_sup(z)=z I(z)P_Z(z)                                (SSN6)
```

is exactly the monic locator of the exceptional, internal, and external
supported slopes and has degree `4e+1`.

Equation `(SSN4)` is an implementation router. It reconstructs the active-row
norm, up to the printed scalar, by exact division:

```text
H(z)=
 z R_D(z)/[kappa_0 Q(z;s)Q(z;x_0)(zI(z))^r].         (SSN7)
```

Thus a classifier may work against the sparse binomial `X^N-1` and two
degree-`e` boundary-row forms. It need not construct the degree-`6e+3`
locator `C` or multiply its row evaluations merely to obtain `H`.
