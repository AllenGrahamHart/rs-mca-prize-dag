# PRE-REGISTRATION — THE GAMMA-SHELL QUESTION: refutation or re-pose (round 20, THE PRIORITY)

Round 20, 2026-08-06. Coordinator-authored brief; the pilot appends
its own registrations BEFORE any computation. THE BOARD'S SHARPEST
QUESTION: THEOREM DSA proved accidents exist at admissible tower
rows; whether that breaks the PRIZE-LEVEL statement or merely our
intermediate runs through the gamma-shell/budget analysis left open
at the DSA bank. Two live outcomes, both wins: WITHIN-BUDGET (our
intermediate was lossy — deliverable = the re-pose guidance) or
BUDGET-BREAK (a refutation path for the grand challenge itself — a
resolution). EXTREME honesty discipline required: a budget-break
claim would be the campaign's biggest single result and gets the
strongest possible falsifier treatment.

## 0. The state (quote verbatim before working)

- background/nodes/crossing_dsa_refutation (+ its 2026-08-06
  addendum: the scope condition is SATISFIED — tower rows are
  in-family; the refutation of OUR intermediate stands
  unconditionally; THIS pilot owns the prize-level consequence).
- The object of record: the crossing count is per-gamma-shell —
  X_w(gamma) = #{S in W_w : prod T(S) = gamma} (round-15 mun
  REPORT'S row map; the DSA witness has sig(S) = 1941325217792
  computed but its SHELL POPULATION undetermined).
- The consumer chain: critical/nodes/rate_half_list_adjacent_crossing
  (its statement + its budget B* = floor(q/2^128); at the witness
  row log2 B* = 127.510) and UPWARD — trace exactly which
  prize-level statement consumes the crossing node's bound, so any
  budget-break claim names the exact statement that breaks. Do not
  stop at our node.
- The accident family: DSA gives >= C(108,53) = 2^103.6 accidents
  at the witness row (one epsilon's fibre); the FULL family is
  larger (all epsilon in the pigeonhole class; LEMMA ROT orbits).

## 1. Pre-registered deliverables

- **(G1) THE SHELL MAP OF THE ACCIDENT FAMILY.** For the DSA
  accidents at the witness row: how do their sigs/gammas distribute
  over shells? Structure available: the accidents are lifts of
  reduced solutions (LEMMA DS bijection); sig behaves how under the
  2^33-periodic lift and the ROT orbit action? Derive the exact
  sig-arithmetic of the lift (a lifted S' has sig = f(sig'(S'),
  structure) — work it out), then the shell distribution law.
  Toy-verify the sig-arithmetic exhaustively at the three DSA gate
  shapes before any prize-row claim.
- **(G2) THE BUDGET COMPARISON.** Per-shell: structural population
  ~ 2^117.15 per sig class (round-15 [B3]) vs B* = 2^127.51 at the
  witness row — the structural margin is ~ 2^10.4. The accidents
  add HOW MUCH to the MAXIMAL shell? Three regimes to decide:
  (i) accidents spread ~uniformly over 2^41 shells (adds ~2^62.6
  per shell from the single-epsilon fibre — negligible vs 2^117);
  (ii) accidents concentrate on FEW shells (the periodic lift may
  force sig into a small coset! — check this FIRST, it is the
  danger case); (iii) intermediate. The full-family count (all
  epsilons, orbit-corrected per LEMMA ROT + the ssl CATCH-19A
  scope note: the crossing instance IS all-odd so the 2N constant
  applies) must be estimated with stated error bars, worst case
  first.
- **(G3) THE VERDICT, with the refutation protocol.** If the
  maximal-shell total exceeds B* at ANY admissible row: STOP,
  pre-registered-falsifier-check everything, produce a
  self-contained reproduction script computing the exact per-shell
  count and the exact budget at that row, trace the consumer chain
  to the prize-level statement, and report which statement breaks
  — clearly labelled as a CANDIDATE refutation for coordinator
  replay, NOT a claimed resolution. If within budget at all
  admissible rows: state the margin law and the RE-POSE guidance
  (what the crossing intermediate should claim instead — e.g. a
  per-shell bound with the accident term priced in).
- **(G4) THE PT-2 INTERACTION.** The bracket endpoint clears the
  ternary threshold by 0.336 bits (tern_master_threshold watch
  line). Does the shell analysis change at w just above 2^34 vs at
  the endpoint? State whether the re-pose (if that is the verdict)
  is stable across the bracket.

## 2. Pre-registered falsifiers / honesty clauses

- The sig-arithmetic toy gate is MANDATORY before prize claims.
- A budget-break claim requires: exact arithmetic (no floats at the
  comparison), BOTH the count lower bound and the budget upper
  bound derived with citations, the consumer chain traced to the
  prize statement, and the CANDIDATE label. Overclaim on this
  question is the worst failure mode available to this campaign.
- A within-budget verdict must state the margin at the WORST
  admissible row, not a favourable one.
- Concentration (regime ii) must be decided by proof or exhaustive
  toy census, never assumed away.

## 3. Rules of engagement

- DRAFT ONLY: write only inside notes/pilots_20260806/gamma_shell/.
  Never edit dag.json, node shards, tools/, or push. Do NOT read
  notes/pilots_20260806/crossing_gap/ (sibling this round). Do NOT
  read CAMPAIGN_LEDGER entries appended after the "ROUND 20
  LAUNCHED" marker (the round-19 quarantine rule).
- COMPUTE LAW: never bare python3, INCLUDING file patching and JSON
  peeking — tools/ramguard tiny|local -- python3 ..., literal --,
  from repo root /home/u2470931/smooth-read-solomin/prize.
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report; the
  coordinator persists it verbatim.
