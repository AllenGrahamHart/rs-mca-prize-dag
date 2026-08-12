# Proof

The factor-incidence theorem gives exactly `Rm_j` distinct points of
`Q_j=0` on the grid `X_cls x Gamma`. For every `gamma in Gamma`, the fiber
`Q_j(gamma,X)` is nonzero and has degree at most `n_j`, so it has at most
`n_j` distinct roots. Every supported root of `Q_j(t,x_*)` adds a point in
the same parameter fiber and on the new row `x_* notin X_cls`. Therefore

```text
Rm_j+s_j<=Tn_j,                                   (1)
```

which proves the first two assertions in `(URB4)`.

Each `Q_j(t,x_*)` is nonzero: otherwise its factor would make
`G(t,x_*)` identically zero. Bihomogeneity therefore makes it a binary
form of exact degree `m_j`, so `u_j=m_j-s_j` is nonnegative.

Put `J_*=gcd(Lambda,g_*)` and `g_off=g_*/J_*`. The center-adjusted
heavy-row factorization is

```text
G(t,x_*)=g_off(t)S_B(t)T_(2+d_A)(t),
deg g_off=e-6-d_A.                                (2)
```

Every root of the squarefree `g_off` lies in `Gamma`. Each is a root of at
least one specialized factor, so

```text
sum_j s_j>=e-6-d_A.
```

Since `sum_jm_j=M=e-2`, this gives

```text
sum_j u_j=M-sum_j s_j<=4+d_A,                     (3)
```

and completes `(URB4)`. No assertion about the other `4+d_A` projective
degrees of the heavy row is needed.

The exact factor trichotomy has

```text
n_j=ceil(Rm_j/T),
chi_j=2n_j-3m_j
 =-1       for large odd,
 =-2       for huge even.                         (4)
```

Using `2R=9e-q`, equation `(URB2)` becomes

```text
2sigma_j=3e chi_j+qm_j.                           (5)
```

Also `(URB4)` gives `sigma_j>=m_j-u_j>=m_j-(4+d_A)`.
For `chi_j=-1`, substitute in `(5)` to get

```text
qm_j-3e>=2m_j-8-2d_A,
(q-2)m_j>=3e-8-2d_A.                              (6)
```

For `chi_j=-2`, the same calculation gives

```text
qm_j-6e>=2m_j-8-2d_A,
(q-2)m_j>=6e-8-2d_A.                              (7)
```

These are `(URB5)` and specialize to `(URB6),(URB8)` with the required
parities.

It remains to compress the `d_A=1` profiles. Here `q=7`. Profile II has
two large-odd factors and one small-odd factor, hence total parameter
degree at least

```text
2(3e-10)/5+1>e-2                                 (8)
```

for every relevant `e>5`, contradicting `sum m_j=e-2`. Profile III has
one huge-even and one small-odd factor, hence degree at least

```text
(6e-10)/5+1>e-2.                                  (9)
```

It is likewise impossible. The trichotomy leaves only profile I, proving
`(URB7)`. Least parity-compatible ceiling and direct substitution of the
official `e` give `(URB9)`. QED.
