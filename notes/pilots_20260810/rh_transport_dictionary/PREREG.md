# PREREG — rh_transport_dictionary (round 31)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation beyond the two
named anchors. AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260810/slack_recursion/REPORT.md` (round 29)
2. `notes/pilots_20260810/slack_recursion/MINT_PACKAGE.md`

## Mandate

Round 29 resolved the supply side of RH-AC into a MODEL CRITIQUE
gated on one named object: THE (t,M) TRANSPORT DICTIONARY. The t=1
toy model is provably unfaithful (the razor lives at coset scale
t = 2^34; naive transport over-satisfies by ~115 bits; C(127,64)
matches NEITHER coset formula). Theorems A/B (the product-word
realization of Graham-Sloane and the matching upper bound) are exact
at t=1; NOTHING is known at t > 1. Every supply-side razor claim in
the lane is gated on this dictionary. YOUR JOB: build its first
entries.

## Deliverables

**D1 — THE FAITHFUL MODEL, POSED.** Define exactly what a
(t,M)-faithful supply model must preserve to license transport to
the razor's t = 2^34 coset scale (which quantifiers, which counting
unit, which normalization). Pre-register the definition BEFORE
measuring; state the C(127,64) puzzle as its first test case.

**D2 — SMALL-t EXACT MEASUREMENTS.** At t = 2, 3, 4 (and higher if
cheap) on small admissible scale ladders: measure the exact
arbitrary-word supply maximum in the coset-faithful setting.
Checkpointed batches; exact integers; results files.

**D3 — THE TRANSPORT LAW.** From D2: does the t=1 Theorem A/B pair
generalize (a product-word family per coset, a matching upper
bound)? Derive the candidate (t,M) law, test it against every
measured point, and against C(127,64) — if the puzzle resolves
(the value matches the law under the right reading), say which
reading; if not, the law is wrong and say so.

**D4 — THE RAZOR VERDICT, HONESTLY SCOPED.** What do D1-D3 license
about t = 2^34? State the extrapolation gap exactly; pre-registered
falsifier for the law; zero-power declaration on anything the
small-t window cannot see. Misses first. DO-NOT-INHERIT WARNING:
the round-27/28 banked supply lines contain two corrected errors
(the "same fate likely" line; the ratio transport) — read the
corrections in the crossing_location addenda before quoting
anything.

## Constraints (binding)

- COMPUTE LAW: never bare python3. `tools/ramguard tiny -- python3 ...`
  (256M/60s) for peeks, `tools/ramguard local -- python3 ...` (1G/5min)
  for real runs, from the repo root, literal `--`. RAMGUARD_TIMEOUT
  may extend walls; document each use. Stdlib only. No Modal, no
  network, no git.
- RAM DISCIPLINE: file-at-a-time reads; NEVER open dag.json;
  checkpointed background batches with results files for >10-min
  runs.
- WRITE SCOPE: ONLY inside
  notes/pilots_20260810/rh_transport_dictionary/. No dag/, nodes/,
  tools/ edits. No git. Never touch any path containing
  prize-codex-.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md.
  Never read the sibling round-31 dirs (rh_overlap_cap,
  rh_type2_stratum, rh_e_axis_audit). Round-30 and earlier pilot
  dirs are readable (slack_recursion's scratch/ scripts especially —
  copy before running).
- BLIND PRIORS: after reading ONLY the two anchors, append "## Pilot
  registrations" (expected (t,M) law shape, P(C(127,64) resolves
  under the law), expected surplus trend in t) BEFORE any further
  read.
- REPORT: REPORT.md in your dir; MISSES-FIRST; every quantifier
  claim quoted file:line (CATCH-24C); own-repo greps before novelty
  claims (CATCH-24A); zero-power declarations on max-quantified
  claims.
