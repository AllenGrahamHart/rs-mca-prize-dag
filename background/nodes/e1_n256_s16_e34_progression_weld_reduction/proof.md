# Proof

In the progression template exactly two heavy-heavy chords have one circular
length. Their common endpoint is the middle heavy position. Translate one
outer endpoint to zero and reflect if necessary. The repeated length then has
the unique representative `t` in `1,...,63`, and

```text
H={0,t,2t}.
```

The value `t=32` would make the outer chord a diameter and is excluded; no
other value in the range identifies heavy positions. Conversely, these 62
normal forms exhaust the progression template.

Let the heavy signs be `s_0,s_1,s_2`. The two repeated-class heavy-heavy
products contribute

```text
4 s_1(s_0+s_2).
```

Only the two extension positions `-t` and `3t` can supply heavy-light chords
in this class, so their combined contribution has magnitude at most four.
The light-Sidon property permits at most one light-light chord, of magnitude
one. If `s_0=s_2`, the repeated class therefore has magnitude at least
`8-4-1=3`, contradicting profile `(6,7)`. Hence `s_2=-s_0`. Global sign gives
the printed coefficient normalization.

The outer heavy-heavy chord has circular length represented by `2t` modulo
128 and is the singleton heavy-heavy class. A light position lies at this
distance from a heavy position precisely when it is one of

```text
-2t, 3t, -t, 4t             modulo 128.
```

The heavy-template theorem forces at least one such heavy-light chord. The
four residues are nonheavy and distinct: every forbidden equality reduces to
`mt=0 mod 128` for `m` in `{2,3,4,5,6}`, whose only candidate in the printed
range is `t=32`, already removed.

There are 125 nonheavy positions. Four-position supports meeting `W_t` number
`binom(125,4)-binom(121,4)=1,195,965`. After global sign, the middle heavy
sign gives two choices and the light signs give sixteen. Multiplying by the
62 normal forms proves the chamber count.

Finally consider the automorphism `sigma_u:F(X)->F(X^u)` of
`Z[X]/(X^128+1)` for odd `u`. Reduction modulo `X^128+1` permutes the 128
coefficient positions with possible sign changes. It therefore preserves
coefficient magnitudes and, because `u` is a unit modulo 256, conductor.
Moreover

```text
sigma_u(F(X)F(X^-1))=sigma_u(F)(X)sigma_u(F)(X^-1),
```

so autocorrelation magnitudes are permuted. Multiplication by `u` also
permutes the triples with index sum zero modulo 128, proving invariance of
`M_3`.

The odd units act transitively on residues with a fixed 2-adic valuation.
Among `1<=t<=63`, `t!=32`, the five possible valuations `0,...,4` have
`32,16,8,4,2` forms. Choosing `1,2,4,8,16` gives the printed orbit collapse
and five-representative census size. QED.
