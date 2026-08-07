# PRE-REGISTRATION — L1-N10-ELL: the decisive ell-sweep (round 22)

Round 22, 2026-08-07. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: execute the compute
request of record L1-N10-ELL at reachable local scale and attempt to
fire falsifier F-w1. This is mystery 6's first post-re-pose test.

## 0. Sources (quote verbatim first)
- critical/nodes/l1_mixed_petal_amplification/statement.md — the
  Round-21 diagnosis addendum (the re-pose L1-MPA-w, falsifiers
  F-w1/F-w2, the BOX law Lambda = 2*ell+b-2).
- notes/pilots_20260807/l1_pma_diag/ — REPOSE_DRAFT.md,
  d3_ell_sweep.py, a5_scale32.py, a3_exhaustive_exact.py: REUSE this
  machinery (it is coordinator-replayed); do not rewrite from
  scratch what already verifies.
- experiments/prize_resolution/l1_balanced_mixed_growth_census_result.md
  — the banked N10 numbers and schedules.

## 1. Deliverables
- (D1) THE SWEEP: exact retained counts at n=32, ell=2,3 (both
  scalar schedules + the minimal-degree word), and n=24 extended to
  ell=5,6. Attempt n=32 ell=4 ONLY if it fits ramguard local
  (1G/5min per invocation; you may checkpoint across invocations via
  files in YOUR OWN dir). If a cell does not fit, report its exact
  cost (candidates, memory, time estimate) and SKIP it — spec it as
  a Modal request line for the coordinator instead. You may NOT
  launch Modal jobs.
- (D2) THE F-w1 TEST at every completed cell: does any word exceed
  10*BOX(ell)/q? Include adversarial words per cell (minimal-degree
  word mandatory; a filter-guided + random search like a5's; note
  the round-21 finding that the exhaustive max at n=16 was NOT
  filter-extremal, so do not trust the filter to find the max —
  say what your search can and cannot conclude).
- (D3) THE LAW IN ELL: does retained ~ sum_m N_{k+m}(ell) q^{-m}
  (the random-word law) continue to hold as ell grows, or does a
  mixed-petal amplification signal emerge? Derive N_{k+m}(ell)
  closed-form first (extend the round-21 derivation), predict, then
  measure. Prediction before measurement, per cell.
- (D4) THE CLAUSE-(b) SHAPE: the trend of retained/(BOX/q) in ell
  at fixed n — flat, growing, or shrinking? What does the trend
  predict for the ell = Omega(n/log n) regime, stated as an honest
  extrapolation with its epistemic label?

## 2. Falsifiers / honesty
- If F-w1 FIRES (a word with retained > 10*BOX(ell)/q): the
  re-pose must be re-drafted around the witness; report the witness
  with a reproduction script and STOP the positive line. That is a
  successful outcome.
- If F-w2 fires (any contributor at sigma > 2*ell+b-2): clause (a)
  is killed — report immediately, highest priority.
- Census evidence is evidence, never proof; label throughout.
  Search maxima are lower bounds on true maxima — label them.

## 3. Rules
- DRAFT ONLY in notes/pilots_20260807/l1_ell_sweep/. Never edit
  dag.json/nodes/tools; no git; no Modal. COMPUTE LAW: every python3
  invocation via tools/ramguard tiny|local -- python3 ... (literal
  --), from repo root, INCLUDING file patching and JSON peeking.
  2-power grids where a grid is yours to choose (n=24 cells are
  allowed here: they extend the banked round-21 baseline, which is
  the comparison of record). Name every measured functional
  (CATCH-19C). Verbatim quotes with file:line. No REPORT.md — your
  final message IS the report. QUARANTINE: do not read
  notes/pilots_20260802/CAMPAIGN_LEDGER.md at or past line 2487
  (the "ROUND 22 LAUNCHED" marker); do not read the other round-22
  pilot dirs (ge_floor_falsifier, bb_nu_transport, f2_rlocality);
  PASS THIS QUARANTINE CLAUSE VERBATIM to any subagent you dispatch.
