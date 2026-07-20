# Proof

Because every root of `D_*` is nonzero, the pair-trace resolvent factors as

```text
R_D(Z)=e_4^3 product_({A,B} subset Omega)(Z-z_(A,B)),
z_(A,B)=(A+B)^2/(AB).                              (1)
```

The mismatch trace-resolvent elimination proves that a pair has the required
completion-root invariant coupling precisely when

```text
K_O(z_(A,B))=0.                                    (2)
```

For a fixed pair put `t=A/B`. Then

```text
z_(A,B)-2=t+t^(-1).                                (3)
```

If `C_m` denotes the normalized trace polynomial, the doubling identity
`C_(2m)(X)=C_m(X)^2-2` shows inductively that evaluation of the recurrence in
`(JPT2)` at a zero `z` of `K_O` gives

```text
Q_j(z)=C_(2^j)(z-2).                               (4)
```

Polynomial reduction modulo `K_O` does not alter this value. Combining
`(3)` and `(4)` yields

```text
Q_40(z_(A,B))-2
 =t^N+t^(-N)-2
 =(t^N-1)^2/t^N.                                  (5)
```

The denominator in `(5)` is nonzero. Hence the terminal trace equation holds
if and only if `(A/B)^N=1`.

Reduction of `R_D` modulo `K_O` also preserves its value at every zero of
`K_O`. Consequently a common zero of `K_O`, `Rbar`, and `Q_40-2` is, by
`(1)`, the trace of an actual pair; by `(2)` that same pair has the invariant
coupling; and by `(5)` its ratio has order dividing `N`. Conversely, every
pair with these three properties supplies a common zero. This proves the
claimed zero set and the nonconstant-gcd criterion.

Finally `G_2` divides the cubic `K_O`, so its degree is at most three. Every
recurrence representative is reduced modulo that cubic and therefore has
degree at most two. QED.
