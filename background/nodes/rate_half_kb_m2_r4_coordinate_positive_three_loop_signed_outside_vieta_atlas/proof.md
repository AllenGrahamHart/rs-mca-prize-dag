# Proof

The complete edge classifier gives two colored incidences and internal
multiplicities `(2,2,1)`.  Name the uncolored outside pair `d` and the
colored pairs `e,f`.  Each multiplicity-two pair must use its two opposite
signed types, giving products `de,-de` and `df,-df`.  The remaining
internal edge has product `sigma ef`.

Before gauge fixing, let the signs on the two colored edges and the single
`ef` edge be `(epsilon_e,epsilon_f,sigma)`.  Flipping representative `e`
acts by

```text
(epsilon_e,epsilon_f,sigma) ->
(-epsilon_e,epsilon_f,-sigma),                   (1)
```

and flipping `f` is analogous.  Thus every orbit has a representative
`(1,1,sigma')`, while the product
`epsilon_e epsilon_f sigma` is invariant.  The eight raw assignments form
two orbits of four, with invariant `+1` or `-1`.  The common placement atlas
has four orbits, so there are eight combined lanes.

In 442, the colored common endpoint is the unique low-degree pair.  In 433
the two low-degree pairs and `e,f` may both be exchanged, so their two
matchings are equivalent.  This proves `(KBP3V-1)` and the lane count.
Formula `(KBP3V-2)` is the identity `(r+epsilon t)^2` when
`p=epsilon rt`.

For the Vieta equations, take a source lift `z` with `z^2=w`.  The positive
common-kernel form gives

```text
E(w)-pD(w)=0,
z beta(w-1)+sD(w)=0.                              (2)
```

Multiplying the second row at `z` by its row at `-z` gives `-Q_p,s(w)`.
Conversely, under `(KBP3V-4)`, if `Q_p,s(w)=0`, put

```text
z=-sD(w)/(beta(w-1)).                             (3)
```

Then `(3)` satisfies `z^2=w` and the original sum row.  The product row is
already `P_p(w)=0`.  Hence the square-root-free pair is exact under the
guards.

Applying this independently to seven distinct labels proves the saturated
ideal formulation.  A common guarded root of two nonconstant univariate
polynomials forces their resultant to vanish, proving `(KBP3V-5)`.  The
converse for a bare resultant can fail at a forbidden common label or a
collision, which is why no unsaturated sufficiency is claimed.  The checker
enumerates the sign action, prints all seven target records in each lane,
and verifies the squared-row identity symbolically. QED.
