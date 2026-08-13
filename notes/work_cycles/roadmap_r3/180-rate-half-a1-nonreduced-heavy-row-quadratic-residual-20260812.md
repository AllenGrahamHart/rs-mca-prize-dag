# Cycle 180: rate-half `A=1` nonreduced heavy-row quadratic residual (2026-08-12)

All `e-6` supported padded-heavy slopes divide the outside split-biform
row. Removing their squarefree factor leaves degree at most four. The
unsupported correction has exact order two, so its square form consumes
two more degrees:

```text
G(t,x_*)=g_*(t)S_B(t)T_2(t),
deg T_2=2,        T_2(tau)!=0.
```

The unique scalar weld must therefore pass one polynomial-remainder matrix
with modulus `g_*S_B` of degree `e-4`; only three quotient coefficients
remain.

```text
result:                  PROVED nonreduced heavy-row quadratic residual
DAG delta:               +1 PROVED leaf, 3 req edges, 1 evidence edge
critical status delta:   none
compute:                 15 exact polynomial checks; no Modal spend
new assumptions:         none
```

The next target is universal nonvanishing of this remainder matrix on the
unique connected weld vector, jointly with the two derivative-row jets.
