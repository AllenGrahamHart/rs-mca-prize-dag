# fm1 proof

Fix a support `R` of size `j`, and write `S = H \ R`. The restriction of the
RS code to `S` has dimension `k`, while `|S| = k + t`. Hence the quotient
syndrome space has dimension `t`.

For a random received pair `(u,v)`, let `U,V in F^t` be the syndromes of
`u|_S` and `v|_S`. The support `R` is aligned at a finite slope `z` exactly
when

```text
U + z V = 0
```

in the quotient, with `V != 0`. The exclusion `V = 0` is the standard
all-slope/paid-fiber degeneracy and is not counted in this first-moment
column.

There are `q^t - 1` choices for nonzero `V`. For each such `V`, there are
exactly `q` choices of `U` on the affine line spanned by `V`, namely
`U = -z V` for `z in F`. Therefore the probability that fixed `R` aligns is

```text
q (q^t - 1) / q^(2t)
  = (1 - q^(-t)) q^(1-t).
```

There are `binom(n,j)` choices of `R`. By linearity of expectation,

```text
E[#aligned] = binom(n,j) (1 - q^(-t)) q^(1-t).
```

This proves the exact FM1 formula.
