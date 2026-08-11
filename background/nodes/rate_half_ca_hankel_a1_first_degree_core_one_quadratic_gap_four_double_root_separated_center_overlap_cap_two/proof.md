# Proof

The heavy row is external to the contracted endpoint union. Concretely,
`g_*` has degree `e-6>0` and cuts out slopes at which `x_*` is a
padded-heavy root; every padding root lies outside `U_0=U\{s_0}`. Since
`x_*!=s_0`,

```text
x_* notin U=S_alpha union S_beta.                  (1)
```

Suppose a root `tau` of `S_B` were `alpha` or `beta`. Equation `(HOC2)`
would make `x_*` a root of the specialized primitive locator
`Q(tau,X)`. By `(1)`, it is not in the actual support `S_tau`, so it is the
padded heavy root. The double-root rank-loss classification then gives

```text
r_tau=1,       g_*(tau)=0,                          (2)
```

contradicting `gcd(g_*,S_B)=1`. Therefore neither endpoint center is a root
of `S_B`. Among the three center factors only `ell_theta` can divide
`S_B`, proving

```text
deg gcd(S_B,Lambda)<=1.                            (3)
```

In the double-root arm, `r_gamma` is exactly the indicator that the
supported slope `gamma` contributes the padded root `x_*`; these are the
roots of the squarefree form `g_*`. Hence `(HOC1)` gives

```text
deg gcd(g_*,Lambda)
 =sum_(gamma in A)r_gamma<=1.                       (4)
```

The roots counted in `(3)` and `(4)` are disjoint by
`gcd(g_*,S_B)=1`. Since `Lambda` is squarefree, taking a gcd with
`g_*S_B^2` counts each center at most once. Equations `(3),(4)` therefore
give

```text
j=deg gcd(Lambda,g_*S_B^2)<=1+1=2.                 (5)
```

Substitution in the center-overlap factorization proves the degree cap in
`(HOC5)`. Nonvanishing and `gcd(T_j,S_B)=1` are the separated heavy-row
nonvanishing and exact correction-order theorems. QED.
