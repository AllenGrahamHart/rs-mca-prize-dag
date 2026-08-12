# Cycle 174: rate-half `A=1` nonreduced higher-corank Smith router (2026-08-12)

**Cycle-177 correction.** `P_tau(x_*)!=0` is not automatic from
`x_* notin U_0`; the compressed minimal recurrence need not split on the
original source. The three-profile theorem remains valid under its explicit
`r>=2` hypothesis away from the full collision
`P_tau(x_*)L_tau(x_*)=0`. Corank one has a separate compressed-recurrence
collision route.

The unshared nonreduced obstruction is now finite away from quotient-root
collision. If `r` is the regular specialized corank, the source locator
factorization is

```text
U_tau=P_tau L_tau,       deg P_tau=d-r,
deg L_tau=r-1.
```

Thus collision is `P_tau(x_*)L_tau(x_*)=0`. Without collision, symmetric
Smith valuation at determinant order four leaves exactly three nonzero-jet
profiles:

```text
[1,3]      with kappa_2=0, kappa_3!=0;
[2,2]      with kappa_2!=0;
[1,1,2]    with kappa_2!=0.
```

The corank-four profile `[1,1,1,1]` forces both jets to vanish.

```text
result:                  PROVED three-profile higher-corank router
DAG delta after repair:  +1 PROVED leaf, 1 req edge
critical status delta:   none
compute:                 five Smith partitions; no Modal spend
new assumptions:         r>=2 and noncollision for the conclusion
```

Explicit diagonal germs realize all three residual Smith/jet behaviors, so
Smith arithmetic is exhausted. The next attack is the quotient-root
collision and then the retained source/Hankel geometry inside the three
noncollision profiles.
