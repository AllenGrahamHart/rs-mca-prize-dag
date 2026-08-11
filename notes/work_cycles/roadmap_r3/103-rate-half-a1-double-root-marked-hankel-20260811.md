# Cycle 103: double-root marked Hankel determinant gate (2026-08-11)

## Cycle pins

```text
our start:       cd155812a
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         none
critical open:   28
```

## Hankel-side interface

The generic row-product formula for the Cycle-102 resultant reuses the
same cube identity and is not independent enough to close a packet. The
primitive-kernel cofactor formulas provide the missing concrete interface:

```text
core-free: det stack(M_0,nu(x))=D_0 Q(x);
core-one:  det(M_1+tau nu(x)nu(x)^T)=tau D_1 Q(x)^2.
```

At the core-one `u=4` double root, the second determinant is exactly
`tau c^2 D_1 g_*^2 S_B^6`, where `g_*` is the squarefree degree-`e-6`
supported factor and `S_B` is quadratic. This is now an explicit Hankel
determinant factorization problem rather than an abstract non-cube request.

## Burn-down

```text
result:                  EXPOSED exact marked-Hankel determinant gates
DAG delta:               +1 PROVED leaf, +3 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next use the Vandermonde/source decomposition of the marked determinant to
test whether the residual linear/quadratic cube factors are compatible with
the evaluation-word weights. Do not infer positivity from the signed
Cauchy--Binet expansion.
