# `A=1` distance-three quartic internal-slice lambda-cube kernel

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_boundary_torus_kernel_reduction`

Retain the quartic boundary torus-kernel notation and assume `e>=4`. Put

```text
A_k=A/D_k,
r_k(X)=B(X)A_k(X)/[xi_k I'(xi_k)].                    (QLK1)
```

Thus at either root `a` of `D_k`,

```text
q_e(a)=lambda_k r_k(a).                               (QLK2)
```

For each `l` put `A^(l)=A/D_l`. For `k!=l`, let `Y_lk(X)` be the unique
polynomial of degree less than `2e-2` whose values at the roots of `A^(l)`
are

```text
Y_lk(a)=
  r_k(a)^3D_l(a)^2/[C(a)(xi_l-xi_k)^2],
       if D_k(a)=0;
  0,   if D_m(a)=0 with m not in {k,l}.               (QLK3)
```

The factor `C^(-1)` need not be constructed at degree `6e+3`; on every
root of `A`, use

```text
C^(-1)=N^(-1)X(X-s)(X-x_0)A'B mod A.                 (QLK4)
```

Every exact external design satisfies the theta-free internal-slice gates

```text
Y_l(X)=sum_(k!=l) lambda_k^3Y_lk(X),
deg Y_l<=4                         (1<=l<=e).          (QLK5)
```

Define the matrix `U` with columns indexed by `k` and rows indexed by

```text
(l,d),       1<=l<=e,       5<=d<=2e-3,
U_((l,d),k)=[X^d]Y_lk.                                 (QLK6)
```

There are `e(2e-7)` rows. The nonzero cube vector

```text
u=(lambda_1^3,...,lambda_e^3) in (F^*)^e             (QLK7)
```

must satisfy

```text
Uu=0.                                                 (QLK8)
```

Therefore full column rank or one coloop column of `U` excludes the entire
support/pair/internal-slope packet before any `lambda_i`, `P_Z`, first-jet,
or external-cofactor enumeration. If `U` has a deletion-stable deficient
kernel, the next exact condition is that its torus kernel meet the
coordinatewise cube subgroup; only then should `lambda_i` be reconstructed.

At `e=3`, `deg A^(l)=4`, so restriction modulo `A^(l)` cannot constrain a
quartic and `(QLK6)` has no rows. Deterministic subgroup controls at
`(e,N,p)=(4,40,241),(5,48,97),(7,64,193)` give matrix sizes and ranks

```text
4x4 rank 4,       15x5 rank 5,       49x7 rank 7,    (QLK9)
```

and every `Y_l` in the displayed control has maximal possible degree
`2e-3`. These are nonvacuity controls, not a universal rank theorem or
external-design census.
