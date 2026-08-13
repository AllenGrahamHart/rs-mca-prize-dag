# Proof

Assume `|Z|` exceeds the Mersenne budget.  By the preceding residue-zero
router, the synchronized top union contains at least `343071` slope-
explanation pairs and its affine codeword line has total common agreement
core `G` of size `g>=m-2`.

Write the line as

```text
c_gamma=A+gamma*p.
```

Its direction `p` is nonzero: two distinct top slopes have inside agreement
sets with nonempty intersection, where their normalized codeword difference
equals the pointwise-nonzero gauged direction.  Outside `E` that gauged
direction vanishes.  A coordinate of `G` outside `E` must therefore be a
zero of `p`, so

```text
|G intersect E|>=g-(K-1)>=67447=:u.                 (1)
```

Now take any selected slope `delta` assigned an explanation `c_delta` with
inside agreement size `h>=e-u+K=30791`.  Choose an `h`-set `S_delta` of its
inside agreements and two distinct top anchors.  By `(1)`,

```text
|G intersect E intersect S_delta|>=u+h-e>=K.        (2)
```

On `(2)`, both normalized differences from `c_delta` to the two anchors
equal the gauged direction.  They are degree-`<K` codewords, so restriction
injectivity makes them equal.  Thus

```text
c_delta=A+delta*p.
```

This applies to every selected pair with `h>=30791`, including repeated
candidate explanations: the nonzero line direction makes the slope
parameter injective.  All such slopes therefore lie on the same affine
line.  Pair noncontainment caps its total core by `m-1`; off-core agreement
sets are disjoint, giving at most

```text
N-m+1=981129                                           (3)
```

high slopes.

Every remaining assigned explanation has `1<=h<=30790`.  Puncture `E` and
use the single cumulative threshold `h=30790`.  Each such explanation has
at least

```text
m-h=36664
```

outside agreements.  Distinct degree-`<K` explanations agree in at most
`c=5` coordinates, so the ordinary Johnson count is

```text
floor(950350*(36664-5)/(36664^2-950350*5))=26.       (4)
```

The heavy-fiber owner theorem gives at most `floor(e/h)<=e` slopes per
explanation.  Hence the low part contributes at most `98232*26=2554032`.
Adding `(3)` proves `(RA1)`, which is below budget by `13242054` and
contradicts unsafety.
