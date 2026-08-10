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

### k_extremal blind priors (registered 2026-08-10, after reading ONLY the two named anchors)

Anchors read verbatim before registering (and nothing else):

- `critical/nodes/rules_freeze/statement.md:9` — "the operative prize rules
  are exactly — smooth domain = coset of a power-of-2-order subgroup;
  k <= 2^40; |F| < 2^256; rates EXACT in {1/2, 1/4, 1/8, 1/16} (no dither
  latitude); the m-quantifier per rules_m_reading (family-per-constant-m)."
- `background/nodes/official_row_primes_pinning/proof.md:28-29` — decisive
  fragments "`for every choice of F, L, and k`" and "`k <= 2^40`".

**P1 (family shape), 0.75.** The grand-challenge row family is a CAP OVER A
FAMILY ("all admissible k <= 2^40"), not a pinned deployment parameter.
Both anchors read that way in isolation: `for every choice of ... k` is a
universal, `k <= 2^40` is its admissibility side-condition. 0.15 that some
consumer-side text re-pins it to k = 2^40 exactly; 0.10 rate-indexed/other.

**P2 (the missing theorem), 0.80.** No node states or proves
k-monotonicity for the rate-half lane, and none reduces k < 2^40 rate-half
rows to the k = 2^40 row. I expect the round-28 flag to survive.

**P3 (verdict), split.** HOLE 0.55 / COVERED 0.30 / PINNED 0.15. My COVERED
mass is mostly the "presentational not substantive" branch: the band /
staircase / floor proofs may in fact be k-uniform (k entering only through
the rate and through log-scale band counts), so the hole would be one of
missing statement rather than missing mathematics. I flag in advance that
"the proofs look k-uniform to me" is NOT sufficient for COVERED at audit
grade — COVERED requires a node whose *statement* carries the quantifier.

**P4 (the uncovered set, if HOLE) — a sharp prediction.** Smooth domain
forces |L| = n = 2^t; rate EXACT 1/2 forces k = n/2 = 2^(t-1). So the
rate-half family is not a continuum: it is exactly the 41 rows
k in {2^0, 2^1, ..., 2^40} (per admissible field F with n | |F|-1). I
predict the uncovered set, if any, is "k = 2^j, j < 40" — discrete,
enumerable, and small. If instead I find non-power-of-2 k in the rate-half
family, that is a self-correction I will report.

**P5 (monotonicity direction), 0.65.** If a monotonicity exists, larger k
is the HARDER row (more bands, longer staircase), so k = 2^40 would be
extremal in the right direction and the reduction would be "small k is
easier". But I register the counter-risk explicitly: B_C-type quantities
and any *absolute* constants tuned at 2^40 need not be monotone, and small
k can break asymptotic-regime side conditions (e.g. things requiring
k large enough for a band count / a log factor / an epsilon-vs-1/k
comparison). Small-k rows failing a "k sufficiently large" proviso is my
top candidate failure mode.

**P6 (blast radius shape), 0.60.** I expect literal constants (2^40, 2^41,
41, 40) baked into the staircase/bracket/floor arithmetic rather than
symbolic k, so a k-uniform restatement would be a real re-derivation, not
a rename. Grep for those literals is my first blast-radius probe.

**P7 (round-28 lesson / consumers' consumers), 0.50.** If something rescues
the lane, I predict it sits ONE LEVEL ABOVE the obvious consumers — in a
submission/scope-declaration node (an "exhibit vs family-uniform"
declaration of the kind `official_row_primes_pinning`'s Consequence rule
already demands), not in the band/staircase nodes themselves. I will read
consumers' consumers before claiming freedom either way.

**Pre-registered falsifiers for my own verdict.** I will call COVERED only
if I can quote a node STATEMENT (file:line) whose quantifier ranges over
k < 2^40 rate-half rows. I will call PINNED only if I can quote text
restricting the campaign's obligation to k = 2^40 exactly. Absent both,
HOLE — and a HOLE claim is gated on CATCH-24A own-repo greps over at least
the literal forms: 2^40, 2**40, 2\^40, 1099511627776, "k = 2^40",
"monotone in k", "smaller k", "all k", "any k", "k <= 2^40".

