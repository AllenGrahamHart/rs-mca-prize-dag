# Cycle 172: rate-half `A=1` nonreduced corank-one router (2026-08-11)

At an unshared nonreduced correction the divided-row image starts with the
two jets `kappa_2,kappa_3`, while the regular determinant has order four.
If the specialized regular block has corank one, its symmetric Schur
complement has order four. A vector whose image starts in order two then has
self-pairing in order at least four. When the padded root is simple,

```text
[z^2](u^TMu)=kappa_2 U_tau(x_*),
[z^3](u^TMu)=kappa_3 U_tau(x_*)
```

after the first jet is removed, so both jets vanish.

```text
result:                  PROVED simple corank-one jet elimination
DAG delta:               +1 PROVED leaf, 1 req edge
critical status delta:   none
compute:                 order-ledger replay only; no Modal spend
new assumptions:         explicit local corank-one and simple-root profile
```

Any surviving unshared nonreduced packet must now have regular corank at
least two or a collision with the specialized minimal locator. The abstract
Smith type `[2,2]` shows why this residual profile needs a separate argument.
