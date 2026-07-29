# Upstream July wave (0f7476f0): bracket unchanged, two facts banked

Harvested 2026-07-29. Status unchanged; the bracket k+2^34 <= a_L <= a_IJ
does not move.

## 1. Our floor construction is now Lane L's lower champion (PR #1101)

The "zero-remainder boundary of the quotient-rotation construction" — an
extension of OUR `rate_half_cyclic_rotated_prefix_floor` (exported as PR
#1051) — is now the declared-field rate-half lower champion, with certified
size bits(L_1) in [1,466,604,010,422 ; 1,467,447,159,516] at agreement
a = k+2^34-1 on q_0 = 3*2^41+1. Same agreement boundary as our bracket's
lower end; the declared field is NOT prize-admissible (B* = 0 there), so it
adds lineage validation and shape evidence, not bracket movement.

## 2. Route triage: the packing bound cannot tighten our upper end

PR #1099's interpolation-packing bound L <= C(n,k)/C(a,k) is field-
independent, which made it a candidate for the safe side of our crossing.
Triage (2026-07-29, lgamma arithmetic): at B* <= 2^128 it certifies safety
only within ~128 grid points of FULL agreement (each step from a=n costs
~log2(n/(n-k)) = 1 bit), against our existing Johnson upper end at ~0.71n.
**Do not chase it.** It is a Lane-L size tool, not a threshold tool.

## 3. Fence inherited from the fixed-G boundary (PRs #1089/#1103)

At the adjacent fixed-G pair, the complete Johnson-scheme Hahn relaxation
gives L <= 20,737,821 — still 3,960,607 above target — with matching primal/
dual certificates, and the complementarity identity shows selected-support
optimization is target-equivalent, not an independent bridge. Any route for
this node using only the pairwise Johnson distribution is therefore fenced.
