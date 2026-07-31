# Proof

The explicit product involution acts on projective coordinates by

```text
[X:Z] |--> [Alpha X+Beta Z : Gamma X-Alpha Z].    (1)
```

Its square is `(Alpha^2+Beta Gamma)` times the identity, and that scalar is
nonzero by the involution compiler.  Suppose first that the six residual
products split into three involution pairs.  Their projective root set is
stable under `(1)`, so the two degree-six binary forms in `(KB41BI-2)` have
the same six simple roots.  They are therefore proportional.

Conversely, `(KB41BI-2)` makes the six-root set stable under the involution.
The product map conjugates source negation to this involution.  Every source
label is nonzero and deployed characteristic is odd, so source negation has
no fixed label; product injectivity therefore gives no fixed product among
the twelve packet products.  The involution consequently partitions the
six residual roots into three two-cycles.  These are exactly the required
residual product pairs.

It remains to quotient the forced-record choices.  Act on a pair
`(signed cell, forced record)` by the same representative sign changes and
`E/F` skeleton automorphisms used in the template classifier.  Exact finite
orbit closure gives the distributions

```text
S0: 2 orbits each of sizes 4,8,16;
S1: 6 orbits of size 8 and 4 of size 16;
S2: 1 orbit of size 1 and 3 of size 2.
```

Their weighted sums are `56,112,7`, proving `(KB41BI-3)` and the total cap
of twenty per common row. QED.
