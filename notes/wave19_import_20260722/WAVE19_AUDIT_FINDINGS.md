# Wave-19 fresh-context replay audit + master integration — v7 (XR uniform-branch emptying + DSP8 P24/P25 satellite reduction + HGE4 dual width cap; first time-rule-compliant Modal launch)

Audit agent: 20+ consolidated checks, replay battery 81/81 at pin, mutation
controls 6/6, validator PASS. Master integration same session. Full audit
detail in the session scratchpad (w19_findings.md); this note is the
banked record.

## PINS
- v7 pin **a962c045** ("Exclude reciprocal C2 affine shard"); base = wave-18
  pin b5e5e884; range 43 commits. Master at integration start: 16604899.

## VERDICT
**NOTHING CLOSES.** +37 nodes (all PROVED reductions/fences/compilers/
certificates, explicit no-close disclaimers), +133 edges, **0 base->pin
status flips** (verified exhaustively). The master-vs-pin "flips"
(descriptor, dli, baseline) and the "removed" c1r3 node are LINEAGE SKEW:
the branch predates the 2026-07-21 Decisions 6-8 surgeries; Codex touched
ZERO dli/descriptor files in the range (git diff --name-only: 0 hits).
Ceremony survival asserted at import (statuses, req edges, the c1r3 mint,
descriptor PROVED) — all CONFIRMED post-merge.

## ADOPTION (the wave-19 standing checks)
- **Decision-5 time rule: ADOPTED VERBATIM** + a pin-side STRICTER overlay
  (sub-$1 credit ceiling retained on top of the 5-minute rule; "the
  five-minute ruling does not authorize a short but expensive
  many-container fleet") — adopted to master with the r3 pointer
  re-inserted.
- **DSP8 parity supersession (w18-C1): byte-identical** pin vs master — no
  supersession-on-supersession.
- **Section C**: no new corridor divergence (the only master-vs-pin edge
  deltas anywhere are the 4 ceremony edges).
- **r3 roadmap**: pin predates it (chronologically impossible to carry);
  adoption check ROLLS to wave-20.
- **First Modal launch under the time rule: COMPLIANT.**
  ap-Ifv7cgmA0WCon3SfgP1aSo — 16 shards, 32.6s total (max shard 3.13s),
  $0.25 ceiling, registered + hash-pinned + logged "do not rerun". The
  governance loop (Decision 5 -> Codex adoption -> compliant exercise)
  closed in one wave.

## CLUSTERS
- **DSP8 P24/P25 (6 nodes)** — the max-P<=24 satellite REDUCED, not closed:
  exact iff (max P<=24 <=> G_12^neq | H_D, checker only); P=25 encoded
  three ways (exact odd-prime-support scalar; <=4,048x4,072 and
  <=2,378x2,402 quadratic towers, char-0 empty); compiler degree halved
  (67,092,481/25 gens -> 33,550,336/13). "Vacuity" = the satellite route
  (P>=25 locus empty => DSP8 with zero retained records => C36' analytic
  close), NOT the vacuous-rounds concern — separately addressed: "the
  P(t)>=21 watch ... is falsification telemetry, not the falsifier."
  Residual: implementation + cost + the bands 25<=P<=32/34.
  correlation_bound stays TARGET; the 3-amber cascade NOT triggered.
- **XR (29 nodes)** — the uniform prize branch EMPTIED to million-scale
  floors (11,243,370 / 9,629,972 / 2,241,633); the live frontier moves to
  large-flat-nullity NONUNIFORM cells (u+v >= those floors, v <= 1.53B/
  2.90B/1.96B wedge). First-open selector ranks 5,5,5 / 17,17,15 STILL do
  not move. xr_tangent bridge 12->21 ev; residual shrinks to generic-chart
  aggregate + repeated-core aggregate (or the static (n-A)(E-1) route) —
  the roadmap's A6 cheapest-closure candidate got cheaper. P-B untouched.
- **HGE4 (1 node)** — dual width cap h <= min(m/4-1, 2*ceil(ma/8s)-1) +
  parity; ~2.8e10 width-cells deleted; "a width exclusion, not the
  remaining aggregate payment" — ERT4'''' untouched.
- **c1c2 (1 node)** — reciprocal selected-antipodal shard emptied
  (40-squaring trace test, the compliant Modal screen); nonclaim intact;
  adjacent_crossing 109->110 (pose re-taken atomically, PASS).

## INTEGRATION RECORD
+37 background folders; +133 edges; the 4-file experiment packet
(reciprocal affine torsion) co-landed with its consumer; adjacent_crossing
pose re-taken (110 brackets); CR ledger adopted from pin (master snapshot
at notes/wave19_import_20260722/) with the r3 pointer re-inserted; dag
1030->1067 nodes, 2294->2427 edges; validator PASS; new-node battery 75/75
replayable + 1 remote launcher (correctly excluded, manifest 855/14/1105);
blast-radius 191/191; ceremony survival asserted in the merge script.
Board: 208/33/22 critical surface unchanged.

## INFO
- The known duplicate edge (petal_descent bridge) persists in all three
  trees; unique count = raw - 1.
- dli folder moves were 13 (not 12 as earlier recorded).
- xr_highcore gained 3 schema-tolerated scope fields.
