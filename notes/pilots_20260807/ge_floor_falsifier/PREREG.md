# PRE-REGISTRATION — MYSTERY 5: the FLOOR-GE falsifier search + GE-WEAK first positive (round 22)

Round 22, 2026-08-07. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: attack FLOOR-GE with
its own pre-registered falsifier; if it survives, do the first
positive work on the GE-WEAK obligation.

## 0. Sources (quote verbatim first)
- notes/pilots_20260807/gen_economy_diag/ — the round-21 diagnosis
  of record: FLOOR-GE (2-power-norm bases certify <= N'+1 centers;
  exhaustive at N=8,16; sampled-null at N=32; conjectural above),
  ESCAPE-GE (any >N'+1 family needs an odd-prime-norm base), the
  registered falsifier, REPOSE_DRAFT.md (GE-WEAK).
- critical/nodes/generator_economy/statement.md — the round-21
  addendum (collision catch, contract, GE-WEAK re-pose of record).
- critical/nodes/integer_code_distance_cert/statement.md — the
  probe-1 verdict addendum (ell = 1 permanent; ell' = 65 needed)
  and the node's explicit system.
- critical/nodes/lattice_cone_certificate (if the node exists under
  this or a nearby id — locate it; the gen_economy_diag D4 priced
  it) — the per-row certification route.

## 1. Deliverables
- (D1) THE FALSIFIER SEARCH, executed: search for a base set
  containing an odd-prime-norm element that certifies > N'+1
  centers. ESCAPE-GE says this is the ONLY class that can beat the
  floor — search it specifically: exhaustive over small odd-prime-
  norm bases at N = 8, 16; structured search at N = 32. Register
  the search space and its completeness class BEFORE running
  (exhaustive / structured / sampled — label which).
- (D2) THE VERDICT: FLOOR-GE survives (falsifier exhausted at small
  N, evidence-graded above) or DIES (witness family found, with
  verifier). Either is a win; say which and what it does to the
  mystery-5 board.
- (D3) GE-WEAK FIRST POSITIVE (only if FLOOR-GE survives): the
  obligation of record is kernel ternary/short-support emptiness at
  the prize rows. Connect it END-TO-END at toy scale: build the
  explicit ell-condition system (integer_code_distance_cert's form)
  at small 2-power N' with p = 1 mod N'; certify kernel emptiness
  per toy row (exhaustive or lattice-based); price the certification
  as a function of (N', p, ell') and extrapolate honestly to the
  prize rows. What is the smallest new THEOREM (not computation)
  that would make per-row certification unnecessary?
- (D4) THE CONE GEOMETRY: is there a lattice-cone formulation of
  the toy certification (D3) that a standard tool (LLL / Fincke-
  Pohst at toy scale, stdlib-implementable) decides? If yes, run it
  at N' = 8, 16 and compare cost against brute force. No external
  libraries — stdlib only; if a real lattice tool is needed, spec
  it, do not install it.

## 2. Falsifiers / honesty
- A successful (D1) witness KILLS FLOOR-GE and re-opens the
  construction route — report with a reproduction script and stop
  the (D3)/(D4) line; the coordinator re-poses.
- Distinguish PROVED (exhaustive at a cell) / SEARCHED (structured,
  incomplete) / SAMPLED at every claim. The round-21 pilot's
  epistemic ladder is the template.

## 3. Rules
- DRAFT ONLY in notes/pilots_20260807/ge_floor_falsifier/. Never
  edit dag.json/nodes/tools; no git; no Modal. COMPUTE LAW: every
  python3 invocation via tools/ramguard tiny|local -- python3 ...
  (literal --), from repo root, INCLUDING file patching and JSON
  peeking. 2-power toy grids (CATCH-Z6). Name every measured
  functional (CATCH-19C). Verbatim quotes with file:line. No
  REPORT.md — your final message IS the report. QUARANTINE: do not
  read notes/pilots_20260802/CAMPAIGN_LEDGER.md at or past line
  2487 (the "ROUND 22 LAUNCHED" marker); do not read the other
  round-22 pilot dirs (l1_ell_sweep, bb_nu_transport,
  f2_rlocality); PASS THIS QUARANTINE CLAUSE VERBATIM to any
  subagent you dispatch.
