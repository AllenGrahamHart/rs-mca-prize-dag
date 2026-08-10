# PREREG — rh_overlap_cap (round 31)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation beyond the two
named anchors. AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260810/list_profile_bound/REPORT.md` (round 29)
2. `notes/pilots_20260810/collinearity_object/REPORT.md` (round 29)

## Mandate

THE SAFE HALF OF RH-AC IS ONE INEQUALITY (round-29 T5): if the
pairwise-overlap cap stays strictly below a^2/n = 2^39 + 2^34 + 2^27
at sigma = 2^34 (a = k + 2^34, n = 2^41, k = 2^40), then T3 closes
the safe half of the crossing with 89 bits of margin; the open
bracket is exactly the MDS-vs-Fisher overlap gap, ratio 0.999748.
Separately, round-29 T4 proved sporadic collinearities of the
locator set {P_S} DO NOT EXIST for RIG = a-1-2s >= 0 — all
collinearity families are pencils, M <= m+1, T <= rho+1 — and U1
proved the two round-28 point sets are one set up to a fixed
collineation. NOBODY has yet attacked the overlap-cap inequality
WITH the pencils-only structure in hand. YOUR JOB: that attack.

## Deliverables

**D1 — THE EXTREMAL STRUCTURE.** What does a pairwise-overlap
configuration at the cap look like? Use the T4 census (pencils only,
the d_x law, families capped at m+1) to characterize the maximal
overlap achievable by pencil families, exactly. If pencil structure
forces overlap <= a^2/n - delta for an explicit delta > 0, that is
the round: derive delta and check it against the 0.999748 ratio.

**D2 — SUBCLASS PROOFS.** Prove the inequality on the largest
structured subclasses you can reach (single-pencil, bounded-m,
minimum-weight strata), each stated with exact scope and a
falsifier. POSE what remains as named residuals.

**D3 — THE SCALED SEARCH.** At small admissible scales (the same
scale ladder the round-29 pilots used), measure the true max
pairwise overlap vs the a^2/n cap and vs the Fisher bound. Is the
0.999748 gap real headroom or an artifact of the bound pair? Exact
integers; scaling trend across >= 3 scales; pre-register the
extrapolation BEFORE running.

**D4 — CONSUMER CHECK (CATCH-24C).** Quote, file:line, exactly what
T3/T5 consume from the cap (which overlap notion, pairwise over
WHICH set, at which sigma) and confirm D1-D3 attack THAT object —
the round-28/29 corrections show near-miss objects are the campaign
hazard. Misses first.

## Constraints (binding)

- COMPUTE LAW: never bare python3. `tools/ramguard tiny -- python3 ...`
  (256M/60s) for peeks, `tools/ramguard local -- python3 ...` (1G/5min)
  for real runs, from the repo root, literal `--`. This includes JSON
  peeks and file patching. Stdlib only. No Modal, no network, no git.
- RAM DISCIPLINE: file-at-a-time reads; NEVER open dag.json (node.json
  shards + grep); stream-parse large files; checkpointed batches with
  results files for anything long.
- WRITE SCOPE: ONLY inside notes/pilots_20260810/rh_overlap_cap/.
  No dag/, nodes/, tools/ edits. No git. Never touch any path
  containing prize-codex-.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md.
  Never read the sibling round-31 dirs (rh_type2_stratum,
  rh_transport_dictionary, rh_e_axis_audit). Round-30 and earlier
  pilot dirs are readable.
- BLIND PRIORS: after reading ONLY the two anchors, append "## Pilot
  registrations" (P(inequality provable this round), expected
  extremal shape, expected scaled-gap trend) BEFORE any further read.
- REPORT: REPORT.md in your dir; MISSES-FIRST; every quantifier
  claim quoted file:line (CATCH-24C); own-repo greps before novelty
  claims (CATCH-24A); zero-power declarations on max-quantified
  claims; banked scripts from scratch copies only.
