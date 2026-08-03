# Wave-43 audit — 433-1b: CELL 14 CLOSED (1680/1680) + the cell-3 DE block

**Date:** 2026-08-03. **Planner:** Fable. **Range:** `589b30b25..codex-wave43`
(head `6bc692e8`; worker-authored delta = ELEVEN substantive commits, one
node each; the remaining commits are merges of our canonical master).
**Verdict: CLEAN — integrated in full, two forced pin corrections.**

```text
dag.json merge: their graph (1764/4900) = ours (1753/4860) + 11 new
PROVED background nodes + 40 new edges, with ZERO drift in their
copies of our nodes (norm-gate mint, band mint, Route-T statement
edits all absorbed exactly). Merged by append; canonical dump;
verify_prize_dag PASS. All 11 new nodes feed rate_half_band_closure
as `ev` (TARGET in-edge law respected).
```

## What fell

**Cell 14 of deployed positive `433-1b -> O0a` is CLOSED.** The raw
outside ledger `4 signs x 4 lanes x 7 missing records x 15 matchings
= 1680` is tiled by four disjoint exact exclusions, each PROVED empty
over `F_2130706433`:

| node | cases | mechanism |
|---|---:|---|
| `cell14_linear_pair_outside_exclusion` | 144 | missing-de + residual-de pair: target-free linear projection; 144 open + 1632 boundary ideals all UNIT |
| `cell14_rankone_target_projection_exclusion` | 960 | all 4 non-de missing roles x all 15 matchings: rank-one `a f^2 = uv` substitution, 3 eliminant classes, 12,880-root replay |
| `cell14_fixed_a_rankone_chain_exclusion` | 432 | missing-de, matchings {3,4,5,9..14}: fixed `a = ±B/A` torus chain, FLINT eliminants, 9,456-root replay |
| `cell14_fixed_a_rankone_allmixed_exclusion` | 144 | missing-de, matchings {6,7,8}: complete double resultants + exact factor-removal; retained frontier NONE |

Partition completeness hand-checked AND machine-checked: matchings
{0,1,2} are provably exactly those pairing the two residual de records
(the audit checker enumerates all 15 and asserts membership both ways);
{0,1,2} u {3,4,5,9..14} u {6,7,8} = all 15; 3x15x16 + 4x15x16 = 1680;
the all-mixed verifier recomputes the global tiling (`cell14=1680/1680`).

**Cell 3 (7 nodes): structure + the complete DE block.**
`compact_curve_kernel` (24 charts, dimension-1 common curve, unit
beta-boundary after re-saturation, sign-independent 8-coordinate
polynomial kernel) and `global_quadratic_quotient` (block-lex
compression to base + palindromic quadratic in `b` + linear recovery
in `c`, 240/240 exact reductions) are structural theorems.
On them: xi0/pairing0 (16 cases, six-basis norm certificate),
xi1/pairing0 (16, pure parallel-edge transport — proof read line by
line, sound: records 0 and 1 are literally `de`/`(d+e)^2` twins, and
pairing=0 pairs adjacent residual positions, so the two guarded
systems are IDENTICAL), xi2/pairing0 (16, negative-DE variant),
`de_firstpair_complete_exclusion` (the full 144-case block xi in
{0,1,2} x pairing in {0,1,2}), `de_pairing3_complete_exclusion` (48).
Paid DE block: xi in {0,1,2}, pairing in {0..3} = 192 raw cases.
Cell 3 remains OPEN (nonclaims explicit in every statement).

## Catches

- **CATCH (ours, worker-repaired): stale census pins.** Our coordinated
  bundle repriced the census to 242 = 179/38/25 but never updated
  `tools/verify_orbit_census.py` / `tools/verify_critical_harness_coverage.py`
  / `notes/CRITICAL_HARNESS_COVERAGE_20260722.md`, which still pinned
  241 = 179/38/24 (last touched wave 26) — the census verifier would
  have FAILED if run and was simply never run post-bundle. The worker
  applied the Route-T reprice on their side; their versions ADOPTED.
  Both tools now PASS: math 242(179/38/25), submission 257(191/40/26).
- **Forced pin corrections (2, applied under standing authority):**
  `cell3_xi1.../verify_audit.py` pinned "next ... is `xi=2`" in a
  frontier the xi2 commit legitimately rewrote; `cell3_compact_curve_
  kernel/verify_audit.py` pinned "FLINT" in a frontier rewritten around
  the quadratic pair algebra. Pins updated to the current markers,
  commented in place. Worker hygiene note: later commits must re-run
  earlier nodes' audit verifiers when they rewrite their frontiers.
- Roadmap: the worker's copy preserved our r3.1 addendum + wave-42
  ported entry AND corrected the stale preamble census lines (241/24 ->
  242/25) our addendum had only superseded, not rewritten — adopted
  wholesale (no clobber this wave; dag/roadmap/manifest were excluded
  from the bulk checkout per the wave-42 hygiene rule, then roadmap
  adopted deliberately after content verification).

## Verification

All 11 `verify.py` + 10 `verify_audit.py` replayed under ramguard
local: PASS (after dag merge; the verify.py scripts pin dag membership,
so they correctly failed pre-merge). Harness replay via manifest:
`--run --match positive_433_1b_cell14` -> 10/10, `--match
positive_433_1b_cell3` -> 14/14 (includes wave-42 node re-replay
against its updated frontier). Manifest refreshed (2375 scripts).
`verify_prize_dag.py` PASS. Compute-log entry (`PRIZE_COMPUTE_REQUESTS`,
cell-14 linear-pair census, <$3, timeout-replay custody) adopted.

Storage: the 116 MB all-mixed raw ledger exceeds GitHub's 100 MB limit
and is stored as `...allmixed_result.json.gz` (dli_wcl precedent); its
node's `verify.py` digest() decompresses transparently, so the pinned
sha256 of the RAW bytes is unchanged — replayed PASS. The 52 MB
fixed-a flint ledger stays RAW: its audit re-runs the custody-pinned
census script, which reads the raw file, and the frozen provenance
("do not alter") forbids repinning that script.

## Watches

- **Export #1143: cell-14 CLOSURE is now audited and eligible** — the
  natural next export batch is wave-42 (kernel-denominator boundary) +
  wave-43 cell-14 closure as one packet; the worker's own frontier
  says "downstream rate-half consumer or upstream finite-packet
  export; do not decompose cell 14 further".
- 433-1b remaining: cell 3 outside ledger beyond the DE block (xi=3
  no-go routes recorded: 8x8 Sylvester and Euclidean quartic
  resultants both capped; worker route = lower-degree/shared-f
  elimination or pairing-separated projection; pairing=4 backend test
  named as next), plus the other open cells of the 15-cell atlas.
- All exclusions are deployed-prime exact (`F_2130706433`), NOT
  characteristic-uniform — the audit notes say so honestly; any
  eventual band-closure consumption must respect that scope.
- New pin: `6bc692e8`.
