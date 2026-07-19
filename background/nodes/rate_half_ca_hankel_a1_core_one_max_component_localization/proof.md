# Proof

The core-stratified router gives all identities in `(C1M2)`, exact separation
rank `sr(Qbar)=e+1`, at least `T-Delta=T-1` completely split residual slope
fibers, and at least `(N-1)-eta=(N-1)-e=14m` saturated residual domain fibers.

## 1. Exact component defects

For each component, let `I_i` count distinct zeros on `(D\S) x Z`, and put

```text
D_i=T*r_i-I_i,       C_i=(N-1)e_i-I_i,
E=sum_i I_i-I.                                          (1)
```

Grid-line root bounds make `D_i,C_i` nonnegative. The exact residual
incidence identities give

```text
sum_i D_i=O-E<=1,       sum_i C_i=C-E<=e.               (2)
```

In particular `0<=E<=O`. Since `N-1=16m-1=8e+7` and `T=4e+1`, define

```text
z_i=r_i-2e_i.
```

Direct subtraction gives

```text
C_i-D_i=5e_i-T*z_i.                                    (3)
```

If `z_i<=-1`, then `(3)` is at least `T+5e_i>e`, contrary to
`C_i-D_i<=C_i<=e`. Thus every `z_i` is nonnegative. On the other hand,

```text
sum_i z_i=d-2e=1.                                      (4)
```

Exactly one component has `z_i=1`, and all others have `z_i=0`. This proves
`(C1M4),(C1M5)`.

For a residual component, `(3)` becomes

```text
C_i-D_i=5e_i.
```

Since `D_i>=0`, summing away from the unique component and using `(2)` gives

```text
5b<=sum_(i!=*)C_i<=C-E<=e.
```

This proves `(C1M6)`.

## 2. Dominant separation rank

Write

```text
Qbar=Q_* G,       deg_(U,V)G=b.
```

Separation rank is submultiplicative under biform multiplication, while a
form of parameter degree `b` has separation rank at most `b+1`. Therefore

```text
e+1=sr(Qbar)<=sr(Q_*)sr(G)<=sr(Q_*)(b+1),
```

which proves `(C1M7)`. At the official row, `e=2^38-1` is `3 modulo 5`, so
the constants in `(C1M8)` follow by exact division. The last ratio is
strictly greater than four, hence its ceiling is at least five. Separation
rank two is precisely the cross-multiplied equation of two rational maps
after common factors are removed, so the rank bound also excludes separated
pullbacks.

## 3. Squarefree and split fibers

Every component has positive bidegree by the residual router. A repeated
geometric component would specialize with multiplicity at every slope where
its full positive `X`-degree is retained. Its leading coefficient has
parameter degree at most `e_i`, while there are `T-1>e_i` clean split slopes.
At one of them the component retains positive degree, contradicting
squarefreeness of the completely split `Qbar_gamma`. Thus `Qbar` is
geometrically squarefree.

At each of the `T-1` clean slopes, the squarefree product `Qbar_gamma` has all
`d` roots in `D\S`; every component therefore splits with disjoint root sets.
At each saturated residual domain row, `Qbar(U,V;x)` has all `e` roots in
`Z`, and the same componentwise conclusion holds in the parameter direction.
The router supplies at least `14m` such rows. This proves `(C1M9),(C1M10)`
and completes the proof. QED.
