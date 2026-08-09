# PREREG — pincer_formalization (round 27)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

The band-closure analytic half (rate_half_band_closure, critical
TARGET; the anti-concentration direction of the FLOOR v2) cannot
currently be STATED sharply at the razor rows: the WP5 verdict
(critical/nodes/rate_half_band_closure/notes/WP5_RATEHALF_VERDICT.md)
pinned that the row-local random-word first-moment crossing sits
BELOW the proved unsafe reach near the cap, so the floor's intended
model must be the WORST-WORD/PINCER object — "whose per-row crossing
is NOT yet formalized: an open item OF THE FLOOR." Your job: close
that formalization gap. This campaign has felled three
"missing-theorem" claims that were bookkeeping (rounds 24, 25, 26) —
check whether this is the fourth BEFORE building anything new
(CATCH-24A: own-repo grep for the pincer crossing under all its
names).

## Deliverables (ORDER IS BINDING)

**D0 — THE FOUNDATION AUDIT (first, before any formalization).** The
WP5 flag of record: "the safe-side-above-sigma* pincer machinery was
consumed from banked docs, not re-audited." Audit it now: read the
pincer/balance safe-side proof (P6_RATEHALF_SIBLING.md, the
pro_brief_razor.md sigma* provenance — sigma* = 8,592,912,738 =
t*-1, generic pincer; and whatever banked docs they cite), replay
its arithmetic exactly (the WP5 machine checks are your calibration:
sigma* replay, cap reach 2^33, band width 2,978,146, razor threshold
255.899990), and issue a verdict: SOUND / REPAIRABLE / BROKEN, with
the exact load-bearing steps listed. If BROKEN, stop and report —
everything downstream changes.

**D1 — THE FORMALIZATION.** Define the worst-word/pincer per-row
first-moment crossing as an exact object: for an admissible razor
row (q, k, n = 2^41-shape), a computable function sigma_FM(row) with
a stated domain, such that (i) it specializes to the machinery that
proved the safe side above sigma*, (ii) it does NOT reduce to the
random-word crossing (which is refuted near the cap — that
refutation is your negative control), and (iii) it is computable
exactly at scaled band-analogue rows (q <= ~2^40, the window-law
campaign's regime). Register the candidate definition BEFORE
computing with it.

**D2 — THE VERIFICATION AGAINST BANKED EVIDENCE.** Compute
sigma_FM at the banked crossing-fidelity cells (the 18/18 family,
notes: f6a2_results.json; the ~200-prime window-law grid cited in
the witness-hunt recon) and at the four upstream deployed pairs
(the regime-map replay — KB MCA/list 1116047/1116046, M31
1116023/1116022 at n = 2^21). The formalized object must reproduce
what the random-word model already got right AND fix what it got
wrong (the near-cap ordering vs the proved unsafe reach). Register
expected outcomes per cell family first.

**D3 — BAND-AC, THE CONJECTURE OF RECORD (draft).** State the
analytic half as ONE sharp conjecture: at every admissible razor
row, the band determination equals the sigma_FM prediction —
deficit below, safe above, no anti-concentration failure. Name the
quantifiers (which rows, which sigma range, what "equals" means —
exact count vs Poisson tolerance), the consumer bar per consumer
(adjacency_closing, list_adjacency_closing, mca_safe need the
LOCATED determination — read their statements and name each bar,
CATCH-24C), and pre-register at least two falsifiers with power
controls. If D1's object makes the old FLOOR v2 statement wrong in
any particular, say exactly where.

## Escape tests (before the main work)

- Replay the WP5 machine checks (sigma*, cap reach, band width,
  razor threshold, the four-pair margins to 4 decimals).
- Reproduce two f6a2 crossing cells from the banked script (SCRATCH
  COPY — see rules).

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or below line 4062; do not read the other round-27 pilot dirs
  (nonpoly_flank_census, staircase_extension, cancellation_recon).
  Pass this clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from
  /home/u2470931/smooth-read-solomin/prize — including file patching
  and JSON peeking. RAMGUARD_TIMEOUT documented per use.
- BANKED SCRIPTS RUN FROM SCRATCH COPIES ONLY (copy into your dir or
  the session scratchpad first) — a banked script may write into its
  own banked dir (the round-26 lesson).
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no bulk
  loads; checkpoint long runs; background batches with results files
  for >10-min runs.
- DRAFT-ONLY: writes only in notes/pilots_20260809/pincer_formalization/;
  no dag/nodes/tools writes; no git; no Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing; misses
  first. Name every measured functional (CATCH-19C). Own-repo grep
  gates every "this object does not exist" claim (CATCH-24A).
- Your final message IS the report. End with a compliance paragraph.

## Pilot registrations (appended by the pilot before any computation)
