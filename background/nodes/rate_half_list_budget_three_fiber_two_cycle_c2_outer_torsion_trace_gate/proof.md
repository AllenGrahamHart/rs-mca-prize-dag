# Proof

Let `{A,B}` be the selected pair of completion-square roots in a valid
`c=2` packet. The quotient embedding places both roots in the order-`N`
subgroup, so

```text
t=A/B,       t^N=1.                                  (1)
```

They are distinct and nonzero. Define `z` by `(CTT7)`. The trace-resolvent
dependency proves that the original binary-quartic invariant match is exactly

```text
K_O(z)=0.                                            (2)
```

The recurrence `(CTT2)` is the standard identity obtained by multiplying

```text
t^m+t^(-m)
```

by `t+t^(-1)`. Squaring that expression proves `(CTT3)`. Inducting on `j`
in `(CTT4)` therefore gives, for every root `zeta` of `K_O`,

```text
Q_j(zeta)=C_(2^j)(zeta-2).                           (3)
```

Apply `(3)` to the root `z` in `(2)`. Equations `(1)` and `(CTT7)` give

```text
Q_40(z)=C_N(t+t^(-1))=t^N+t^(-N)=2.                 (4)
```

Thus `z` is a common root of `K_O` and `Q_40-2`, proving `(CTT5)` and the
equivalent resultant condition `(CTT6)`.

Finally, the leading coefficient of `K_O` is `4I^3-J^2`. This is a nonzero
scalar multiple of the discriminant of the separable outer quartic. Every
reduction in `(CTT4)` is therefore defined, and its remainder has degree at
most two. There are forty doubling steps because `N=2^40`. QED.

