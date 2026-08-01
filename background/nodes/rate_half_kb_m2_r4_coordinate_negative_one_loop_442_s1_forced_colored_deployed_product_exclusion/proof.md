# Proof

The `S1` outside products are

```text
-ce, -cf, -de, delta*df, -d^2, ef, -ef.
```

Set the forced value `-ce` equal to `m`, so `e=-m/c`.  Removing that record
and writing factors `X-uZ` gives `(KB41FC-1)`.  The proved common quotient
makes `c` a unit, so no denominator component is introduced.

Build `E_0,E_1,E_2` by sparse six-coordinate quotient multiplication.  For
each sign of `delta`, every equation has 23 `(d,f)` terms and leading
monomial `d^4f^4`.  Project into the two proved cubic common components and
replay their six quotient relations.  Exact grevlex Buchberger reduction
reaches a nonzero constant after 56 S-pairs in all four
`(delta,component)` cases; monic normalization gives `1`.  Thus both raw
ideals are unit and both parity cells are empty. QED.
