# Proof

A diagonal shifted-root pair has coefficient-vector norm five, except
`{-1,-1}`, which has norm nine. A pair containing `-1` has norm five, except
the same norm-nine pair. Hence every representation in the stated small-vector
fiber is non-diagonal, does not contain `-1`, and has norm one or three. The
signed-support calculation in the distance-four router shows that norm one is
equivalent to being antipodal.

If `{x,-x}` and `{u,-u}` lie in one product fiber, then

```text
1-x^2=1-u^2,
```

so the two unordered pairs agree. This proves uniqueness of the antipodal
representation.

Fix a generic representation `E={x,y}` with target

```text
t=(1-x)(1-y).
```

For every generic distance-four neighbor `F={u,v}`, the proved cross-overlap
router gives at least one of two oriented types after internal exchanges.

In the first type, the product of `F` is the negative of one root `r` of `E`:

```text
uv=-r,       r in {x,y}.
```

The common shifted product then fixes the sum:

```text
u+v=1+uv-t=1-r-t.
```

For either choice of `r`, the sum and product determine at most one unordered
pair `F`. This gives at most two neighbors.

In the second type, the product `xy` is the negative of one root of `F`.
Thus `F` contains the fixed root `-xy`; its other root is uniquely determined
by

```text
(1+xy)(1-v)=t.
```

The factor `1+xy` cannot vanish because `t` is nonzero. This gives at most one
further unordered neighbor. Therefore the generic-to-generic distance-four
degree is at most three. The unique possible antipodal representation adds at
most one, proving the degree claims.

There is a stronger global count. Fix any total order on the finite set of
valid oriented cross-overlap certificates. For each generic distance-four
edge, choose its least certificate and orient the edge from the pair supplying
the negative root monomial to the pair supplying the positive product
monomial. Thus an oriented edge `E -> F` satisfies

```text
product(F)=-r       for one root r of E.               (4)
```

Fix its head `F` and write `q=product(F)`. Equation `(4)` forces one root of
the tail to be `r=-q`. The common nonzero shifted product `t` then forces its
other root `s` through

```text
(1-r)(1-s)=t.
```

Here `r!=1`, since otherwise the left side would vanish. Hence `s` is unique.
Every generic vertex has indegree at most one in the chosen orientation, so
the generic subgraph has at most `g` edges. Every edge incident to the
antipodal vertex uses one generic vertex, giving at most `ag` additional
edges. This proves `(D4C1)`.

If `a=1`, substitute `g=m-1` to get `2(m-1)`. If `a=0`, `(D4C1)` gives
`N_4(t)<=m<=2(m-1)` for `m>=2`, while the nonempty case `m=1` has no edge.
This proves `(D4C2)`. QED.
