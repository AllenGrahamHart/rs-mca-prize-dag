# Proof

Let `N_h` be the number of transformed explanations with outside deficit at
most `h`. Although the earlier MCA corollary was calibrated in the sparse
range `e<d`, its underlying ordinary set-system argument has no such
hypothesis. After puncturing the direction support, choose exactly
`A_h=m-h` outside agreement coordinates for each explanation. The guard
`A_H>K-1` gives `A_h>K-1` throughout the prefix, and distinct degree-`<K`
explanations intersect on at most `K-1` coordinates. Thus the ordinary
Johnson/mean-centered theorem applies directly and gives `N_h<=C_h`.
For every `v>=h`, also `N_h<=N_v<=C_v`; hence `N_h<=B_h`. Summation by
parts against the nonincreasing owner weights `floor(e/h)` gives the prefix
charge

```text
sum_(h=1)^H (B_h-B_(h-1))*floor(e/h).
```

Every explanation with deficit above `H` belongs to the top-third union.
The cross-layer synchronization theorem puts that entire union on one affine
codeword line and charges its pair-noncontained total core only once, by
`N-m+1=t+1`. Adding the disjoint prefix and high-union charges proves
`(MG1)`.

The primary verifier scans all 528 newly paid official supports and every
prefix threshold using exact integer arithmetic. The independent checker
reconstructs endpoint profiles by a separate grouped summation, checks all
parent hashes, and verifies both adjacent failure modes and hostile
mutations.
