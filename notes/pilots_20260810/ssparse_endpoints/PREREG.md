# PREREG — ssparse_endpoints (round 28)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

RH-AC (rate_half_band_crossing_location, the pose of record) names
two candidate endpoints with NO discriminating evidence held:
(RH-AC-lo) a_RH = k + 2^34 (the quotient floor is tight) vs
(RH-AC-hi) a_RH = 3n/4 (the half-distance pincer HD1 is tight). The
open content is min{a : S_sparse(a) <= B*(q)} within the PROVED
bracket. YOUR JOB: produce the first discriminating evidence — by
executing the two registered falsifiers with their power stated, and
by the first-ever scaled measurements of where the S_sparse crossing
actually sits. Read first: the child's statement
(critical/nodes/rate_half_band_crossing_location/statement.md), the
(RH-SPLIT) lossless decomposition
(rate_half_mca_sparse_layer_reduction, PROVED — S_sparse's exact
definition lives there), HD1
(rate_half_half_distance_safe_bracket), and the round-27
cancellation_recon consumer-bar map.

## Deliverables

**D1 — FALSIFIER F1 (fires against -lo, high power).** Push the
quotient-remainder floor's razor reach beyond 2^34 - 1. The
constant moved 2^33 -> 2^34 in one wave (the optimized v5
re-instantiation, c=2^33, d=1); round-27 cancellation_recon proved
the NEXT RUNG of the same family is 11.87 bits short with a tight
normalizer — so a further push needs a NEW mechanism, not the next
rung. Attack surfaces to price and try (register your order): a
non-2-power scale c; a mixed-depth (d >= 2) instantiation evading
the rung quantization; a hybrid of the rotated-prefix and
fixed-tail variants. A push to 2^34 + delta for ANY delta > 0
refutes (RH-AC-lo) and is the single highest-information result
available. An exhausted search with the mechanism space enumerated
is the complementary result: (RH-AC-lo) hardens.

**D2 — FALSIFIER F2 (fires against -lo from the safe side).**
Exhibit one received word y and one razor row with
N(y, k + 2^34; q) > floor(q/2^128). This is an S_sparse evaluation
at a single agreement — the object of
rate_half_sparse_pinning_rigidity's coupled system. Price it
honestly BEFORE attempting (the round-23 lesson: an unreachable
falsifier is not a falsifier); if unreachable at razor parameters,
execute the scaled analogue and state the transport caveat.

**D3 — THE FIRST CROSSING MEASUREMENTS.** At scaled band-analogue
rows where S_sparse is EXACTLY computable (register the scaling map
— the round-27 staircase_extension R2 map is a template: rate-1/2
RS rows N = 2k, D = the order-N subgroup, B = the scaled budget),
measure min{a : S_sparse(a) <= B} directly across a q-ladder and a
scale-ladder. THE QUESTION: does the measured crossing track the
scaled analogue of k + 2^34 (the -lo endpoint), of 3n/4 (the -hi
endpoint), or an intermediate law? Register predictions per
endpoint with numeric windows. Two-power grids; matched controls
(the random-word crossing at the same cells, computed but used ONLY
as the negative control — the F3 zero-power declaration binds: no
random-word quantity may enter the verdict).

**D4 — THE VERDICT.** State plainly which endpoint (if either)
survives, with the margin ladder. If the measurements land strictly
between the endpoints: the intermediate law, fitted and stated as
the new candidate, with the mechanism-change caveat (the round-27
rho extrapolation's caveat pattern).

## Escape tests (before the main work)

- Reproduce the (RH-SPLIT) decomposition at one banked cell (the
  split is PROVED lossless — your S_sparse must reproduce
  B_mca - B_ca^far exactly there).
- Replay the wave-10 a_RH formula at 3 sample q < 2^167 (the
  crossing your scaled measurements must reproduce in the
  determined region — the calibration).

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or below line 4302; do not read the other round-28 pilot dirs
  (apolar_origin, maxscan_algorithm, mca_safe_rewire). Pass this
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
  notes/pilots_20260810/ssparse_endpoints/; no dag/nodes/tools
  writes; no git; no Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing;
  misses first. Name every measured functional (CATCH-19C). The F3
  zero-power declaration binds throughout. Own-repo grep before
  claiming anything is missing (CATCH-24A).
- Your final message IS the report. End with a compliance
  paragraph.

## Pilot registrations (appended by the pilot before any computation)
