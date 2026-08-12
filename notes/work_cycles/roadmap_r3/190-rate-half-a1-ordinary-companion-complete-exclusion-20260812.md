# Cycle 190: rate-half ordinary-companion complete exclusion (2026-08-12)

The quartic deck involution from Cycle 189 is itself too costly. Every full
six-row slope contributes thirty ordered pairs; deleting the six pairs on
the known involution graph leaves twenty-four. Across `2^39-13` full
slopes, quartic pair multiplicity gives at least `3298534883250` distinct
subgroup points on the at most four residual fiber-product components.

The audited Corvaja--Zannier bounds force one residual component to be a
second toral graph. It induces another subgroup-compatible deck
transformation `X -> cX` or `X -> c/X`. Together with either first
involution `X -> -X` or `X -> k/X`, this second transformation is equal to
the first or generates a Klein four subgroup. The first option is excluded
because its graph was removed; the second is impossible because the deck
group order divides the cover degree six.

Shape C is therefore empty. Together with the quadratic exclusion of
shapes B and D, the four-shape classification now leaves only shape A: one
large irreducible odd factor with record
`(e-2,(3e-7)/2;e-7,2,3;4)` and no ordinary companion.

```text
start:                   4313462fd
result:                  NARROWED, all ordinary companions excluded
DAG delta:               +1 PROVED node, +4 req edges, +1 ev edge
critical status delta:   none
upstream terminal delta: strong Lane-T PR #1161 extension
delta-star movement:     none
compute:                 exact local replay only; no Modal spend
next route action:       attack the unique large irreducible shape A
```
