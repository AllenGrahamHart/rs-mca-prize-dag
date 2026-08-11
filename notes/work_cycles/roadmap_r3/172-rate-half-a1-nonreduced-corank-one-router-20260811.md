# Cycle 172: rate-half `A=1` nonreduced corank-one router (2026-08-11)

At an unshared nonreduced correction the divided-row image starts with the
two jets `kappa_2,kappa_3`, while the regular determinant has order four.
If the specialized regular block has corank one, the full contracted-source
kernel has dimension two. Its minimal locator has degree `d-1`, and because
`x_*` lies outside `U_0`, the primitive kernel is exactly
`(X-x_*)P_tau`; simplicity is automatic. The symmetric Schur complement
has order four, so a vector whose image starts in order two has self-pairing
in order at least four:

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
new assumptions:         explicit local corank-one profile
```

Any surviving unshared nonreduced packet must now have regular corank at
least two. A quotient-root collision is contained in that higher-corank
locus. The abstract Smith type `[2,2]` shows why this residual profile needs
a separate argument.
