# Proof

For `m in F_p^*`, multiplication by `m` gives a bijection

```text
C_m -> {(c,d) in A^2:d/c=m},  a -> (a,ma),
```

so `|C_m|=R(m)`.

Fix an ordered pair of product representations

```text
(a,b), (a',b'),       ab=a'b'=t.
```

Put

```text
m=b'/a=b/a'.
```

The two expressions agree because `ab=a'b'`. Moreover

```text
b'=ma,   b=ma',   a,a' in C_m,   t=m*a*a'.        (1)
```

The product representations are equal exactly when `a=a'`. They are swaps
exactly when `m=1`: if `m=1`, (1) makes the second representation `(b,a)`;
conversely a swap forces `ma'=a'`, hence `m=1`.

Conversely, from `m!=1`, distinct `a,a' in C_m`, and `t=m*a*a'`, the ordered
representations

```text
(a,ma'), (a',ma)
```

have product `t` and are neither equal nor swaps. These constructions are
inverse. The proved swap-involution count says that the number of such
ordered representation pairs is `Q(t)=P(t)(P(t)-2)+D(t)`, proving `(LS1)`.
Multiplying `(LS1)` by `R(t)`, summing over `t!=1`, and substituting
`t=m*a*a'` proves `(LS2)`.

Geometrically, each `a in C_m` gives the point

```text
(1-a,1-ma) in H^2
```

on the line `Y=1+m(X-1)` through `(1,1)`. Formula `(LS2)` says that an
ordered pair of distinct nonidentity-line points emits slope `m*a*a'` and is
weighted by the number of non-base points on that target line.

## Canonical-target no-go fence

The exact symbolic search in
`experiments/prize_resolution/h3_chord_target_identity_search.py` tests all
source-coordinate monomials with exponent vectors in `{-1,0,1}^4` as a
putative target point `(z,w) in H^2`. Over the rational function field in
independent `a,a',m`, the only identity

```text
1-w=m*a*a'*(1-z)
```

in this class is `z=w=1`, the excluded base point. Hence the natural claim
that every source chord canonically supplies one nontrivial target witness is
false in this complete bounded ansatz. This fence is not a statement about
more general rational constructions.
The exact run record is in `symbolic_search_result.md`.

The second exact fence in `classical_collinearity_no_go.md` tests every direct
assignment of the six subgroup variables to the standard collinear-triple
equation and finds none. Thus the known `T(H)` estimate is not a citation-level
close for `(LS2)` without an additional rational bridge.
