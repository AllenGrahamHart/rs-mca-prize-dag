# wz_report.md — F-round 1 verdict: WCL-ZONE-COVERAGE **SURVIVED**

- **Node:** `dli_wcl_zone_coverage` (was: zero F-rounds; this is round 1).
- **Round design:** pre-registered in `wz_falsifiers.md` BEFORE any
  computation; exact tables in `wz_results.md`; catches in
  `wz_findings.md`; raw data `wz_shard_*.json` + `wz_log_*.txt`;
  enumerator `wz_census_modal.py`; evaluator `wz_eval.py`.

## Verdict

**SURVIVED**, controls all green. No kill line tripped:

- KILL-1a (forced-structure saturation): no trip — every sub-volume band
  sits near its Poisson volume null.
- KILL-1b (recurring orbit family): no trip — 673 orbit keys, zero
  recurrences across primes (2-power n' makes strict forced families
  algebraically impossible; see weight caveat below).
- KILL-2 (scaling anomaly): no trip — L=1 families A (N=32) and C (N=64)
  track the q^-L volume law across 2^17..2^27 with non-monotone rho
  ending near 1; L=2 family B is monotone-up (rho 1.62/2.40/4.65) but
  below the pre-registered 4x-and-3-witnesses threshold.
- KILL-3 (integrity): 12/12 banked M2 cells exact on both engines; both
  mutation controls and the lift control tripped as required; zero
  orbit-closure flags; N=64 engine cross-check green on a nonempty cell.

## What this round proves and cannot prove

Evidence weight: analogue rows only — q up to 2^27 (official ~2^256), n'
in {64,128} (official 512L, with odd part for most L), L in {1,2}
(official 1..34), 264 band cells + 12 positive controls. Within that
range, the exceptional mass behind W_cl behaves exactly like the volume
null and shows no q-robust structure. The round CANNOT rule out:

1. official-row-specific accidents — the A1-PROD density-vs-row gap that
   is the node's core difficulty stands untouched (a 7937-style accident
   at either official field cannot be excluded by any analogue census);
2. the odd-n' forced-family channel (invisible at 2-power n', wz-C3) —
   though pure subgroup-sum relations are excluded at all official levels
   by the pre-hoc argument recorded in the pre-registration;
3. L >= 3 behavior, and growth of the L=2 correlation excess (wz-C4);
4. any qualitative change between 2^27 and 2^256.

Structural findings sharpen the node itself: WCL-ZONE is an EMPTINESS
predicate at official L <= 12 and a counting predicate only at L >= 13
(wz-C1), and its dedup conventions have no canonical implementation yet
(wz-C2, wz-C8) — both belong in the node notes before proof work.

## Round 2 (pre-commitments for the next falsification pass)

1. **B-family resolution (primary):** L=2 bands b13-b16 with >= 96 primes
   each (cheap: ~0.2s/prime on the mitm enumerator), plus a
   correlation-corrected null built from the banked f2b level-correlation
   data. Kill line to pre-register: rho(B) monotone with top/bottom >= 4
   AND >= 5 nonempty top-band witnesses (tighter statistics than round 1).
2. **Odd-n' channel:** cells at n'=96 (N=48, L=1, window w<=6, mitm
   feasible) and n'=192, where z^N+1 factors and forced families are
   algebraically possible — direct search for orbit keys recurring across
   primes, which round 1 could not see in principle.
3. **Composite forced constructions at official n'_L:** algebraic search
   (resultant-gate style) for products m(z)*P(z) landing in windows with
   level survival, extending the pure-subgroup exclusion of wz-C3.
4. **Spec work (not a falsifier):** canonical first-owner dedup
   definition + composition order (wz-C2/C8) so future censuses and any
   certificate format are comparable.

## Status line for the DAG

dli_wcl_zone_coverage: F-rounds 1/1 survived (this round). Still a
TARGET; nothing here promotes it — the round only establishes that the
predicate is not refuted by the structure it quantifies over at analogue
scales, and it materially clarified what a proof must certify (emptiness
at L <= 12 per row, counting at L >= 13, pinned dedup).
