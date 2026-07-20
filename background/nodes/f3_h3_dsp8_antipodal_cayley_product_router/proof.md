# Proof

Because `t` in `(ACP2)` is nonzero, `a` is not `1` or `-1`, so `C(a)` is
defined and nonzero. Take an ordered representation

```text
(1-X)(1-Y)=1-a^2
```

and put `u=X/a`, `v=Y/a`. Since `X,Y,a` lie in `H`, so do `u,v`. Expansion
and cancellation of the constant terms give

```text
u+v=a(1+uv).                                         (1)
```

If `u=1`, equation `(1)` and `a!=1` force `v=-1`; if `u=-1`, it and
`a!=-1` force `v=1`. The same holds after exchanging `u,v`. Thus the
solutions meeting `{1,-1}` are exactly the two orders of the antipodal pair
`{X,Y}={a,-a}`.

Away from those boundary solutions all Cayley values are finite and nonzero.
Cross multiplication gives

```text
C(u)C(v)=C(a)
  iff
(1-a)(1+u)(1+v)=(1+a)(1-u)(1-v)
  iff
u+v=a(1+uv),                                         (2)
```

where the last equivalence uses that the characteristic is odd. The Cayley
map is injective on the complement of `1`, with inverse

```text
C^(-1)(gamma)=(gamma-1)/(gamma+1).                   (3)
```

Consequently `(X,Y)->(C(X/a),C(Y/a))` is a bijection from the ordered
nonantipodal representations of `1-a^2` to the ordered factor pairs counted
by `M_a`. Restoring the two boundary orders proves `(ACP4)`, and `(ACP5)` is
immediate.

The same bijection respects exchange of the two roots, so it induces a
bijection between unordered nonantipodal representations and unordered
factor pairs. Restricting both sides to the small generic predicate gives
exactly `V_a`. The inverse in `(3)`, followed by scaling by `a`, recovers the
original roots, so the signed support and its disjointness relation are
retained rather than inferred from a marginal factor count. Hence `E_a` is
exactly twice the number of disjoint generic edges at the target `1-a^2`.

The quotient-line definition gives

```text
L_a=R(1-a^2).                                        (4)
```

The adapter proves that `K_25^A` counts the two orientations of each
disjoint generic edge, each paired with one ordered quotient representation,
over antipodal targets with `P(t)>=25`. A canonical sign chooses every such
target once. Substituting `(ACP5)` and `(4)` therefore gives `(ACP7)` with no
extra factor. QED.
