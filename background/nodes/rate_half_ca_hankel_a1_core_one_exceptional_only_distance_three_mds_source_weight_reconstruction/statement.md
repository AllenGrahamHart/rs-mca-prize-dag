# `A=1` core-one distance-three MDS source-weight reconstruction

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_external_split_design_saturation`

Retain the pair-Lagrange notation

```text
D_i(X)=(X-a_i)(X-b_i),
Phi(z)=product_i(z-xi_i)/Delta_0,
Delta_0=product_i(-xi_i),
L_i(z)=product_(j!=i)(z-xi_j)/Delta_i,
Delta_i=product_(j!=i)(xi_i-xi_j),                    (SWR1)
```

and the internal-fiber scalars

```text
Q(xi_i;X)=lambda_i B(X)A(X)/D_i(X).                  (SWR2)
```

The top `X`-coefficient is

```text
[X^r]Q=z q_bar(z),
q_bar(z)=sum_i(lambda_i/xi_i)L_i(z).                 (SWR3)
```

Let `Theta_2` be the nonzero quadratic moment from the exceptional crossing.
For `a in {a_i,b_i}`, define

```text
K_a=
 Theta_2 Delta_i /
 (Delta_0 A'(a) B(a)^2 (lambda_i/xi_i)(A/D_i)(a)).   (SWR4)
```

Every denominator in `(SWR4)` is nonzero. The unique source representations
of the exceptional and first-order moment vectors are exactly

```text
h_0=sum_(i=1)^e sum_(a in {a_i,b_i})(-xi_i K_a)c(a),

h_1=sum_(i=1)^e sum_(a in {a_i,b_i})K_a c(a)
    +sum_(t in T)
       Theta_2/(A(t)^2 B'(t)) c(t),                  (SWR5)
```

where `c(x)=(1,x,...,x^(2r))^T`.

Equivalently, at every slope `z`, the canonical source coefficient at an
exceptional root in pair `i` is

```text
beta_a+z alpha_a=K_a(z-xi_i).                        (SWR6)
```

At an external slope the unique minimum-weight circuit on
`R_A union T union G_z` has scalar

```text
Lambda_z=Theta_2 Phi(z)/q_bar(z).                    (SWR7)
```

Thus a distance-three classifier has no independent contracted source
weights or endpoint moment variables once the pair partition, internal
slopes, internal scalars, and `Theta_2` are fixed. It must reconstruct
`(SWR5)`.

There is also an exact converse at the contracted Hankel level. Suppose the
pair-Lagrange generator has the required `3e` external squarefree split
fibers and define `h_0,h_1` by `(SWR5)`. If `M(z)` is the middle Hankel matrix
of `h_0+z h_1` and `q(z)` is the coefficient vector of `Q(z;X)`, then

```text
M(z)q(z)=0                                           (SWR8)
```

identically. The exceptional rank is `r-1`, every internal and external
supported rank is `r`, and for one nonzero scalar `c_H`,

```text
adj M(z)=c_H z q(z)q(z)^T.                           (SWR9)
```

Consequently the two padded exceptional shifts obey the complete
first-order transversality gate. No independent Hankel-chain, rank, or
adjugate variables remain on this chart. The corrected reciprocal square,
the original endpoint lift/column-far condition, and exclusion of additional
split fibers are not supplied by this converse.
