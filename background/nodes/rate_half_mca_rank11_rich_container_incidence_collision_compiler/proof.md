# Proof

For a family of `B` sets of size at least `h` in an `n`-element universe,
let `d_x` count the sets containing coordinate `x`. After discarding excess
elements, the total incidence is `I=Bh`.

The discrete convexity of `binom(d,s)` implies that, subject to
`sum_x d_x=I`, the sum `sum_x binom(d_x,s)` is minimized when the `d_x`
differ by at most one. If `I=qn+r`, this minimum is

```text
r binom(q+1,s)+(n-r)binom(q,s).                         (IC)
```

For all 508 containers,

```text
I=508*42453=21566124=20*1048576+594604.
```

Thus some coordinate has multiplicity at least 21. Formula `(IC)` gives

```text
sum_{i<j}|J_i intersect J_j|             >= 211121520,
sum_{i<j<k}|J_i intersect J_j intersect J_k| >= 1308351400.
```

There are `binom(508,2)=128778` pairs and
`binom(508,3)=21720556` triples. Taking ceilings of the two averages gives
1640 and 61.

Every polynomial in `W_i+W_j` vanishes on `J_i intersect J_j`; similarly,
the span of three containers vanishes on their triple intersection. Since
every `W_i` has dimension at most three, the two span dimensions are at most
6 and 9.

Finally, at least 254 of the 508 containers have the same dimension
`r in {2,3}`. Apply the same argument to those 254 sets:

```text
I'=254*42453=10783062=10*1048576+297302,
pair-incidence minimum   =50158940,
triple-incidence minimum =139207710.
```

Division by `binom(254,2)=32131` and `binom(254,3)=2699004` gives ceilings
1562 and 52. The maximum coordinate multiplicity is at least 11, and the
typed spans have dimensions at most `2r` and `3r`. This proves every claim.
