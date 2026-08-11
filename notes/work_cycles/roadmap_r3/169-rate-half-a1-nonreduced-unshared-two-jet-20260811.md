# Cycle 169: rate-half `A=1` nonreduced unshared two-jet gate (2026-08-11)

For `S_B=ell_tau^2` with `g_*(tau)!=0`, the fixed heavy row and regular
determinant have orders six and four. Correction contact uniformly forces
only `z^2|F_0`; without assuming how the two contact units lie above the
base, retain

```text
kappa_2=[z^2]F_0,       kappa_3=[z^3]F_0.
```

The exact recurrence gives

```text
[z^s]F_i=x_*^i kappa_s       (s=2,3),
D_1|F_i for all i            iff kappa_2=kappa_3=0.
```

Vanishing extends the cubic quotient and gives local Smith type `[4]`.

```text
result:                  PROVED two-scalar nonreduced local gate
DAG delta:               +1 PROVED leaf, 3 req edges
critical status delta:   none
compute:                 tiny truncated-series replay; no Modal spend
new assumptions:         one nonreduced correction root, unshared with g_*
```

The unshared nonreduced failure is now an exact two-jet decision rather than
an unstructured exception.
