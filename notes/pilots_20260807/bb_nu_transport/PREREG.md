# PRE-REGISTRATION — MYSTERY 4 (crossing): BB's method shape -> the accident UPPER bound / nu(A) (round 22)

Round 22, 2026-08-07. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: the named crux of the
crossing mystery is an UPPER bound on accidents in the break region.
THEOREM BB's proof concentrates accidents into 256 shells — a LOWER-
bound construction. The question: does BB's METHOD (shell
concentration) transport to an upper bound — either on accidents
directly or on the M-route's nu(A)? This is a method transport, NOT
an inequality transfer.

## 0. Sources (quote verbatim first)
- notes/pilots_20260806/gamma_shell/ — THEOREM BB (the 72.065-bit
  proved budget-break), LEMMA SL / THEOREM SM / THEOREM AC, the
  shell structure (256 shells), the break-region row description
  (a_L >= k+2^34+1; safe side w=2^35).
- notes/pilots_20260806/crossing_gap/ — the gap analysis banked in
  round 20.
- critical/nodes/rate_half_list_adjacent_crossing/statement.md —
  the THEOREM BB addendum (threshold relocation, consumers are
  existence/determination-shaped; the crux stated).
- notes/pilots_20260807/red_closability_probes/REPORT.md — PROBE
  2's countermodel (L_1 = 6 > B* = 5 >= B_C = 5 at RS[F_5,|D|=4,
  k=2]): the WARNING of record. L_1 -> B_C is NOT a transfer. Any
  transported bound must name its functional and prove its own
  inequality; quoting BB's inequality for a different functional is
  the exact mistake the countermodel kills.
- The M-route and nu(A): locate the definition in the crossing
  lane's nodes/notes (grep for nu(A) / M-route in critical/nodes
  and notes/pilots_20260806/); quote it with file:line before
  using it.

## 1. Deliverables
- (D1) THE METHOD ANATOMY: decompose BB's proof into its named
  steps (shell decomposition, concentration, counting). For each
  step, state what it PROVES (direction, functional, row region)
  — a table, applies/fails-because per step, against the upper-
  bound target. The round-19 discipline: exact hypothesis matching,
  no vibes.
- (D2) THE TRANSPORT ATTEMPT: if some steps survive (D1), derive
  the candidate upper bound at toy rows (2-power grids; small
  tower rows e >= 3 with delta_a = 1 to match BB's region) and
  VERIFY numerically: compute true accident counts exhaustively at
  toy scale and compare against the candidate bound. A bound that
  fails at a toy row is dead — report the cell.
- (D3) THE nu(A) VARIANT: same exercise for the M-route's nu(A) —
  does shell concentration bound nu(A) above? If nu(A)'s definition
  makes the transport type-mismatch (like L_1 vs B_C), say so
  immediately and name what WOULD bound it.
- (D4) THE HONEST REMAINDER: whichever way (D2)/(D3) land, state
  exactly what the crossing mystery still needs: the crux
  restated with whatever was gained, and the next decisive test.

## 2. Falsifiers / honesty
- Pre-register (before computing) the toy-row test cells and the
  acceptance rule for a candidate bound.
- If the method does not transport, a clean NO with the exact
  step-level gap is the deliverable — do not manufacture a
  conditional bound from unverified steps.

## 3. Rules
- DRAFT ONLY in notes/pilots_20260807/bb_nu_transport/. Never edit
  dag.json/nodes/tools; no git; no Modal. COMPUTE LAW: every
  python3 invocation via tools/ramguard tiny|local -- python3 ...
  (literal --), from repo root, INCLUDING file patching and JSON
  peeking. 2-power toy grids (CATCH-Z6); no shift-0 cells where
  shifts exist (CATCH-19B). Name every measured functional
  (CATCH-19C). Verbatim quotes with file:line. No REPORT.md — your
  final message IS the report. QUARANTINE: do not read
  notes/pilots_20260802/CAMPAIGN_LEDGER.md at or past line 2487
  (the "ROUND 22 LAUNCHED" marker); do not read the other round-22
  pilot dirs (l1_ell_sweep, ge_floor_falsifier, f2_rlocality);
  PASS THIS QUARANTINE CLAUSE VERBATIM to any subagent you
  dispatch.
