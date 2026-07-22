# `A=1` distance-three quartic boundary torus-kernel reduction

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_boundary_dual_moment_gate`

Retain the pair-Lagrange and dual-moment notation. Define the nonzero labels

```text
theta_i=c_i xi_i/lambda_i
       =xi_i P_Z(xi_i)/lambda_i^2 in F^*.             (QTK1)
```

For `i!=k`, put

```text
W_ik(z)=L_i(z)/(z-xi_k),       deg W_ik<=e-2.         (QTK2)
```

At either root `a` of `D_k`, the exceptional CRT quotient has the
derivative-free form

```text
V_a(z)=-q_e(a) sum_(i!=k)
 theta_i D_i(a)^2 W_ik(z)/(xi_i-xi_k).               (QTK3)
```

For `0<=j<=2e-6`, define fixed coefficient polynomials

```text
A_ji(z)=sum_(k!=i) W_ik(z)/(xi_i-xi_k) *
 Tr_(R_k/F)(
  X^(j+1)(X-s)(X-x_0)B(X)q_e(X)^3D_i(X)^2
 ),                                                     (QTK4)

R_k=F[X]/(D_k).
```

Then the dual moments factor exactly as

```text
M_j(z)=-sum_i theta_i A_ji(z).                        (QTK5)
```

Let `T` be the matrix whose columns are indexed by `i` and whose rows are
the coefficients `[z^ell]A_ji`, with

```text
0<=j<=2e-6,       0<=ell<=e-2.                       (QTK6)
```

It has `(2e-5)(e-1)` rows and `e` columns. Every exact external design must
satisfy

```text
T theta=0 for one theta in (F^*)^e.                  (QTK7)
```

Consequently either of the following is an exact exclusion certificate for
a proposed pair-Lagrange packet before reconstructing external cofactors:

1. `rank T=e`; or
2. `ker T` contains no vector with every coordinate nonzero.

The second condition has an exact rank-only form on the official field,
where `q>e`. A torus kernel vector exists if and only if

```text
rank T<e and rank(T with column i deleted)=rank T
for every i.                                           (QTK8)
```

Thus one full-rank certificate or one coloop column excludes the packet;
there is no need to enumerate kernel vectors.

The matrix depends only on the support partition, internal slopes,
`lambda_i`, and the resulting `q_e`; `P_Z` enters only through the torus
vector `(QTK1)`. At `e=3`, `T` has only two rows and cannot have rank three.
The deterministic `F_97` control has rank two after every column deletion,
so its one-dimensional kernel does meet the torus.
Deterministic subgroup controls at `(e,N,p)=(4,40,241),(5,48,97),
(7,64,193)` have full ranks `4,5,7`, respectively. These controls prove
that the exclusion is nonvacuous, not that every admissible or official
packet has full rank.

No universal rank theorem, external-design nonexistence, or projective-line
decomposition is asserted. Proving that every official candidate has full
rank, or has torus-free kernel, would exclude the remaining generic
saturated distance-three branch.
