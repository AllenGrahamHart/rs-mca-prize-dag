# Proof

Suppose first that one biform `G` realizes both factorizations. For nonzero
scalars `lambda_x,zeta_delta`,

```text
G(t,x)=lambda_xP_x(t),
G(delta,X)=zeta_delta F_delta(X).                   (1)
```

Evaluating both identities at `(delta,x)` gives `(SWG3)`. At a nonincidence
cell every displayed factor is nonzero. Comparing `(SWG3)` for `x` and the
anchor `a_delta` gives `(SWG4)`, so `W lambda=0`. The row coefficient theorem
also gives `Krow lambda=0`. This proves necessity.

Conversely, suppose `(SWG5)` has a full-support kernel vector `lambda`.
Write

```text
P_x(t)=sum_(j=0)^m p_(j,x)t^j.                     (2)
```

The equations `Krow lambda=0` say that for every `j` the vector

```text
(lambda_xp_(j,x))_(x in X)                         (3)
```

belongs to `RS[F,X,n+1]`. Since `R>n`, there is a unique polynomial
`g_j(X)` of degree at most `n` with these evaluations. Hence

```text
G(t,X)=sum_(j=0)^m g_j(X)t^j                       (4)
```

has bidegree at most `(m,n)` and satisfies

```text
G(t,x)=lambda_xP_x(t)       (x in X).               (5)
```

Fix `delta in Z`. Because `F_delta` has degree `n<R`, at least one row is a
nonincidence, so the anchor exists. Define `zeta_delta` by `(SWG6)`; it is
nonzero. Equation `(SWG4)` then gives

```text
lambda_xP_x(delta)=zeta_delta F_delta(x)            (6)
```

for every nonincident `x`. At an incidence, both sides vanish by `(SWG2)`,
so `(6)` holds on all `R` rows. Equations `(5)--(6)` show that the two
degree-at-most-`n` polynomials

```text
G(delta,X),       zeta_delta F_delta(X)             (7)
```

agree at all points of `X`. Since `R>n`, they are equal. This proves the
fiber factorization and the sufficiency of `(SWG5)`. Applying the usual
dual-GRS parity checks to the coefficients of `(7)` also proves that the
parameter-fiber coefficient gate follows automatically.

It remains to specialize. In both pair profiles, every classified row is
light, whereas every padded-heavy root lies outside `X`. The padded-fiber
factorization therefore gives `(SWG2)`: both sides vanish exactly when the
actual support at `delta` contains `x`.

For one fiber the number of weld rows is the number of nonincidences minus
one, proving `(SWG9)`. Since `F_delta` has degree `n`, this is at least
`R-n-1`. Substitution gives

```text
extremal: R-n-1=2p-1+d_A,
strict:   R-n-1=p+1+r_A.                            (8)
```

Multiplying by the selected fiber counts proves `(SWG10)`. The official
substitutions in `(SWG11)` are direct. QED.
