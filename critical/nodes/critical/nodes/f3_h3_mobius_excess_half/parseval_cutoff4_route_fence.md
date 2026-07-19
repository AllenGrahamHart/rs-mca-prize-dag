# Parseval cutoff-four route fence

Date: 2026-07-13.

The proved rich-fiber norm cutoff uses seven coefficient vectors of squared
norm at most `3` and forces a pair at squared distance at most `6`. Replacing
`6` by `4` cannot follow from this metric information, even after imposing
the matching constraint that distinct representations of one nonzero product
cannot share a factor.

The exact graph probe
`experiments/prize_resolution/h3_parseval_cutoff4_probe.py` uses genuine
shifted-pair coefficient vectors. Vertices have squared norm at most `3`; two
vertices are adjacent when their squared distance exceeds `4`. In the
matching version they must also have disjoint exponent pairs. Seven-cliques
exist at orders `16`, `32`, and `64`. At order `64`, one matching witness is

```text
(1,2), (3,4), (5,6), (7,8), (9,10), (11,12), (13,14).
```

All seven vectors have squared norm `3`, all exponent pairs are disjoint, and
all pairwise squared distances are at least `6`. Modal run
`ap-oSn78pIzwhAuDxXpR59N63` replayed both the unconstrained and matching
graphs at all three orders with peak RSS `55MB`.

This is a route fence, not a C36 counterexample: the displayed pairs are not
claimed to have one common shifted product modulo an official prime. Any
improvement from `6^(n/4)` to `4^(n/4)` must use those same-product
congruences, a resultant/coprimality input, or another arithmetic property.
Parity, norm caps, centroid packing, and factor-disjointness alone are
insufficient.
