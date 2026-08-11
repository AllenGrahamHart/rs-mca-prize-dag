# Cycle 168: rate-half `A=1` squarefree unified heavy-row gate (2026-08-11)

Cycle 167 extends the cubic quotient through every squarefree shared root.
The three-center source partition also shows that a correction center must
already be the unique possible padded-heavy center. Therefore, without any
supported/correction disjointness assumption,

```text
j=deg gcd(Lambda,g_*S_B^2)<=1,
G(t,x_*)=(g_*S_B^2/J)T_j,
T_j!=0,       deg T_j<=1,       gcd(T_j,S_B)=1.
```

At a correction root the exact row order is
`ord g_*+2-ord Lambda`. The complete augmented gate is still the one
barycentric test `H|R_lambda`, and passage gives the displayed nonzero row.

```text
result:                  PROVED unified squarefree constant/linear gate
DAG delta:               +1 PROVED leaf, 6 req edges
critical status delta:   none
compute:                 three-case valuation replay; no Modal spend
new assumptions:         S_B squarefree only
```

The squarefree double-root arm now has one global nonzero remainder wall.
Only nonreduced `S_B` lies outside the local heavy-row machinery.
