# `A=1` exceptional non-MDS annihilating-pair router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_mds_schur_router`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_residue_self_dual_algebra`

Let `U_q` be the dimension-`e` normalized exceptional coefficient space in
the reduced algebra

```text
R_A=F_field[X]/(A) = product_(A(a)=0) F_field.
```

If the normalized exceptional code is not MDS, then there are a partition
of the exceptional roots into `I disjoint_union J`, with `|I|=|J|=e`, and
linearly independent nonzero elements `u,v in U_q` such that

```text
u|_I=0,       v|_J=0,       uv=0 in R_A.             (HNA1)
```

Equivalently,

```text
supp(u) subset J,       supp(v) subset I.             (HNA2)
```

Let `u_hat,v_hat` be the canonical degree-below-`2e` representatives and
put

```text
D_u=gcd(A,u_hat),       D_v=gcd(A,v_hat).
```

Then

```text
deg D_u>=e,       deg D_v>=e,       lcm(D_u,D_v)=A.  (HNA3)
```

Consequently exactly one of the following certificate classes applies:

```text
max(deg D_u,deg D_v)>=e+1;                           (excess zero)
deg D_u=deg D_v=e, gcd(D_u,D_v)=1, D_uD_v=A.         (exact halves) (HNA4)
```

Write the annihilators in the normalized coefficient basis as

```text
u=sum_(i=0)^(e-1) lambda_i p_i,
v=sum_(i=0)^(e-1) nu_i p_i,
p_i=q_(i+1)/q_1 mod A,
```

and define

```text
H_lambda=sum_i lambda_i q_(i+1),
H_nu=sum_i nu_i q_(i+1).
```

Since `q_1` is a unit modulo `A`, the same gcd locators are obtained without
quotient inversion:

```text
D_u=gcd(A,H_lambda),       D_v=gcd(A,H_nu).          (HNA5)
```

More generally, let `r_I,r_J` be the ranks of the two `e`-column
restrictions. Weighted self-duality gives

```text
r_I=r_J=e-d,       1<=d<=floor(e/2).                 (HNA6)
```

The subspaces

```text
U_I={u in U_q:u|_I=0},       U_J={v in U_q:v|_J=0}
```

both have dimension `d`, have disjoint support, and satisfy

```text
U_I U_J={0} in R_A.                                  (HNA7)
```

Thus deficiency `d` supplies `d^2` annihilating numerator pairs, all with
the same two mandatory degree-`e` zero locators.

Thus the non-MDS branch can be attacked by excluding an annihilating pair
inside `U_q`; no enumeration of its `binom(2e,e)` maximal minors is needed.
This theorem does not exclude such a pair from the official split-incidence
space.
