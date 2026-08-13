# `A=1` shape-A tensor-rank-two biform exclusion

- **status:** PROVED
- **closure:** every official Shape-A all-excess survivor has tensor rank at
  least three
- **consumer:** `rate_half_band_crossing_location`

Let `e>=9` be odd and put

```text
m=e-2,
n=(3e-7)/2,
R=(9e-7)/2=3n+7.                                  (TRE1)
```

Let `Gamma` be a set of `3e` parameter values. Suppose a biform `G(t,X)`
of bidegree at most `(m,n)` satisfies:

1. for every `x` in an `R`-element domain set, `G(t,x)` has exact degree
   `m` and exactly `m` distinct roots in `Gamma`;
2. for every `delta in Gamma`, `G(delta,X)` is a nonzero polynomial.

Then `G` has tensor separation rank at least three. In particular, there
are no univariate polynomials of the displayed degree bounds such that

```text
G(t,X)=A_0(t)B_0(X)+A_1(t)B_1(X).                 (TRE2)
```

Every official Shape-A all-excess survivor satisfies the two hypotheses.
Therefore every block-supported `K_all` survivor that also satisfies the
exact Shape-A row nonvanishing condition has tensor rank at least three.

## Scope

The theorem excludes the additive/separated mechanism behind the exact
`e=7` degree-ledger fence, and every other rank-one or rank-two coefficient
matrix. It does not exclude tensor rank at least three and does not by
itself prove `K_all` full rank.
