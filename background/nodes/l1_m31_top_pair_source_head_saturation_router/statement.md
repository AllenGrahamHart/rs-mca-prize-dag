# M31 top-pair source-head saturation router

- **status:** PROVED
- **closure:** proof
- **requires:** `l1_m31_rank7_dense_top_decorated_shift_pair_router`,
  `l1_m31_top_neighbor_core_shadow_payment`
- **source contract:** upstream proper-`G` normal form at `b9665145`

Retain the deployed source parameters

```text
g=354972,  sigma=282544,  w=67447,
d=g-w=287525,  k=d-sigma=4981,  t=k-1=4980,
N=1053557,  m=72428,       M0=2157929.
```

For every proper zero-excess member use the canonical source data

```text
G_i | P,       Q_i=P/G_i,       f_i=Q_i b_i,
deg b_i < deg G_i-w,
H_i=gcd(L_0,Y-f_i),       deg H_i=deg G_i,
L_S | H_i,       f_i=f_*+L_S a_i,       deg a_i<k.
```

Put

```text
gamma_i=[X^(d-1)]f_i.
```

For every top pair `i,j`, whose combined residual supports intersect in
exactly `t` points, let

```text
C_ij=gcd(Q_i,Q_j),       K_ij=gcd(H_i,H_j).
```

Then the source determinant is saturated:

```text
A_i^G b_j-A_j^G b_i=(gamma_j-gamma_i)K_ij,          (HS1)

G_i=J_ij^G A_i^G,       G_j=J_ij^G A_j^G.
```

In particular `gamma_i!=gamma_j`, and the residual difference is

```text
a_j-a_i=(gamma_j-gamma_i)
          C_ij (K_ij/L_S).                          (HS2)
```

The monic product in `(HS2)` is exactly the degree-`t` common-support
locator.

Consequently every fixed head fiber is independent in the top-pair graph.
The constant-weight Cauchy bound gives

```text
#{i:gamma_i=gamma} <=458812                         (HS3)
```

for every field value `gamma`. Any violating proper family therefore uses
at least five head values, and at least

```text
M0-458812=1699117                                   (HS4)
```

members have `gamma_i!=0`, equivalently `deg f_i=d-1` and
`deg b_i=deg G_i-w-1`.

Moreover the original dense-top anchor, with no condition on its own head,
forces at least

```text
215793*4980/15=71643276
```

distinct `(core, neighbor-head-value)` pairs. Separately, one nonzero-head
anchor has at least `107897` top neighbors. It forces at least `2238863`
degree-`4979` cores and at least `35821804` colored core pairs.

## Scope

The theorem is a source-sensitive coloring and spread reduction. It does not
bound the number of head values, aggregate their fibers, assign them to a
first owner, prove the local cap `215792`, or pay `Q=147595`.
