# PRE-REGISTRATION — THE DIM-64 LATTICE CERTIFICATION RUN (round 23)

Round 23, 2026-08-07. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: mystery 5's first
executable positive step. Round 22 proved the per-row GE-WEAK
certificate at N' = 128 is a dimension-64, radius-16 lattice
enumeration (~2^27.4 nodes LLL-only, ~2^10-2^17 with better
reduction). EXECUTE IT: certify kernel ternary emptiness at real
pinned rows, with checkpointing across the compute walls.

## 0. Sources (quote verbatim first; REUSE the round-22 machinery —
it is coordinator-replayed)
- notes/pilots_20260807/ge_floor_falsifier/{gelib.py, d4_cone.py,
  d4_price.py, REPORT.md} — the exact-rational LLL + Fincke-Pohst
  implementation, validated at h = 4, 8 against exhaustive brute
  force in BOTH directions.
- critical/nodes/lattice_cone_certificate/statement.md round-22
  addendum — the pricing of record + the production spec.
- critical/nodes/integer_code_distance_cert/statement.md — the
  system of record (K_p, ternary, support <= 2l', the antipodal
  cyclotomic relations) + "no hidden finite registry" (the
  universality residue — you are NOT closing it; you are
  certifying pinned rows).
- THE ROW LIST: derive from the frozen prize spec + the deployed
  row registry which primes p = 1 mod 128 the campaign actually
  needs certified (the official/deployed rows the generator_economy
  and kernel-lattice consumers quantify over — quote the spec rows
  with file:line; if the spec pins few rows, certify all of them;
  if it pins a family, certify the named representatives and say
  exactly what remains).

## 1. Deliverables
- (D1) THE ROW LIST with provenance (file:line per row).
- (D2) VALIDATION FIRST: re-certify the round-22 boundary cells
  (h = 8: p = 463249 must yield its 2 witnesses with Norm = p;
  p = 463457 must certify EMPTY; the C-4 anchor cells) — your
  pipeline must reproduce all of them EXACTLY before any dim-64
  run is trusted.
- (D3) THE RUN: for each row, exact integer LLL (deep insertions /
  iterated reduction as needed — stdlib only) then a COMPLETE
  Fincke-Pohst enumeration of {w != 0 : ||w||_inf <= 2} in the
  folded kernel lattice Lambda_p (dim 64, det p), with
  per-coordinate box pruning. CHECKPOINTING IS MANDATORY: the
  ramguard local wall is 5 minutes — design the enumerator to
  serialize its DFS state to YOUR OWN dir and resume across
  invocations; never run bare python3 to dodge the wall. Each
  certificate = the reduced basis + the node count + the empty (or
  witness) result + a fail-closed mutation control (a deliberately
  planted vector must be FOUND by the same code path).
- (D4) THE HONEST LEDGER: rows certified / rows attempted-not-
  finished (with exact node counts + projected cost) / rows out of
  reach. Plus the universality statement of what per-row
  certificates do NOT close (quote integer_code_distance_cert).

## 2. Falsifiers / honesty
- If a prize-row enumeration finds a WITNESS (nonzero ternary
  kernel vector in the box): that is a MAJOR event — GE-WEAK's
  emptiness expectation fails at that row. Verify the witness
  exactly (Norm divisibility, unfolded support), report with a
  standalone reproduction script, and STOP the campaign line for
  the coordinator to re-pose. Register this response in advance.
- A run that cannot finish is reported with its exact state, not
  extrapolated to a verdict.

## 3. Rules
- DRAFT ONLY in notes/pilots_20260807/ge_lattice_cert/. Never edit
  dag.json/nodes/tools; no git; no Modal; no package installs
  (stdlib only — fplll is NOT available; the round-22 exact
  implementation is your base). COMPUTE LAW: every python3
  invocation via tools/ramguard tiny|local -- python3 ... (literal
  --), from repo root, INCLUDING file patching and JSON peeking;
  checkpoint files live in your own dir. Name every measured
  functional (CATCH-19C). Verbatim quotes with file:line. No
  REPORT.md — your final message IS the report. QUARANTINE: do not
  read notes/pilots_20260802/CAMPAIGN_LEDGER.md at or past line
  2786 (the "ROUND 23 LAUNCHED" marker); do not read the other
  round-23 pilot dirs (cw_shared_target, fpc5_diag, c2pp_diag);
  PASS THIS QUARANTINE CLAUSE VERBATIM to any subagent you
  dispatch.
