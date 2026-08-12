# Cycle 176: rate-half `A=1` Pade-Bezout collision Smith router (2026-08-12)

The Pade determinant identity now has a complete local-module refinement:
the regular Hankel block is congruent to `Bez(Q,P_F)`, whose cokernel is
the contact algebra `O_tau[X]/(Q,P_F)`. At the exact nonreduced collision,
Hensel reduction leaves the quadratic presentation

```text
q=y^2+c_1y+c_0,       P_F=b+ay mod q,
ord(b,c_0,c_1,a)=(2,6,>=3,>=1).
```

Its multiplication matrix proves exact regular corank two and the
one-scalar router

```text
[z]a!=0:       Smith [1,3],
[z]a=0:        Smith [2,2].
```

```text
result:                  2 PROVED nodes; exact collision reduced to one jet
DAG delta:               +2 PROVED leaves, 4 req edges, 2 evidence edges
critical status delta:   none
compute:                 2304 Gram, 348 Smith, and 14 local fixture checks
new assumptions:         finite degree-preserving locator chart
```

The earlier abstract corank-three and corank-four cases are empty in the
geometric collision. The next attack is the scalar `[z]a`, equivalently
the first parameter jet of the `y`-coefficient of `P_F mod q`, using the
global source or split-biform identities.
