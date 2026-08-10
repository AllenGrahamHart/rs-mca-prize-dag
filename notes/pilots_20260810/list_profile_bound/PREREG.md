# PREREG — list_profile_bound (round 29)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

THE THEOREM TARGET under the new working hypothesis. Round 28's P0
correction established: RH-AC's open content is the FAR-CA crossing
on [k+2^34, 3n/4) — the Hankel layer applies only above 3n/4, and
the PROVED simple-pole floor puts B_ca^far(k+2^34-1) >= 2^216
against B* = 2^128 (88 bits unsafe at the bracket bottom). The
working hypothesis of record is a_RH = k + 2^34 + O(1). What is
MISSING is the safe half just above: an UPPER bound on the max list
profile (equivalently B_ca^far, equivalently F_LMAX at razor
parameters) at agreements sigma = 2^34 + c that crosses below
B* = 2^128 for explicit small c. The round-28 measured decay of the
exact max profile is 2.8074 bits per unit of a at the one exactly
computed scaled cell (0.6865 * log2 q) — at that rate the 88 unsafe
bits clear in ~32 units; the certified worst-case lower bound on the
decay ratio (0.1451) clears them in ~217 units. Either would pin
a_RH = k + 2^34 + O(100) — the question is what is PROVABLE. Read
first: notes/pilots_20260810/ssparse_endpoints/{REPORT.md,
FABLE_AUDIT.md} (the P0 chain, the decay ladder, the named
downward bias); the round-28 addenda on
critical/nodes/rate_half_band_crossing_location/statement.md; the
far-CA machinery above 3n/4 (rate_half_ca_hankel_fullrank_branch,
split_pencil_equivalence, far_ca_rider_reduction — their proofs
state their own domains); apolar_origin's mechanism C (min-weight
coset uniqueness, the type-1/type-2 dichotomy — proved legal on
both official profiles; a candidate instrument BELOW 3n/4).

## Deliverables

**D1 — THE POSE.** State the target theorem precisely: for
admissible razor rows, an explicit function UB(sigma) with
B_ca^far(k + sigma) <= UB(sigma) and UB(2^34 + c) < 2^128 for an
explicit c. Name what each candidate consumer needs (CATCH-24C):
adjacency_closing needs the pair (the PROVED floor at k+2^34-1
already supplies the unsafe half IF the crossing lands at k+2^34+c
with the safe half at that exact index). Register at least one
falsifier with power (what measured object would show NO such UB
exists at small c — i.e. the profile is FLAT above 2^34; note this
is exactly what (RH-AC-hi) would need, already facing the 2^40
flatness demand — quantify the link).

**D2 — THE INSTRUMENT SURVEY (own-repo first, CATCH-24A hard).**
What in-repo machinery gives max-list-profile UPPER bounds at
agreements just above k + 2^34? Candidates to check: (a) apolar's
mechanism C ported below 3n/4 (its legality margins were computed
at the official profiles — do they hold at sigma = 2^34?); (b) the
QMU/QMP minimal-support species; (c) Johnson-type bounds at these
radii (the banked Johnson machinery is elsewhere in the lane — its
domain?); (d) the far-CA rider reduction pushed below its stated
domain (it needs L_2(2tau) at 2tau = 2^35 << k — the round-28
report says hopeless; verify or refute that pricing); (e) anything
the greps surface. For each: domain, what it yields at
sigma = 2^34 + c, and the gap to 2^128.

**D3 — THE ATTACK.** Prove what is provable. If a full UB theorem
is out of reach, the bankable partials: (i) UB on a sub-stratum
(e.g. the tangent-free or pole-restricted part); (ii) a
conditional UB (on a named standard hypothesis); (iii) the exact
scaled-cell program — extend the round-28 measured-decay cell to a
LADDER (register the cells; the named downward bias must be
quantified per cell, not waved at) giving the decay law with error
bars, as the evidence base for the pose. The zero-power
declaration binds: no mean-model quantity enters any verdict.

**D4 — THE CONSTANT.** Under whatever lands, pin the working
hypothesis's O(1): the explicit c with a_RH <= k + 2^34 + c
(conditional or unconditional), and the margin ladder. If nothing
pins c, state the sharpest honest bracket and what closes it.

## Escape tests (before the main work)

- Replay ssparse's d4_margins.py (SCRATCH COPY; coordinator got
  the ladder reproduced) — your baseline numbers.
- Verify the P0 chain's two scope quotes yourself (the Hankel
  r < R/2 lines) — you build on them.

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or below line 4474; do not read the other round-29 pilot dirs
  (collinearity_object, k_extremal, slack_recursion). Pass this
  clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root —
  including file patching and JSON peeking. RAMGUARD_TIMEOUT
  documented per use.
- BANKED SCRIPTS FROM SCRATCH COPIES ONLY.
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no
  bulk loads; checkpoint long runs; background batches with
  results files for >10-min runs.
- DRAFT-ONLY: writes only in
  notes/pilots_20260810/list_profile_bound/; no dag/nodes/tools
  writes; no git; no Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing;
  misses first. Name every measured functional (CATCH-19C). The F3
  zero-power declaration binds. Own-repo grep before claiming
  anything is missing (CATCH-24A — five firings and counting).
- Your final message IS the report. End with a compliance
  paragraph.

## Pilot registrations (appended by the pilot before any computation)
