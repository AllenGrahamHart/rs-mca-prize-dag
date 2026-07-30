# Proof

Assume that the forced source value `w` in `(KBDM-8)` is ramified for
`W=X^2`. In the source-line coordinates the ramified values are
`{0,infinity}`, and `tau(W)=1/W` exchanges them. Thus `w` and `tau(w)` are
the two distinct ramified labels.

At `w`, the two coincident component stars are the same reduced edge on the
two-label set `J_1`; hence that star vertex has weight at least two. Whole-
fiber diagonal transport makes the quartic at `tau(w)` the reciprocal
square on the two crossing labels in `I`. Its coincident star is another
weight-at-least-two vertex. The two vertices are distinct because one is
`J-J` and the other `I-I`. They contribute at least

```text
binom(2,2)+binom(2,2)=2                              (1)
```

to the complete-source defect.

The ramified orbit has now used both branch values. Therefore all four
labels of `K_0=K intersect tau(K)` are unramified. Each contributes two
reduced quadratic stars, for eight star units total. By `(KBDM-4)` all
their roots lie in `J_0`. A reduced quadratic star is an unordered
two-subset of `J_0`, and `|J_0|=4`, so there are at most six possible
vertices.

If their weights are `e_1,...,e_6`, padding by zeros, then
`sum e_i=8`. Convexity, or direct balancing, gives

```text
sum_i binom(e_i,2) >= 2,                            (2)
```

with equality at `(2,2,1,1,1,1)`. These `J_0-J_0` vertices are disjoint
from the two vertices in `(1)`. Hence `(1)--(2)` give
`Delta_star>=4`, contrary to the complete-source quartic defect theorem
`Delta_star<=3` imported by the recurrence router.

Thus the forced fiber is unramified. The `4/3` dimension and minor
conclusions follow from the preceding linear-cut theorem. QED.
