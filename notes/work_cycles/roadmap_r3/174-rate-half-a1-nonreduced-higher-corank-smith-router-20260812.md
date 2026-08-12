# Cycle 174: rate-half `A=1` nonreduced higher-corank Smith router (2026-08-12)

The unshared nonreduced obstruction is now finite away from quotient-root
collision. If `r` is the regular specialized corank, the source locator
factorization is

```text
U_tau=P_tau L_tau,       deg P_tau=d-r,
deg L_tau=r-1,           P_tau(x_*)!=0.
```

Thus collision is exactly `L_tau(x_*)=0`. Without collision, symmetric
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
DAG delta:               +1 PROVED leaf, 2 req edges
critical status delta:   none
compute:                 five Smith partitions; no Modal spend
new assumptions:         noncollision for the three-profile conclusion
```

Explicit diagonal germs realize all three residual Smith/jet behaviors, so
Smith arithmetic is exhausted. The next attack is the quotient-root
collision and then the retained source/Hankel geometry inside the three
noncollision profiles.
