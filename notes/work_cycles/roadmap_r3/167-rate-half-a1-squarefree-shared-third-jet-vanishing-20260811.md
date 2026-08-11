# Cycle 167: rate-half `A=1` squarefree shared third jet vanishes (2026-08-11)

At a shared root the regular symmetric Hankel block has corank one and
determinant order three. The Cycle-166 image starts as

```text
M u=z^2 kappa_tau nu(x_*)+O(z^3).
```

A corank-one symmetric Schur-complement lemma forces `u^TMu` to order at
least three. Its order-two coefficient is
`kappa_tau U_tau(x_*)`; the padded root is simple, so `U_tau(x_*)!=0`.
Therefore

```text
kappa_tau=0,
D_1|F_i for every i,
Smith_tau(D_1)=[3].
```

```text
result:                  PROVED squarefree shared-jet vanishing
DAG delta:               +1 PROVED leaf, 4 req edges
critical status delta:   none
compute:                 tiny Schur replay only; no Modal spend
new assumptions:         S_B squarefree; sharing allowed
```

The cubic quotient now extends through all squarefree shared corrections.
The double-root local exception is reduced to nonreduced `S_B`.
