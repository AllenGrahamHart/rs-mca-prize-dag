# Proof - XR nongeneric-explanation Plotkin width

Distinct codeword pairs explaining the same received pair have explanation
supports intersecting in at most `K-1` coordinates. Canonical truncation to
`A` coordinates preserves that upper bound. It is also injective: if two
pairs had the same canonical `A`-subset, both component differences would
vanish on `A>K` points and hence both pairs would be equal. Thus `(XW2)`
defines a binary constant-weight code of length `N` and distance at least
`2H`.

For `m=|mathcal E|`, sum pairwise Hamming distances coordinatewise. If a
coordinate occurs in `a_x` supports, its contribution is
`a_x(m-a_x)<=m^2/4`. Therefore

```text
binom(m,2)2H<=Nm^2/4.                                  (1)
```

When `N<4H`, rearranging `(1)` gives `(XW3)`. At equality `N=4H`, map the
supports to sign vectors. Their pairwise inner products are nonpositive, so
the elementary Rankin lemma gives at most `2N` vectors.

If `E=N-4H` lies in `[0,C log_2 n]`, partition the supports by their pattern
on any `E` coordinates. Puncturing within one class preserves distance and
leaves length `4H`, so Rankin gives at most `8H` members per class. Since
`2^E<=n^C` and `H<=n`, this is at most `8n^(C+1)` in total. Negative `E` is
already covered by `(XW3)` or the equality bound. This proves `(XW4)`.

For the terminal tree, begin with `N_0<=4H`. The equality bound gives at most
`2N_0<=8H` explanation children. Every live nongeneric transition satisfies

```text
N_(j+1)<=N_j-A_j<=N_j-H.                               (2)
```

Thus level-one instances have length at most `3H`; by `(XW3)` each has at
most `4` explanation children. Level two has length at most `2H` and at most
`2` children. Level three has length at most `H`, and `(2)` leaves no next
live instance. Hence the number of live instances is at most

```text
1+8H+32H+64H=1+104H,                                   (3)
```

proving `(XW5)`. The genuine-tangent coordinate injection charges at most
the current ambient length, which is at most `4H`, at every instance.
Therefore the total is at most

```text
4H(1+104H)<=420H^2.                                    (4)
```

At an official row `H<=n`, and `420n^2<=16n^3` for every `n>=27`; all six
clean candidates are much larger. This proves `(XW6)` without charging any
generic-chart mismatch slope.

For `(XW7)`, the root explanation count is at most `8n^(C+1)` by `(XW4)`.
After one transition,

```text
N_1<=3H+C log_2 n<=7H/2.
```

The strict Plotkin denominator is at least `H/2`, so the branching factor is
at most `8`. At the next two levels, lengths are at most `5H/2` and `3H/2`,
giving branching factors at most `2` and `1`. A further transition leaves
length at most `C log_2 n<=H/2`, below the live minimum `A>=H`.

Writing `B_0=8n^(C+1)`, the whole live tree therefore has at most

```text
1+B_0+8B_0+16B_0<=1+200n^(C+1)                         (5)
```

instances. Charging at most `n` genuine tangents per instance gives

```text
n(1+200n^(C+1))<=201n^(C+2),                            (6)
```

which proves `(XW8)--(XW9)`.
