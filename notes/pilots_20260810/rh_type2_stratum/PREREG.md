# PREREG — rh_type2_stratum (round 31)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation beyond the two
named anchors. AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260810/collinearity_object/REPORT.md` (round 29)
2. `notes/pilots_20260810/apolar_origin/REPORT.md` (round 28)

## Mandate

The residual budgets {2^39, 2^39+1} of RH-AC fail to close for
EXACTLY THREE named reasons (round 29): (i) the 1-or-3-integer w*
tiling gap per m; (ii) THE NON-MINIMUM-WEIGHT TYPE-2 STRATUM, where
the banked cap is 5.04e22 against a budget of 2^39 — a ~39-order
gap and THE BIG ONE; (iii) m = 1. YOUR JOB: residual (ii). Determine
whether the 5.04e22 is crude counting or a real wall: the cap came
from a coarse stratum count; the apolar (AO1) and collinearity (T4)
structure theorems were NOT applied to the non-minimum-weight
stratum. Close it, shrink it, or prove it is the honest frontier.

## Deliverables

**D1 — THE CAP'S ANATOMY.** Reconstruct, file:line, exactly how the
5.04e22 was derived (which count, which stratum definition, which
inequalities). Name every place slack was given away.

**D2 — STRUCTURE TRANSPORT.** Which of the banked structure theorems
(AO1's O=0/m>=2 apolarity route; T4's pencils-only census; U1's
identification; the d_x law) apply to non-minimum-weight type-2
configurations, and with what modifications? Derive the sharpened
cap where they apply; POSE the obstruction where they do not.

**D3 — THE SCALED CENSUS.** At small admissible scales, enumerate
the non-minimum-weight type-2 stratum EXACTLY (the round-29 pilots'
census machinery is banked and readable — copy scripts into your
dir). Measure: actual stratum size vs the 5.04e22-style bound's
small-scale analogue. If the bound is loose by orders of magnitude
at small scales, quantify the looseness trend across >= 3 scales;
pre-register the extrapolation BEFORE running.

**D4 — VERDICT + RESIDUALS.** Either a sharpened cap (exact, with
proof sketch and falsifier), or the honest statement of the wall
with the exact missing ingredient named. Misses first; zero-power
declarations where searches had no power.

## Constraints (binding)

- COMPUTE LAW: never bare python3. `tools/ramguard tiny -- python3 ...`
  (256M/60s) for peeks, `tools/ramguard local -- python3 ...` (1G/5min)
  for real runs, from the repo root, literal `--`. This includes JSON
  peeks and file patching. Stdlib only. No Modal, no network, no git.
- RAM DISCIPLINE: file-at-a-time reads; NEVER open dag.json (node.json
  shards + grep); checkpointed batches with results files for
  anything long.
- WRITE SCOPE: ONLY inside notes/pilots_20260810/rh_type2_stratum/.
  No dag/, nodes/, tools/ edits. No git. Never touch any path
  containing prize-codex-.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md.
  Never read the sibling round-31 dirs (rh_overlap_cap,
  rh_transport_dictionary, rh_e_axis_audit). Round-30 and earlier
  pilot dirs are readable.
- BLIND PRIORS: after reading ONLY the two anchors, append "## Pilot
  registrations" (P(cap crude by >= 10 orders), P(stratum closes
  under 2^39 this round), expected binding obstruction) BEFORE any
  further read.
- REPORT: REPORT.md in your dir; MISSES-FIRST; every quantifier
  claim quoted file:line (CATCH-24C); own-repo greps before novelty
  claims (CATCH-24A); zero-power declarations on max-quantified
  claims; banked scripts from scratch copies only.
