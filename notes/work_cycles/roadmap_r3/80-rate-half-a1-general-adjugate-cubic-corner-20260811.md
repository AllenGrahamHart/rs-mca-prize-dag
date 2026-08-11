# Cycle 80: general core-one adjugate and cubic corner (2026-08-11)

## Cycle pins

```text
our start:       28b0485b3
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   38 PRs; no new overlap
critical open:   28
```

## General adjugate

Every core-one contraction is a square symmetric middle-Hankel pencil. If
`q` is its primitive degree-`e` kernel vector, then

```text
adj M=D q q^T,       deg D=Delta=d-2e.
```

The common cofactor factor is exactly the regular Kronecker determinant.
The local chain

```text
pole length <= root omission <= rank loss <= ord(D)
```

makes the pushed-forward pole divisor a factor of `D`. The proved leaf is
`rate_half_ca_hankel_a1_core_one_general_middle_adjugate_factorization`.

## First surviving corner

At `e=floor(16m/13)=169155635042`, the carrier lower bound equals maximal
slack. Thus every possible failure has

```text
ell=126866726279,       T=rho+2,
Delta-3<=p<=O<=sum c_gamma<=Delta.
```

Consequently

```text
D=P_p E_3,       deg E_3<=3,
T-Delta=2e+3=338311270087 clean split fibres.
```

The proved leaf is
`rate_half_ca_hankel_a1_core_one_first_surviving_cubic_residual_corner`.

## Burn-down

```text
result:                  NARROWED first core-one degree to cubic residual
DAG delta:               +2 PROVED leaves, +5 req edges, +2 ev edges
critical status delta:   none
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next classify the degree-at-most-three residual factor jointly with the
`2e+3` clean fibres and the exact adjugate identity. This is a finite-defect
algebraic target; no large computation is indicated.
