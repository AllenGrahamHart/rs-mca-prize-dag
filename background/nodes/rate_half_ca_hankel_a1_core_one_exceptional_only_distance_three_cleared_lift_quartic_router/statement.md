# `A=1` distance-three cleared-lift quartic router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_pair_lagrange_normal_form`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_external_split_design_saturation`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_calibrated_conic_kernel_lift_normal_form`

Retain the exact distance-three design and the notation of the calibrated
kernel-lift normal form. Put

```text
R(z;X)=R_0(z)+XR_1(z)+X^2R_2(z),
E_i(X)=A(X)B(X)/D_i(X),       rho_i=P_Z'(xi_i)/P_Z(xi_i),
c_i=P_Z(xi_i)/lambda_i.                                      (CLQ1)
```

Define the degree-at-most-two polynomial

```text
U_i(X)=
 [c_iD_i(X)rho_i-partial_z R(xi_i;X)]/I'(xi_i)               (CLQ2)
```

and

```text
N_i(X)=E_i(X)U_i(X)
 -c_iD_i(X)partial_zQ(xi_i;X)/(lambda_i I'(xi_i)).            (CLQ3)
```

Then

```text
deg E_i=2e+1,       deg N_i<=2e+3,
J_x(xi_i)=N_i(x)/E_i(x)                              (x in C). (CLQ4)
```

Let `L_i` be the internal Lagrange basis. The kernel lift is reconstructed
without coefficientwise division by

```text
J_x(z)=s_xI(z)+sum_i [N_i(x)/E_i(x)]L_i(z).                    (CLQ5)
```

Consequently the following is a polynomial biform:

```text
F(z;X)=A B q_e R
 +I [(A B)^2 I+q_e sum_i D_iN_iL_i],                           (CLQ6)

deg_z F<=2e,       deg_X F<=4e+6.                              (CLQ7)
```

At every active outside row,

```text
F(z;x)=(A(x)B(x))^2H_x(z).                                    (CLQ8)
```

For an external slope `gamma`, let `G_gamma^X` be its monic degree-`2e+1`
active-row locator and put

```text
K_gamma(X)=C(X)/G_gamma^X(X),       deg K_gamma=4e+2.           (CLQ9)
```

There is a unique nonzero polynomial `T_gamma` such that

```text
F(gamma;X)=K_gamma(X)T_gamma(X),       deg T_gamma<=4.         (CLQ10)
```

The slopewise quartics are fibers of one global quartic biform. There is a
unique `Omega(z;X)` satisfying

```text
F(z;X)Q(z;X)
 =(A(X)B(X))^2q_e(X)P_Z(z)+C(X)zI(z)^2Omega(z;X),    (CLQ11)

deg_z Omega<=e-2,       deg_X Omega<=4.               (CLQ12)
```

If `ell_gamma=[X^(2e+1)]Q(gamma;X)`, then

```text
Omega(gamma;X)=
 ell_gamma T_gamma(X)/(gamma I(gamma)^2).            (CLQ13)
```

Thus clearing the conic kernel lifts leaves only four units of degree beyond
the exact external nonincidence locator, and the resulting quartics lie on
one polynomial curve of degree at most `e-2` in their five-dimensional
coefficient space. This curve is not asserted to be a projective line, and
the quartics are not asserted to be fixed or domain-split. The exact `e=1`
Hankel-design fixture attains degree four, and each of its three residual
quartics has only the two exceptional roots in the base field. The local
sharpness calculation does not satisfy the official `e>=3` degree step used
to extract the factor `z` in `(CLQ11)`.
