# Cycle 191: rate-half shape-A norm concentration (2026-08-12)

With all ordinary companions removed, the split biform is the single
shape-A large factor. The global off-line padding degree is `e-7`, while
the squarefree heavy-row form already gives `e-7` distinct slopes whose
padding factor contains `x_*`. Degree equality therefore forces every
off-line padding root to equal `x_*`:

```text
product_delta R_delta=(X-x_*)^(e-7).
```

Multiplying the proved all-excess fiber factorizations now gives the exact
global norm

```text
product_delta G(delta,X)
 =c L_U0(X)^(e-2)(X-x_*)^(e-7)T(X),
T=product_delta H_delta,
deg T=e-sum_delta q_delta<=e.
```

The polynomial `T` is coprime to `L_U0` and its values on every classified
row are the known tangent products after removing the two displayed power
factors. The remaining shape-A norm problem is therefore one
degree-at-most-`e` source residual, not a family of padding choices.

```text
start:                   466cd4d95
result:                  NARROWED, shape A has one concentrated excess norm
DAG delta:               +1 PROVED node, +5 req edges, +1 ev edge
critical status delta:   none
upstream terminal delta: candidate Lane-T PR #1161 extension
delta-star movement:     none
compute:                 exact local replay only; no Modal spend
next route action:       couple T to the scalar weld and source/Pade syzygy
```
