# FM0-FM2 — split-fibre first-match selector pilot (2026-08-02)

> **Verdict: OUTCOME-A, conditionally — and the condition is the
> undefined selector order.** At every point where the selector has real
> choice, the split-fibre witnesses are NOT first matches (intended rank
> ~ median of W_z). Under SUPPORT-KEYED orders (LEX/COLEX), |Gamma_lo|
> collapses 89-97 -> 0-4. Under POLYNOMIAL-KEYED and random orders:
> ZERO compression (91-97/97, near-Sidon) — **K1 is live under those
> orders.** 4125/4125 exact checks PASS across ten parameter points.
> Pilot by an Opus 5 subagent; audited by Fable (FABLE_AUDIT.md).

## FM0 — the headline finding

**`prec` is nowhere defined in the repository** (bridge L38,
canonicalization contract L5, audit L57 all say "a fixed order").
PP4.0 was adopted but never written. Eight ambiguities catalogued
(A1-A8) in SELECTOR_MANIFEST.md; FM2 proves A1 (supports vs polynomials)
and A2 (lex vs colex) are OUTCOME-DECIDING.

## Lemmas proved (data-confirmed exactly)

- **L1:** W_z and W_w are disjoint for z != w (shared S forces
  deg V < K against deg V = A-m >= K). No selector can compress by
  support collapse.
- **L2:** distinct-slope exact-A supports meet in at most A-m =
  K+(h-m); observed max core = A-m exactly in all ten cases.

## FLAG for adjudication

The bridge asserts post-strip cores <= K and defines Gamma_hi by core
= K. For h > m (including RowC 1/4: A-m = 257 = K+1), globally generic
strip-free pencils have selected cores of K+1 (P3: 17/97 slopes with
core >= K+1 and never exactly K; P6: 24; P5: 46/46). Either the
generic-branch hypothesis must strengthen (no joint pair on > k points)
or Gamma_hi must widen to {core >= K}. Statement-level repair on a
PROVED node — planner adjudication required. See FABLE_AUDIT.md.

## FM2 measurements (key rows)

Intended witness selected first (LEX/COLEX/POLYLEX/HASHx2): P3 2/2/0/0,0
of 95; P4 0/0/0/0,0 of 55; P7 0/0/-/0,0 of 89. Control P5 (no
competition): 4/5/5/5,5 of 6.

|Gamma_lo| under orders (candidate counterfactual = all live slopes):
P4: LEX 3, COLEX 3, POLYLEX 97, HASH 95/93 (of 97).
P3: LEX 1, COLEX 4, POLYLEX 91 (of 97).
P7: LEX 1, COLEX 0, HASH 97/97 (of 97).

Selected witnesses are NOT low-complexity codewords (deg p = K-1 at
97/97 under LEX) — the structure lives in the SUPPORTS: all selected
supports share a low-index prefix/window ({x_0..x_4} at P4; width-19
window under COLEX).

Competition-depth sweep (same shape, varying q): 6857 witnesses/slope ->
Gamma_lo 3.1%; 1725 -> 4.7%; 330 -> 1.6%; 117 -> 45.1%. Compression is
a WITNESS-DENSITY effect, breaking below ~10^2 choices/slope. At
official scale log2|W_z| ~ 668 even at the smallest super-budget q
(extrapolation, not measurement).

## Honest limits

Budget untestable at pilot scale (M <= N^2 everywhere — the audit's
vacuity bound re-derived). The collapse is QUANTIFIER-driven: greedy
pairwise-low-core subfamilies of the selected family remain 34-60% of
slopes and near-Sidon; P-B's "meets EVERY other" quantifier does the
final ejection — the route should not lean on that fragility. Collapsed
slopes land in Gamma_hi (P-A1, same 8n^3): the mechanism RE-ROUTES
mass; an exchange theorem must pair with a P-A1 accounting statement.

## Recommendations (adopted per FABLE_AUDIT.md)

1. Write PP4.0 as a SUPPORT-KEYED order — surfaced decision.
2. FM3 target: the prefix/shadow theorem (lex-first-match forces
   selected supports to contain {x_0..x_{K-1}} at sufficient density
   => Gamma_lo empty).
3. Pair with P-A1 accounting or the budget argument is circular.
4. Adjudicate the bridge flag before wording FM3.

(Artifacts: SELECTOR_MANIFEST.md, pb_split_fibre_pilot.py,
fm2_aggregate.py, fm2_shape_probe.py, RESULTS.json, results_P*.json,
shape_P*.json.)
