# Proof

The marked source-frame theorem gives

```text
q_i^T M_s q_j=0
```

for both endpoint matrices `M_s` and all `i,j`. A projective change of
parameter replaces the coefficient vectors by an invertible linear
combination and replaces the local derivative `dot M` by a linear
combination of the endpoints. Therefore

```text
u^T dot M v=0       for every u,v in W_q.            (1)
```

The specialized primitive locator `Q_gamma` is a parameter evaluation of
`q`, hence belongs to `W_q`; it also belongs to `K_gamma`. This proves the
first inclusion in `(QKI3)`.

By the supported first-jet theorem, the form induced by `dot M` on

```text
K_gamma/span{Q_gamma}                               (2)
```

is nondegenerate and has dimension `c`. Equation `(1)` says that the image
of `H_gamma/span{Q_gamma}` in `(2)` is totally isotropic. If `U` is a
totally isotropic subspace of a nondegenerate bilinear space `V`, then
`U subset U^perp`, so

```text
2 dim U<=dim V.                                     (3)
```

Apply `(3)` with `dim V=c`. This proves `(QKI3),(QKI4)` over every
characteristic.

Evaluation on the distinct source set `T_gamma` has kernel, inside the
degree-at-most-`d` coefficient space, equal to

```text
Q_min F[X]_(<=c)=K_gamma.                           (4)
```

Restricting `(4)` to `W_q` shows that the kernel of the matrix `(QKI5)` is
exactly `H_gamma`. Rank-nullity and `(QKI4)` give

```text
rank E_gamma=(e+1)-dim H_gamma
            >=e-floor(c/2).                        (5)
```

The nonzero vector `Q_gamma` is always in that kernel, so the rank is at
most `e`. This proves `(QKI6)`. Substitution of `c=1` and `c=2` gives
`(QKI7),(QKI8)`. The exception caps are inherited from the supported
first-jet theorem. QED.
