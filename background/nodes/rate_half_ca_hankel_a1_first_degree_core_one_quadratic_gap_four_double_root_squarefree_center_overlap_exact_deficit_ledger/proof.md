# Proof

The exact source partition identifies the center deficits in the
double-root arm:

```text
r_gamma=1  iff  x_* is a padded root at gamma
         iff  ell_gamma divides g_*.               (1)
```

Hence the center factors of `g_*` have total degree

```text
deg gcd(Lambda,g_*)=sum_(gamma in A)r_gamma=d_A.    (2)
```

Every assigned-center actual error support lies in `U`, whereas the fixed
heavy point `x_*` lies outside `U`. If a center `gamma` is a root of
`S_B`, then `Q(gamma,x_*)=0`; at that center `x_*` can therefore only be a
padded locator root. Equation `(1)` gives

```text
ell_gamma|S_B and ell_gamma|Lambda
             => ell_gamma|g_*.                     (3)
```

Since `Lambda` is squarefree, `(3)` says that adding the factor `S_B^2`
does not add any new center root to the gcd. Thus

```text
gcd(Lambda,g_*S_B^2)=gcd(Lambda,g_*)               (4)
```

up to a unit. Equations `(2),(4)` prove `(HED2)`.

The unified squarefree remainder theorem gives

```text
R_lambda=G(t,x_*)=(g_*S_B^2/J)T_j,
T_j!=0,       deg T_j<=j,       gcd(T_j,S_B)=1.    (5)
```

If `d_A=0`, then `j=0`, so `J=1` and `T_j` is a nonzero scalar. If
`d_A=1`, the unique center with nonzero deficit supplies the sole factor
of `J`, and `(5)` gives the second profile in `(HED3)`. QED.
