
## H1/S3 ADDENDUM (2026-07-26; GF list-compiler replay, no status change)

Replay of Przemek's `thm:affine-span-list` (GF :498) and `thm:rank-flat-list`
(GF :583) against this node. Artifact:
`verify_affine_span_chamber_replay.py`; full record in
`notes/affine_span_chamber_replay_20260726.md`.

**The compilers kill none of the thirteen edge-degree chambers.** They constrain
the affine span of four codewords in `RS[F,D,K]`; the chambers are edge-degree
patterns of the *locator* pencil. No map between the two exists in this node, so
the Convergence Ledger's S3 promotion test ("ev→req when chamber coordinates are
bound to affine spans") cannot fire. What is owed is a lemma computing the affine
rank `s` (ideally also `d_1,d_2,b`) of the four codewords from a chamber's edge
degrees. **H1 remains ev-wired.**

Positive by-product, proved here directly and independently of the compiler:

```text
no THREE list members at agreement a are collinear, whenever
n-K+1 > floor(3(n-a)/2).
```

Three collinear members share one support `supp(v)`; on it their values are
pairwise distinct so at most one agrees with `u` per position, off it all three
coincide, giving `3a <= 3n - 2 wt(v)`, against MDS `wt(v) >= n-K+1`. At the
official row this fires for every

```text
a >= 1,466,015,503,701 = 3n/4 - 183,251,937,963,
```

so in particular at `3n/4` and `3n/4-1`, where it reproduces the compiler's
`s=1` caps (1 and 2). Consequently any four list members at `a = 3n/4-1` have
affine rank `s in {2,3}`.

Caution recorded (it looked like a rigidity theorem and is not): pinning the
generalized Hamming weights at the MDS floor `d_j = R+j` makes the rank-flat cap
appear to force `b=0` at `s=2`. That holds ONLY at minimum support `d_2=R+2`; the
cap is not monotone in `d_2`, and the `b`-budget grows to ~4.5e10 at `d_2=3n/4`
and is vacuous once `z` is small.

The cited `RS[F_17,F_17^*,8]` four-codeword witness at agreement `11=3n/4-1` is
now banked as exact integers (12 exist in the normalized branch; one pinned).
Measured: affine rank `s=3`, generalized weights `(9,12,14)`, `z=2`, `g=2`,
`b=0`, all six pairwise agreements exactly `K-1=7` (every difference is a
minimum-weight codeword), and **no triple collinear**. Both compilers give cap
`8` against the actual list size `4` — slack 4, i.e. neither is within a factor
of two of tight on the only concrete configuration on record.
