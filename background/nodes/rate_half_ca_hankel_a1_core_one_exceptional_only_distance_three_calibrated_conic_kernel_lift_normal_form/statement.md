# `A=1` distance-three calibrated conic kernel-lift normal form

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_pair_lagrange_normal_form`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_external_split_design_saturation`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_complement_residue_rank_three_gate`

Retain the exact pair-Lagrange external design. Write

```text
I(z)=product_i(z-xi_i),       P_Z(z)=product_(gamma in Z_ext)(z-gamma),
G_x(z)=monic(Q(z;x)),         H_x(z)=P_Z(z)/G_x(z)                 (CKL1)
```

for each of the `6e+3` active outside rows `x`. Thus `deg G_x=e`,
`deg H_x=2e`, and every displayed divisor is squarefree. Put

```text
q_e(X)=[z^e]Q(z;X),       s_x=B(x)G_x(0)=A(x)B(x)/q_e(x).         (CKL2)
```

All `s_x` are nonzero. For the matched pair locator

```text
D_i(X)=X^2-sigma_i X+pi_i,
c_i=P_Z(xi_i)/lambda_i,                                      (CKL3)
```

let `R_0,R_1,R_2` be the unique polynomials of degree less than `e`
satisfying

```text
R_0(xi_i)=c_i pi_i,       R_1(xi_i)=-c_i sigma_i,
R_2(xi_i)=c_i.                                               (CKL4)
```

Then every scaled complement has the unique normal form

```text
s_x H_x(z)=R_0(z)+xR_1(z)+x^2R_2(z)+I(z)J_x(z),
deg J_x<=e.                                                   (CKL5)
```

The coefficient of `z^e` in `J_x` is exactly `s_x`. Moreover
`R_0,R_1,R_2` are linearly independent exactly when the pair locators
`D_1,...,D_e` span all quadratics, so they are independent on the surviving
generic rank-three branch.

The kernel lifts satisfy the exact global product identity

```text
product_(x in C)
 (R_0+xR_1+x^2R_2+I J_x)
   =kappa P_Z^(4e+2),       kappa=product_(x in C)s_x!=0.       (CKL6)
```

Thus the live saturated branch is not merely a conic in `F[z]/(I)`: it is a
conic with degree-`e` kernel lifts constrained by one exact perfect-power
identity. No bound on the span or row-interpolation degree of the `J_x` is
asserted.
