# XR prize flat-nullity rank-metric trade router

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependency:** `xr_prize_flat_nullity_maxwell_trade_space_compiler`

Use a minimal core from the general flat-nullity compiler. Put

```text
s=u+v,
D=s(t-2)+e+1,
M=|V|=a+s+(h t-e)/2.                                  (RM1)
```

For every integer `1<=r<=t-2`, if

```text
D>(t-2-r)M,                                           (RM2)
```

then the core has a nonzero trade of matrix rank at most `r`. Equivalently,
some trade has rank at most

```text
t-1-ceil(D/M).                                        (RM3)
```

In particular, a core with no rank-one trade must satisfy

```text
2s+(t-1)e+2<=(t-3)(2a+h t),                           (RM4)
```

and a core with no trade of rank at most two must satisfy

```text
4s+(t-2)e+2<=(t-4)(2a+h t).                           (RM5)
```

Thus `t=3` always has rank one and `t=4` always has rank at most two. At the
maximal-flat-nullity boundary `s=k-a`, the `e=0` official arithmetic forces
rank one through core arities

```text
12,9,9
```

and rank at most two through arities

```text
18,13,13
```

at prize rates `1/4,1/8,1/16`; positive `e` can only strengthen those
conclusions.

This is a low-rank existence router. It does not classify rank-two trades for
`u>0`, count the canonical circuit owners, or pay the aggregate P-A target.
