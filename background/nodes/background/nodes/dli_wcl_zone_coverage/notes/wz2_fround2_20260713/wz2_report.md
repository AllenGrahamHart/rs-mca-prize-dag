# wz2_report.md — F-round 2 verdict: WCL-ZONE-COVERAGE **SURVIVED** (both parts), dedup-spec debt discharged with one major interface finding

- **Node:** `dli_wcl_zone_coverage` (F-rounds now 2/2 survived).
- **Round design:** PART 0 spec first (`wz2_dedup_spec.md`), then
  pre-registration (`wz2_falsifiers.md`) BEFORE any computation; exact
  tables `wz2_results.md`; catches `wz2_findings.md` (wz2-C1..C8); raw
  data `wz2_shard_*.json` + `wz2_log_*.txt`; enumerator
  `wz2_census_modal.py`; evaluator `wz2_eval.py` +
  `wz2_eval_report.json`. 14 Modal apps, all exit 0; controls all green;
  round-1 cells and banked M2 cells reproduced EXACTLY under the new
  module (raw path), as mandated.

## Verdict per part

- **PART 0 (dedup canonical spec, #191/wz-C2): DISCHARGED.**
  `wz2_dedup_spec.md` is an implementation-grade canonical spec grounded
  clause-by-clause in the banked machinery (M2 enumerator, census
  weight-bounded multiplier closure + union-find + min-weight generator,
  round-7 exact division, census lift identity, round-1 freeze), with an
  explicit 8-item ratification list (below) where the banked record is
  silent or split. Implemented as a standalone module with a 10-test
  conformance suite + 5 deterministic mutation controls — 12/12 replay
  checks green. The spec's own consistency probe (section 6) produced
  the round's major finding: **with the pose's deduplicated ledger, C1'
  fails EXACTLY at the banked accident row (L=1, q=7937): W_cl 236 -> 8,
  K'_dedup = 6.5019 > 4** (wz2-C1). The M3 CORRECTED POSE uses one
  symbol W_cl for two ledgers that cannot coincide; pre-declared NK-5
  (an interface finding, not a WCL-ZONE kill), but it BLOCKS the node's
  downstream assembly as written.
- **PART 1 (family-B trend, #193/wz-C4): SURVIVED-WITH-EXPLANATION.**
  Pre-registered kill: monotone rho over (b10,b12,b14,b15,b16) AND
  top/bottom >= 4 AND >= 4 new-band witnesses with >= 2 in b16. Outcome:
  rho = 1.615, 2.395, 4.648, **3.62, 0.00** — turnover at b15, b16 empty
  (0/384 vs 0.106 null). The explanation branch (also pre-registered)
  is satisfied: new bands Poisson-consistent; the b14 octave is
  enriched (b14-deep: rho 6.71, a ~1% event) but bounded; the family
  carries a ~2x O(1) level-correlation factor with NO growth in scale.
  Round-1's only sustained trend is resolved as a small-K artifact.
- **PART 2 (odd-n' mixed channel, #192/wz-C3): SURVIVED.** KILL-O1
  (generic saturation / recurrence): no trip — generic populations track
  the Poisson null at both odd tower widths and all levels (rho_gen
  1.01..2.28, non-monotone, no saturation; 0 recurring generic keys).
  KILL-O2 (semi-forced growth): no trip — rates flat, the
  norm-statistics expectation. The forced channel exists EXACTLY as
  algebra dictates and no further: forced ledger = {orbit(Phi_{n'})} at
  every one of 108 L=1 cells, absent at L >= 2; all semi-forced
  witnesses are even-weight 2-power-factor multiples with
  exactly-verified norm divisibility; O96L3 is empty. Round 2 also
  BANKED the fixed-vector exclusion lemma (wz2-C3): no fixed integer
  vector is forced at any official level, so the officially live mixed
  channel is q-dependent constructions only.

## What this round proves and cannot prove

Evidence weight added: q up to 2^29, n' in {64, 96, 192} (first
composite/odd-part towers, where forced families EXIST and were found to
be exactly the algebraic ones), L in {1, 2, 3}, 1,272 band cells + 13
replay/audit cells, plus the exact-dedup audit of 8 banked rows. Still
untouched (unchanged from round 1): official-row-specific accidents (the
A1-PROD density-vs-row gap — no analogue census can see them),
q-dependent forced constructions at official n'_L (probed only via
saturation statistics at analogue scale), L >= 4, and any qualitative
change between 2^29 and 2^256.

## Dedup-spec ambiguity list (RATIFY-1..8, maintainer decisions owed)

1. **RATIFY-1** cross-orbit total order: (w, sparse-rep lex) [round-1
   freeze, default] vs (w, dense M2 orbit_key lex).
2. **RATIFY-2** literal 2N mass for degenerate orbits (default literal =
   pose letter; overcharges forced orbits 6x at n'=96, anti-conservative
   on the C1' side).
3. **RATIFY-3** shadow ownership by connected component (default, per
   census + empirical_M_ledger) vs direct-witness-only.
4. **RATIFY-4** singular-source witness scope: weight-<=3 sweep
   (default, banked closure precedent) vs factor-wise exact division
   (spec Appendix A). LOAD-BEARING at official rows with odd(L) > 1
   (wz2-C6).
5. **RATIFY-5** lift maps for all k >= 2 (default yes; k=2 banked 57/57,
   k=3 now data-validated 96/96).
6. **RATIFY-6** lift gate = C1'-admissibility of the source row
   (default, round-1 freeze). LOAD-BEARING: flips the forced mass 12->0
   per cell purely on the companion's balance condition (wz2-C5).
7. **RATIFY-7** lift source object: any primitive vanisher of matching
   weight (default) vs source-window-restricted — divergent only
   cross-level (official tower).
8. **RATIFY-8** composition order lift->shadow (default; observed
   immaterial on all replay/audit cells, material in principle).

## Round 3 (recommendations, in priority order)

1. **The blocking item is no longer a falsification round.** wz2-C1
   must go to the maintainer: repair the M3 interface by EITHER (a)
   dropping the dedup phrase from WCL-ZONE (zone bound prices the RAW
   primitive ledger; dedup then only lives in bookkeeping upstream), OR
   (b) re-posing C1' against the deduped ledger — in which case its
   literal K' <= 4 form is already refuted at q=7937 and a new allowance
   shape is needed. Until ratified, censuses should report BOTH ledgers
   (raw + canonical dedup), as this round's artifacts do.
2. Family B is resolved; the escalate pre-commitment (K=1536 at b15-b17)
   is NOT triggered and should not run. The L-dimension is the thin
   direction: an L=3/L=4 analogue family at n'=64 (aspect-admissible
   N=48/64 rows) would test whether the O(1) correlation factor
   compounds with depth.
3. The odd-n' channel's remaining official risk is q-DEPENDENT
   constructions: a targeted round could implement the subgroup-sum
   family (support on the index-(q-1)/n' multiplicative subgroup) as an
   explicit PLANT-style generator and measure whether any variant lands
   in official-shaped windows with level survival — extending wz2-C3
   from fixed vectors to the parametrized family.
4. Certificate design input (from wz2-C4): at composite-n' rows a
   complete-window certificate can price the tagged populations by
   resultant enumeration (finite, exact per candidate); the generic
   population is the only part needing the Poisson-null argument. This
   decomposition mirrors the emptiness-vs-counting dichotomy of wz-C1.

## Status line for the DAG

dli_wcl_zone_coverage: F-rounds 2/2 survived. Still a TARGET; nothing
here promotes it. The round discharged the #191 dedup-spec debt
(canonical spec + reference module + conformance suite, 8 RATIFY items),
resolved the #193 family-B trend as a bounded O(1) correlation factor,
probed the #192 odd-n' mixed channel (forced structure = exactly the
algebra, nothing q-robust beyond it, fixed-vector official transport
PROVEN impossible), and surfaced one blocking interface finding (wz2-C1:
deduped-C1' exactly fails at q=7937) that must be resolved by the
maintainer before the node's downstream assembly can be used.
