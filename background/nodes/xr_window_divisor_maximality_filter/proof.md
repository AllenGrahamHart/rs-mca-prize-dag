# Proof

Fix a maximal codeword pair with full joint core `W` of size `k+e`.
A raw `(k+d)`-set producing this pair is exactly a subset
`Z subset W` of size `k+d`: interpolation on `Z` recovers the unique
pair because `|Z|>=k`, and every raw set recovering the pair must lie
inside its full agreement set. Hence this fiber has size
`binom(k+e,k+d)`. Distinct maximal pairs have disjoint fibers by unique
interpolation. Summing the fibers proves `(F)`.

For `e=d` the fiber size is one. For `e>d` it is larger than one and
the corresponding locator is not a maximal depth-`d` core. The
selected condition is an additional predicate on the unique maximal
pair and is absent from the linear window equations. This proves the
necessity of both filters.

Finally, two copies of the same full-rank `d`-row matrix have stacked
rank `d`, not `2d`; full single-word rank alone cannot establish joint
transversality.
