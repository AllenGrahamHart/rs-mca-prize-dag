# Wave-44 audit — 433-1b cell 3: the DE block extends to pairings 4 and 5

**Date:** 2026-08-03. **Planner:** Fable. **Range:** `6bc692e8..codex-wave44`
(head `0a10b725`; worker-authored delta = TWO substantive commits, one
node each). **Verdict: CLEAN — integrated in full.**

Merge: their graph = ours + 2 PROVED background nodes + 4 edges (ev x2
into `rate_half_band_closure`, req x2 from the quadratic quotient);
zero adoption of their stale copy of our re-posed band TARGET
statement (ours is newer — checked, ours kept). DAG 1770/4910.

## What fell

`cell3_de_pairing4_complete_exclusion` (48 raw cases: xi in {0,1,2} x
4 source signs x 4 target lanes at pairing 4; 8 source rows, 64 lane
checks, 0 witnesses, 8 boundary records all exactly f = 0) and
`cell3_de_pairing5_complete_exclusion` (48 raw cases; 16 source rows,
96 lane checks, 0 witnesses). Paid DE block now xi{0,1,2} x
pairing{0..5} = 288 raw cases. Same FLINT low-degree backend as
pairing 3 (wave 43); nonclaims explicit (no other matching, cell-3,
K3, LIST, MCA, or Prize closure).

## Verification

Both verify.py + verify_audit.py replayed PASS under ramguard after
the dag merge; verify_prize_dag PASS; census unchanged 242(179/38/25);
manifest refreshed. Worker roadmap adopted (strict superset: +2
work-cycle entries; 0 lines lost). Bulk checkout excluded
dag/roadmap/manifest per the hygiene rule.

## Watches

- Cell-3 remaining: pairings 6..14 of the DE block + xi >= 3 records
  (worker's no-go ledger stands); export batch candidate once the DE
  block or cell 3 closes.
- New pin: `0a10b725`.
