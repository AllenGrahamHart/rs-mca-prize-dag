# Proof

Fix a received `m`-row word `U`. For every listed codeword tuple, take the
first `a`-subset of its common agreement set in a fixed order. For a fixed
subset `S` of size `a>=k`, each component polynomial is uniquely determined by
its agreement with the corresponding row of `U` on any `k` points of `S`.
Thus at most one listed tuple is assigned to `S`. There are `binom(n,a)` such
subsets, proving `(SC)`.

For `(AV)`, count pairs `(U,c)` where `U` is an `m`-row received word and the
codeword tuple `c` has common agreement at least `a` with `U`. There are
`q^(km)` codeword tuples. For a fixed tuple, the number of received words with
common agreement exactly `s` is

```text
binom(n,s)(q^m-1)^(n-s):
```

choose the `s` matching positions, force the received vector there, and at
every other position choose any of the `q^m-1` different vectors. Dividing the
total incidence count by the `q^(mn)` received words gives the displayed
average. The maximum integer list size is at least its ceiling.

For `(EK)`, count received words that admit a codeword tuple with common
agreement at least `k+1`. For a fixed tuple and fixed `(k+1)`-subset, there are
`q^(m(n-k-1))` received words matching it there. There are `q^(km)` codeword
tuples and `binom(n,k+1)` subsets, so the union bound gives at most

```text
binom(n,k+1) q^(m(n-1))
```

bad received words. Under `(HM)` this is strictly less than the `q^(mn)`
received words, so choose `U` for which no tuple has common agreement `k+1`.

Every `k`-subset `S` nevertheless determines a tuple by interpolating each row
of `U` on `S`. Distinct subsets determine distinct tuples: otherwise the same
tuple would agree on their union, which has at least `k+1` points. Hence this
word has exactly `binom(n,k)` tuples at agreement at least `k`, using `(SC)`
for the matching upper bound.

The safe-anchor statement is immediate from `(SC)` and monotonicity of
`binom(n,a)` for `a>=ceil(n/2)`. Formula `(AV)` supplies the general lower
staircase, and the exact unsafe-anchor statement follows from `(EK)`.
