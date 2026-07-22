# XR prize arbitrary-rank dual-projective support router

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_prize_arbitrary_w_trade_circuit_segre_router`,
  `xr_prize_arbitrary_w_rank_two_dual_plane_support_router`,
  `xr_prize_arbitrary_w_rank_two_received_pair_router`

Let a support-minimal row-scaling circuit have trade rank `r>=2`, active
arity `t`, row-space basis `F_1,...,F_r`, and coefficient vectors
`c_i in F^r`. Put `X` equal to the union of its row supports. Then

```text
L=<F_1,...,F_r> subset (W|X)^perp,                   (AR1)
r+2<=t<=2r+1.                                        (AR2)
```

The basis has no common zero on `X`, so it defines a projective map

```text
Phi:X->P^(r-1),       Phi(x)=[F_1(x):...:F_r(x)].     (AR3)
```

Every row support is the complement of one projective hyperplane section:

```text
lambda_i=sum_j c_(ij)F_j,
S_i=X\{x:c_i dot Phi(x)=0}.                          (AR4)
```

The coefficient-slope columns

```text
z_i=(c_i,gamma_i c_i) in F^(2r)                      (AR5)
```

form a projective circuit: they have rank `t-1`, their unique dependence has
all coefficients nonzero, and every proper subset is independent. For `r>=2`
any projective coefficient direction `[c_i]` occurs at most twice. A repeated
pair has a common row support and routes to the local-tangent basis/flat owner.

Received-pair interaction is equally uniform. The vector

```text
theta=(<F_j,b>,<F_j,q>)_(j=1,...,r) in F^(2r)        (AR6)
```

annihilates every `z_i`, so its allowed interaction space has dimension

```text
2r-t+1.                                              (AR7)
```

At maximal circuit arity `t=2r+1`, `theta=0` and the whole dual space `L`
annihilates both received directions. At smaller arity, `(AR7)` is the exact
interaction chamber.

Conversely, a dual `r`-space, a projective circuit `(AR5)`, certified selected
blocks containing the supports `(AR4)`, and an interaction vector in the
annihilator reconstruct the trade-row constraints.

This theorem gives one schema for every remaining higher-rank first-core
record. It does not count projective maps/hyperplane arrangements or prove
the aggregate P-A bound.
