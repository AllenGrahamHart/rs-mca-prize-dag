# Cycle 166: rate-half `A=1` squarefree shared third-jet gate (2026-08-11)

At a simple root shared by `g_*` and `S_B`, the supported and correction
contacts may be distinct normalized branches. Their orders therefore cannot
be added automatically in the fixed base polynomial. The correction branch
always gives `z^2|F_0`; define

```text
kappa_tau=(F_0/z^2) mod z.
```

The exact recurrence gives

```text
(F_i/z^2) mod z=x_*^i kappa_tau,
D_1|F_i for all i       iff kappa_tau=0.
```

On the vanishing branch the cubic quotient extends and the local Smith type
is `[3]`. On the nonvanishing branch the canonical image has exact order two.

```text
result:                  PROVED one-scalar shared-root gate
DAG delta:               +1 PROVED leaf, 4 req edges
critical status delta:   none
compute:                 tiny truncated-series replay; no Modal spend
new assumptions:         S_B squarefree; shared roots allowed
```

The squarefree shared branch is now an explicit third-jet decision rather
than an unstructured failure of the separated proof.
