# Petal growing-excess census (Modal) — INCONCLUSIVE, two flags

Ran the banked petal census tooling (gate PASS; witnesses A,B pass) over
calibration rows p in {1009,2003,4001,8009}, ell=2, t=3, c=2..3 (scan reached
c=2,3 in budget). Result per row (identical across all four primes):

    c=2, d=4: residue_line_count=1, dim_K=4, exact_realizable_extras 0/210
    c=3, d=5: residue_line_count=0, dim_K=6, exact_realizable_extras 462/462

## Why this does NOT resolve the c-independence claim
1. RAW vs UNCHARGED: the terminal payload asks for c-INDEPENDENT UNCHARGED
   extras (after charging paid coset/pullback families). The census reports RAW
   realizable extras. The 0->462 jump is a threshold at tiny params (0/210 ->
   ALL 462/462), and is exactly the CHARGED coset mass expected to grow; it does
   NOT measure the uncharged residual that the claim bounds. So raw growth is
   NOT the falsifier.
2. dim_K vs LEMMA 13: raw dim_K = (d+1) - residue_line_count = 4 at c=2 exceeds
   the Lemma 13 bound c+1 = 3 (petal_residue_kernel_linear_bound, PROVED). So
   the census's raw K is a DIFFERENT object than the lemma's charged-quotient K
   -- a scope discrepancy. FLAG for content audit: reconcile the census raw
   kernel with petal_residue_kernel_linear_bound's hypotheses.

## What a decisive census needs
Extend the tooling to CLASSIFY each realizable extra as charged (coset /
multiplicative-pullback / dihedral -- the paid families) vs uncharged, and test
whether the UNCHARGED count and its bound exponents are FLAT in c across
c=2..8. Only the uncharged residual bears on the payload. Raw counts and raw
dim_K are the wrong metric.
