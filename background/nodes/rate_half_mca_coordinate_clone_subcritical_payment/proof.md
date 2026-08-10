# Proof

Fix one clone class `C` and its irreducible component `V(F_C)`. A nonzero
bidegree-at-most-`(1,1)` coordinate equation containing this irreducible
bidegree-`(1,1)` component is a scalar multiple of `F_C`; therefore the
clone classes are disjoint coordinate sets.

Let `R_C` be the rich parameter points assigned to this component after a
deterministic tie-break among components. Every point of `R_C` automatically
satisfies the `c` equations in `C` and must satisfy at least `m-c` equations
outside `C`. An outside coordinate curve does not contain `V(F_C)` and meets
it in at most

```text
(1,1).(1,1)=2
```

projective points. Double-counting incidences between `R_C` and outside
coordinates gives

```text
|R_C|(m-c) <= 2(n-c).                                (1)
```

For `2<=c<=m-1`,

```text
c(m-c+1) >= 2(m-1) >= n.                            (2)
```

Indeed `c(m+1-c)` is concave in `c` and has the same endpoint value
`2(m-1)` at `c=2` and `c=m-1`. Inequality (2) is equivalent to

```text
2(n-c)/(m-c) <= 2c.
```

Combining with (1) proves `|R_C|<=2c`. Summing over disjoint subcritical
classes gives at most `2n` rich parameter pairs and hence at most `2n`
distinct slopes. The literal row checks are

```text
2n = 4194304 < 16777215 < 274980728111395087.
```

Finally, two classes of size at least `m` would be disjoint and consume at
least `2m>n` coordinates. Thus there is at most one large class. QED.
