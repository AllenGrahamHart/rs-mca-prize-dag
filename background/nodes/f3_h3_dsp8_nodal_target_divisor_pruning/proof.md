# Proof

All three roots in `(NTP1)` have a common nonzero factor `c`, so positive and
negative root collisions are unchanged after suppressing it. Put `a=theta`
in that scale-free triple. This gives `(NDP1)`, with every displayed
denominator nonzero on the admissible parameter set.

Direct subtraction gives the following numerators, up to nonzero denominator
factors and irrelevant signs:

```text
             R(b)                         U(b)                         V(b)
R(a)  (a-b)(a+b+1)          (ab-1)(ab+b+1)          (ab+a+1)(ab+a+b)
U(a)  (ab-1)(ab+a+1)        (a-b)(ab+a+b)            (a+b+1)(ab+b+1)
V(a)  (ab+a+b)(ab+b+1)      (a+b+1)(ab+a+1)          (a-b)(ab-1).
                                                               (1)
```

The six linear-fractional solutions represented by the factors in `(1)` are
exactly the six values in `S(a)`. This proves that a positive root collision
is equivalent to `b in S(a)`. Each such value merely permutes the three roots
in `T(a)`, as can also be checked directly. Conversely, if two triples with
common sum `3` and common product `1` share a nonzero root, their remaining
two roots have the same sum and product. Their unordered root multisets are
therefore equal. This proves `(NDP3)`, including repeated-root cases where
some of the six orbit values coincide.

The normalized target router gives

```text
t=1+R(a)R(b)(R(a)+R(b)-3).
```

Since `R(a)=-1/q(a)`, this is

```text
t=1-[q(a)+q(b)+3q(a)q(b)]/[q(a)^2q(b)^2],           (2)
```

which proves `(NDP5)` and `(NDP6)`. Expanding the numerator of `(2)` and
factoring gives

```text
q(a)^2q(b)^2-q(a)-q(b)-3q(a)q(b)
 =(ab-1)(ab+a+1)(ab+a+b)(ab+b+1).                  (3)
```

This proves `(NDP4)`. Each factor on the right of `(3)` occurs in `(1)`, so
`t=0` forces a positive root collision. Signed disjointness therefore removes
the complete zero-target divisor, not merely a generic part of it.

Finally, after positive collisions are removed, signed disjointness is
equivalent to the nine additional nonvanishing tests
`T_i(a)+T_j(b)!=0`. These tests and `(NDP6)` are direct field operations and
may be applied before the more expensive richness and quotient-line counts.
Orbit canonicalization is count-preserving only when the decoration and
repeated-root multiplicities are retained. No estimate for the surviving
pairs has been used, so no correlation bound follows. QED.
