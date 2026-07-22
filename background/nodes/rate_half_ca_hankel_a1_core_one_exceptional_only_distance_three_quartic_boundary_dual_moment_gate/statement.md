# `A=1` distance-three quartic boundary dual-moment gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_boundary_crt_reconstruction`

Retain the exceptional CRT reconstruction and put `d=deg A=2e`. For a root
`a` of `D_k`, define

```text
V_a(z)=
 [sum_i D_i(a)N_i(a)L_i(z)]/(z-xi_k),       deg V_a<=e-2. (QBM1)
```

Then the degree-four collapse is equivalent to the following explicit
vector-valued moment system:

```text
M_j(z)=sum_(A(a)=0)
 a^(j+1)(a-s)(a-x_0)B(a)q_e(a)^2V_a(z)=0,

                         0<=j<=2e-6.                 (QBM2)
```

There are exactly `2e-5` such polynomial identities, each of `z`-degree at
most `e-2`. Equivalently, without splitting the pair locators, let
`R_k=F[X]/(D_k)` and let `V_k` be the quotient in `(QBM1)` computed in
`R_k[z]`. Then

```text
M_j(z)=sum_k Tr_(R_k/F)(
 X^(j+1)(X-s)(X-x_0)B(X)q_e(X)^2V_k(z)
)=0.                                                     (QBM3)
```

Within the active-row design, `(QBM2)` is equivalent to the global quartic
weld. When it holds, the unique degree-at-most-four polynomial in `X`
interpolating

```text
q_e(a)^2 V_a(z)/C(a)                                  (QBM4)
```

is `Omega(z;X)`. Thus the live saturated branch can be attacked through
streaming pair traces and exact zero certificates; neither the degree-
`6e+3` active locator nor all external quartic cofactors need be
materialized for this gate.

No independence among the specialized equations in `(QBM2)`, projective
line decomposition, or rank bound on the five surviving coefficients is
asserted. On the deterministic random `e=3,F_97` control, the sole index
`j=0` gives a nonzero polynomial of degree one, exactly detecting the
degree-five exceptional interpolant.
