# Proof

The profile reduction proves that `(0,8)` has no odd autocorrelation
coefficients. Modulo two, every non-diameter autocorrelation coefficient is
the multiplicity of its light-light chord class. Even energy also forces zero
or two light-light diameter edges.

Translate one light position to zero and enumerate the other three positions
in increasing order. There are exactly `binom(127,3)=333,375` such supports.
The exact six-chord classification retains 63 supports for which every
non-diameter distance has even multiplicity and the diameter count is zero or
two. Every retained support has two diameter edges and is uniquely of form

```text
{0,t,64,64+t},       1<=t<=63.                        (1)
```

This classification is replayed independently in both vertex and positive-gap
coordinates. Odd units modulo 128 act transitively on steps of each fixed
2-adic valuation. Hence the six representatives `1,2,4,8,16,32` cover (1),
proving the light router in the statement.

For each representative, choose the three heavy positions from the other 124
positions. Multiplying all coefficients by `-1` does not change any chord
product, so fixing the first heavy sign positive leaves 64 sign patterns.
The exact coverage is therefore

```text
6 * binom(124,3) * 64 = 119,087,616.                  (2)
```

The production engine forms every signed folded chord coefficient directly.
For each of the six templates it tests 310,124 heavy supports and 19,847,936
signed vectors. It retains a vector only when there are zero coefficients of
magnitude one, eight of magnitude two, and none of larger magnitude. Every
template count is zero.

The audit engine independently multiplies `F(X)F(X^-1)` in
`Z[X]/(X^128+1)`, checks the constant term 16 and every anti-palindromic
coefficient identity, and applies the same profile predicate. It independently
tests all of (2) and again obtains zero in every template. Thus no actual
coefficient vector in the exhaustive light router has profile `(0,8)`, which
removes that branch of the proved `V=64` profile reduction. QED.
