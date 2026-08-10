# PREREG — k_extremal (round 29)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation. AUDIT-AND-DRAFT:
any surgery stays coordinator-gated.

## Mandate

THE FLAGGED SEAM from round 28 bank 1 (out-of-mandate flag, now
mandated): rules_freeze/statement.md:9 states the caps as k <= 2^40
(an UPPER bound), and official_row_primes_pinning records ABF26
quantifying "for every choice of F, L, and k" — but no node was
found establishing that k = 2^40 is the extremal rate-1/2 row or
reducing smaller-k rate-1/2 rows to it. The ENTIRE rate-half lane
(the band decomposition, RH-AC, the staircase, the floors, the
brackets) is posed at n = 2^41, k = 2^40. If the grand-challenge
quantifier includes k < 2^40 rate-half rows and nothing reduces
them, the lane has a silent coverage hole of the round-28-tiling
kind. If k = 2^40 is extremal by a provable monotonicity, that
theorem should exist as a node. YOUR JOB: settle which, at audit
grade.

## Deliverables

**D1 — THE QUANTIFIER MAP.** For each consumer that quantifies over
rows (mca_grand, list_grand, mca_safe, mca_unsafe,
adjacency_closing, their row-convention suppliers s0_zero_open /
mixed_radix_frontier / official_row_primes_pinning / rules_freeze):
quote with file:line exactly what k-range its claim covers. Is the
grand-challenge row family "k = 2^40 exactly" (a pinned deployment
parameter), "all k <= 2^40" (a cap over a family), or rate-indexed
(k = n/2 with n ranging)? The upstream agents.md / ABF26 reading
matters — quote it.

**D2 — THE COVERAGE AUDIT.** If the family includes k < 2^40
rate-half rows: what covers them TODAY? Candidates to check
(CATCH-24A greps first): (a) a monotonicity argument (is the
crossing/safety claim at smaller k implied by the k = 2^40 case?
B_C's behavior in k is NOT obviously monotone — check what the
proofs actually use); (b) the clean-rate corridor machinery (do the
R2/corridor nodes cover small-k rate-half rows as
"clean-rate-adjacent"?); (c) the smooth-domain admissibility
conditions (maybe k < 2^40 rows are inadmissible by the domain
conventions — n | q-1 with n = 2k a 2-power still admits many k).
State the verdict: COVERED (by what, exactly) / PINNED (the family
is k = 2^40 only, by which text) / HOLE (with the uncovered set
mapped exactly, the E7 pattern).

**D3 — THE DRAFT.** Per the verdict: if PINNED, the one-paragraph
clarifying note on the row conventions (so the next auditor doesn't
re-run this); if COVERED, the conforming cross-references; if HOLE,
the exact-edit draft of the honest scope flags (the E7 style:
flagged, not silently resolved) + the candidate reduction theorem
posed (k-monotonicity or a per-k family statement), NOT proved —
posed with falsifiers.

**D4 — THE BLAST RADIUS.** If HOLE: which banked results are
k = 2^40-specific vs k-uniform? (The staircase formula, the
brackets, the floors — their proofs' k-dependence, skimmed at
domain level.) A one-page map, not a re-audit.

## Escape tests (before the main work)

- Quote rules_freeze:9 and the ABF26 line verbatim (the two anchors
  the flag was raised on).
- Verify one consumer's row convention resolves as you read it (a
  worked example at a small admissible row).

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or below line 4474; do not read the other round-29 pilot dirs
  (collinearity_object, list_profile_bound, slack_recursion). Pass
  this clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root.
- BANKED SCRIPTS FROM SCRATCH COPIES ONLY.
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no
  bulk loads.
- DRAFT-ONLY: writes only in notes/pilots_20260810/k_extremal/; no
  dag/nodes/tools writes; no git; no Modal; stdlib only.
- Every quantifier claim quoted with file:line (CATCH-24C). Own-repo
  grep gates every "nothing covers it" claim (CATCH-24A). Register
  blind priors BEFORE reading beyond the named anchors; misses
  first. THE ROUND-28 LESSON BINDS: read the consumers' consumers —
  a quantifier freedom claim needs the full chain.
- Your final message IS the report. End with a compliance
  paragraph.

## Pilot registrations (appended by the pilot before any computation)
