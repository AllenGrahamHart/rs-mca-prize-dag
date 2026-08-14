# Proof

The rank-nine evaluation kernel is `F*u`. Owners agreeing with the received
pair on `B` form one affine plane with directions `(u,0)` and `(0,u)`. Each
record of slope `gamma` has a nonempty affine owner line of direction
`(-gamma*u,u)`. Distinct slopes give distinct directions, so

```text
sum_p C(t_p,2)=C(g,2).                              (1)
```

Let `J` be the coordinates where every plane owner agrees with the received
pair. Since `B subset J`, put `j=|J|>=9`. As in the ten-cell theorem, owner
cores split as `C_p=J disjoint_union P_p`, and petals `P_p` are pairwise
disjoint.

If `t_p>=2`, two size-`m` supports through `p` intersect in at least

```text
2m-n=134944.
```

The two distinct slope equations recover both received columns, so this
intersection lies in `C_p`. Put `D=n-m=981104`, `x=m-|C_p|`, and
`y=t_p-1`. Fixed-owner exception disjointness gives `yx<=D`.

Assume `j<=134943=m-D-1`. Then

```text
D+1-x-y=(D-yx)+(y-1)(x-1)>=0,
|P_p|>=t_p-1,
t_p<=D+1.
```

Doubling (1), summing over owner points, and using petal disjointness gives

```text
g(g-1)
 <=981105*sum_p |P_p|
 <=981105*(2097152-j)
 <=981105*(2097152-9)
  =2057517483015.                                  (2)
```

Finally,

```text
1434405*1434404 <=2057517483015
                 <1434406*1434405.
```

Thus `g<=1434405` in the low-core branch. Every larger plane has
`j>=134944`.
