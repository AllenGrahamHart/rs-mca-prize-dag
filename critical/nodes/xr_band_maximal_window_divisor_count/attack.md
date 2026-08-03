# Attack Plan

## Exact Currency

Count maximal selected locators `R_d`, never all divisors in the affine
window intersection. Record the reconstructed pair, its full agreement
set, selected supports, live slopes, and strip classification for every
candidate family.

## Route 1: arithmetic inverse theorem

Show that more than `17n^2/25` maximal selected locators force a common
cyclotomic divisor pattern or a low-complexity residue-class support.
The conclusion must be one of the classes already removed by P3,
BP parity, or liveness L. A statement about raw locators is insufficient.

## Route 2: maximal-fiber compression

Use the fiber identity

```text
RAW_d = sum_{e>=d} MAX_e binom(k+e,k+d)
```

in the reverse direction: quotient out all fibers belonging to deeper
maximal pairs, then seek a polynomial or incidence bound on the
remaining exact-depth representatives. Any compression must preserve
the selected `L_P>=2` predicate.

## Route 3: joint row-space transversality

The two single-word Toeplitz systems each have rank `d`, but their
stacked rank need not be `2d`. Classify large row-space intersections.
A useful theorem would show that intersection dimension above a stated
threshold forces quotient periodicity or another paid strip. Do not
assume transversality from the tangent gate alone.

## Route 4: bounded falsification

Search toy rows for maximal selected families, stratified by stacked
rank and residue support. Computation can discover a construction or
calibrate an inverse theorem, but toy survival cannot prove the prize
row bound. Use Modal for any nontrivial enumeration and retain partial
checkpoints.

## No-Go Fences

- Raw affine-divisor counts are refuted as the target currency.
- First-moment margins are average-case evidence, not a uniform bound.
- Packing by `k`-subsets is exponentially too weak.
- The two single-word ranks do not add without a transversality proof.
- "Aperiodic" must include mixed residue-class systems that evade P3.
