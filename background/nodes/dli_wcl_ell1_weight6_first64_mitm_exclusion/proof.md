# Proof certificate

Encode a negative reduced term `-X^e` by the full exponent `e+256` in
`Z/512`. A reduced signed weight-6 relation is therefore a six-set of full
exponents with no equal or antipodal pair whose corresponding powers sum to
zero.

Rotate the six-set by the inverse of any one term. This preserves equality,
antipodality, and vanishing, and places exponent `0` in the set. Exponent
`256` is then forbidden. The five remaining exponents lie among 510 indices.
Among these indices there are 255 antipodal pairs, so the number of legal
unordered pairs is

```text
C(510,2)-255 = 129,540.
```

A triple can contain at most one antipodal pair. Each of the 255 pairs can be
completed by 508 other indices, so the legal triple count is

```text
C(510,3)-255*508 = 21,849,080.
```

Every legal normalized five-set has a legal two/three split. The exact C++
search stores each legal pair by its field sum. For each legal triple it looks
up the sum `-1-triple`, then checks all six cross pairings for repeated or
antipodal indices. Thus it reports `FOUND` if and only if a reduced signed
weight-6 relation exists.

The hash-pinned artifact has 64 rows, one for each prime in the proved
first-64 split-prime panel. Every row has exact pair and triple counts,
`omega^512=1`, `omega^256=-1`, and status `EXHAUSTED`; no worker failed and
the relation count is zero. The primary verifier validates every record and
replays representative rows from the pinned compiler. The independent audit
reconstructs the combinatorial ledger and replays three representative rows
using a separately written sorted-pair implementation. The registered Modal
entry point retains the full 64-row regeneration path.

The dependency theorem proves that these are exactly the first 64 prime
values of `k*2^41+1`; it supplies complete Pocklington and intervening
composite certificates. Combining that certified panel with the exhaustive
search proves the stated finite exclusion.
