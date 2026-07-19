# Proof

For a generic pair, the norm profile theorem gives three distinct unit signed
atoms. If `E,F` are generic endpoints of a distance-six edge, then

```text
<v_E,v_F>=(3+3-6)/2=0.                              (1)
```

Two atoms on one half-basis coordinate contribute either `+1` or `-1` to
this inner product. Thus an overlapping edge has exactly two common support
coordinates, one of each sign: the number of common coordinates is at most
three and a sum of that many signs can vanish only at zero or two.

A positive root--root overlap would give a shared root. Equality of the
nonzero shifted products would then force the other roots to agree. A
positive product--product overlap gives equal ordinary root products; the
common shifted product then gives equal root sums, again forcing the two
unordered pairs to agree. Both contradict a genuine edge. Hence the unique
positive overlap is cross-kind. Exchange endpoints and roots so that

```text
uv=-x.                                               (2)
```

The second, negative overlap cannot reuse either signed-support coordinate in
`(2)`. Among the remaining atoms it therefore has exactly two possibilities:

```text
y=-u,                                                (3R)
xy=u.                                                (3C)
```

The product--product alternative would give `xy=-uv=x` and hence `y=1`.
The reverse cross alternative would give `y=uv=-x`, making `E` antipodal.
Both are excluded.

In case `(3R)`, substitute `y=-u` and `v=-x/u` from `(2)` into the common
shifted-product equation. Since the characteristic is odd, it reduces to

```text
x=2u^2/(1+u^2),       v=-2u/(1+u^2).
```

If `1+u^2=0`, the unreduced equation says `-2=0`, so no valid edge was lost.
The target is

```text
t_R(u)=(1-u)(1+u)^2/(1+u^2).                       (4R)
```

For fixed `t`, equation `(4R)` becomes a nonzero cubic in `u`, with leading
coefficient `-1`, and hence has at most three roots.

In case `(3C)`, equations `(2),(3C)` give `v=-1/y`. The common product
equation reduces to

```text
x=(1+y^2)/(2y^2),       u=xy,       v=-1/y,
```

and

```text
t_C(y)=-(y-1)^2(y+1)/(2y^2).                       (4C)
```

For fixed `t`, equation `(4C)` is again a nonzero cubic with leading
coefficient `-1`. The unique positive and negative support coordinates make
the normalization `(2),(3R)` or `(2),(3C)` unique for each edge. Therefore
the two covers contribute at most three edges each, proving the generic bound
six.

Now let the fiber contain the antipodal pair `{x,-x}` and put `s=x^2=1-t`.
Its vector has one signed atom. A generic endpoint has norm three, so a
distance-six edge has inner product `-1` and exactly one opposite support
overlap. If that overlap is product--product, the generic pair `{u,v}` obeys

```text
uv=s,       u+v=2s,                                  (5P)
```

which determines at most one unordered pair. If it is product--root, exchange
the generic roots so that

```text
u=-s,       v=2s/(1+s).                              (5R)
```

This again determines at most one pair; when `1+s=0`, the original equation
has no solution in odd characteristic. Thus the antipodal vertex has at most
two distance-six neighbors. This proves `(DSO1)`.

Let `O_6,25^0,O_6,25^A` be the overlap moments corresponding to `(DSO4)`.
The quotient-block identity gives

```text
sum_(t!=1)R(t)=Q_n.
```

Using `(DSO1)` target by target and then enlarging to the complete quotient
support,

```text
O_6,25^0+(17/10)O_6,25^A
 <=6 sum_free R(t)+(68/5)sum_antipodal R(t)
 <=(68/5)Q_n,
```

which is `(DSO5)`.

The proved `E=6` interface requires

```text
M_6,25^0+(17/10)M_6,25^A <=B_(n,6)/8,
B_(n,6)=300n^2-102Q_n.                              (6)
```

Split each moment into disjoint and overlapping parts and apply `(DSO5)`.
The residual right side is

```text
B_(n,6)/8-(68/5)Q_n=(750n^2-527Q_n)/20,
```

proving `(DSO6)`. Finally `Q_n<n^2`, so this residual is greater than
`(750-527)n^2/20=(223/20)n^2`. Thus `(DSO7)` implies `(DSO6)` and C36'.
QED.
