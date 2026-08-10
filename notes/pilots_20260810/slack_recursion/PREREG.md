# PREREG — slack_recursion (round 29)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

THE SUPPLY SIDE'S LAST NUMBER. Round 28's maxscan_algorithm decided
the delta=1 flank branch (COLLAPSE at four scales) and named the
route to the remaining one: the MAXIMAL-SLACK curve (arbitrary
received words — the round-27 sampled values 67 > 46 at n=16,
GROWING over two scales while delta=1 died) is undecided, and "the
parity theorem may apply recursively (E on one parity class is
itself an e2 one level down), which is the only visible route to
n=128" — and to the maximal-slack object. YOUR JOB: close the
supply side entirely. Read first:
notes/pilots_20260810/maxscan_algorithm/{REPORT.md, FABLE_AUDIT.md,
scratch/ms_exact.py, scratch/ms_strat.py, MODAL_REQUEST.md};
notes/pilots_20260809/nonpoly_flank_census/{REPORT.md} (the
maximal-slack sampled measurements and their word classes); the
round-28 addenda on
critical/nodes/rate_half_band_crossing_location/statement.md.

## Deliverables

**D1 — THE RECURSION, FORMALIZED.** The round-28 note is one line;
make it a theorem or kill it: does the parity factorization apply
to E restricted to one parity class (i.e., is the restricted E an
e2-type functional one level down, enabling the s <= n/4 stratum
ceiling to iterate)? Register the exact statement and the expected
reduction factor BEFORE proving. If it lands: the n=128 antipodal
scan prices at what? (Register the price.)

**D2 — MAXIMAL SLACK, EXACT AT n=32.** The round-27 measurement
was 120 sampled locator words at n=16 (67 two-field). Design the
exact computation of the ARBITRARY-WORD maximum at n=32 — the
object is max over ALL received-word classes (every delta stratum,
not just delta=1) of the agreement->=a count. Routes: (a) the
delta-stratified union (the window-shift reduction makes each
delta stratum a shifted-window problem — the round-27 proved
reduction; sum/max over delta with the round-28 machinery per
stratum); (b) direct subspace-closure (ssparse-style F_LMAX
generalization — check its cost at n=32); (c) the recursion from
D1 if it lands. Register prices; run the best; two fields; exact.

**D3 — THE SUPPLY VERDICT.** With delta=1 decided and D2 measured:
state the complete supply-side picture — the arbitrary-word max at
n = 8/16/32 (exact), its trend vs the 4.83-bit razor need, and
whether ANY supply-side mechanism remains that could matter at
razor scale. If D2's number still grows: that is a real finding —
characterize the maximizer class (which delta, which structure)
and what it would need to reach the razor need. If it collapses
like delta=1: the supply side of the band question is CLOSED as
evidence, and say so with the margin.

**D4 — THE MINT PACKAGE (if budget remains).** The parity theorem
+ the STRAT_1 closed form + (if D1 lands) the recursion, drafted
as a self-contained mint note (statement, proof, verification
harness pointers) for the coordinator's mint queue.

## Escape tests (before the main work)

- Replay ms_exact.py at n=8,16 (SCRATCH COPY; coordinator got
  IDENTICAL at 8/16/32/64) — your machinery must match before
  extending it.
- Reproduce the round-27 maximal-slack sampled values (67 at n=16,
  two fields) from the banked nonpoly machinery (SCRATCH COPY).

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or below line 4474; do not read the other round-29 pilot dirs
  (collinearity_object, list_profile_bound, k_extremal). Pass this
  clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root —
  including file patching and JSON peeking. RAMGUARD_TIMEOUT
  documented per use.
- BANKED SCRIPTS FROM SCRATCH COPIES ONLY.
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no
  bulk loads; checkpoint everything; background batches with
  results files for >10-min runs. Beat walls BY DESIGN, never by
  relaxation.
- DRAFT-ONLY: writes only in notes/pilots_20260810/slack_recursion/;
  no dag/nodes/tools writes; no git; no Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing;
  misses first. Name every measured functional (CATCH-19C).
  Two-field confirmation for structural claims. Own-repo grep
  before claiming anything is missing (CATCH-24A).
- Your final message IS the report. End with a compliance
  paragraph.

## Pilot registrations (appended by the pilot before any computation)
