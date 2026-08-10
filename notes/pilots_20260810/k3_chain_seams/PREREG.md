# PREREG — k3_chain_seams (round 30)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation beyond the two
named anchors. AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `critical/nodes/rate_half_band_structural_surplus/conditional.md`
2. `critical/nodes/rate_half_band_closure/conditional.md`

## Mandate

ADVERSARIAL. The band red was decomposed (2026-08-09) into the K3 arm
(rate_half_band_structural_surplus) and the analytic half
(rate_half_band_crossing_location), and Codex's wave-55 flip made the
K3 arm CONDITIONAL over a four-leaf subtree. This campaign's audit
cadence has caught a quantifier seam within one round of every major
text landing (the a_safe pin, the decomposition tiling, the P0
reduction, the k-row HOLE). The K3 conditional chain has NOT yet had
its dedicated seam hunt. YOUR JOB: try to BREAK the chain. A clean
"no seam found, here is the evidence" is a valid result only after the
attacks below are actually run.

## Deliverables

**D1 — THE CHAIN, QUOTED.** file:line for every link:
band_closure CONDITIONAL over {structural_surplus, crossing_location};
structural_surplus CONDITIONAL over {k3_distinct_slope_budget_ledger,
k3_independent_review}; the ledger CONDITIONAL over
{coordinate_positive_complete_payment, k3_orientation_assembly,
k3_allocation_inequality}; complete_payment CONDITIONAL over
coordinate_positive_remaining_route_payment. At each link: does the
child's stated conclusion, under its own quantifiers, actually supply
what the parent's gate consumes? Quote both sides. Any paraphrase gap
is a finding.

**D2 — THE ROW BRIDGE (the prime suspect).** The K3 lane is posed at
the KoalaBear row (the kb_m2_r4 prefix; p = 2130706433), while
band_closure's flagship row is n = 2^41, k = 2^40, q < 2^256. Find and
quote the declared bridge by which KB-row K3 certificates feed the
band-closure row. If the bridge is a stated hypothesis, quote it and
check both endpoints' conventions match. If NO statement-level bridge
exists, that is the finding of the round — document exactly what is
missing and its blast radius. Context: the lane pose is now the per-s
four-band family (notes/BAND_LANE_DEFINITIONS.md items 13-15, read
them); a KB-row instance may be legitimate family territory, but only
if some text SAYS so.

**D3 — CONSUMERS' CONSUMERS (CATCH-24C).** adjacency_closing consumes
band_closure's located adjacent pair; mca_safe consumes the safe half
AT THE LOCATED INDEX; mca_grand sits above. Check the located-index
quantifiers survive the decomposition + K3 chain: is "located" ever
weakened to "exists" or "bounded" along the way? Quote every consumer
clause.

**D4 — ATTACK LOG.** For each attack attempted (paraphrase-gap,
row-bridge, quantifier-weakening, owner/partition mismatch, chronology
gap): what you did, what would have constituted a kill, what you
found. Zero-power declarations where your search had no power.
Misses first.

## Constraints (binding)

- COMPUTE LAW: never bare python3. `tools/ramguard tiny -- python3 ...`
  (256M/60s) for peeks, `tools/ramguard local -- python3 ...` (1G/5min)
  for real runs, from the repo root, literal `--`. This includes JSON
  peeks and file patching. Stdlib only. No Modal, no network, no git.
- RAM DISCIPLINE: file-at-a-time reads; NEVER open dag.json (use
  node.json shards + grep); no bulk loads.
- WRITE SCOPE: you write ONLY inside
  notes/pilots_20260810/k3_chain_seams/. No dag/, nodes/, tools/
  edits. No git operations. Do not read or write the Codex worktree
  (any path containing prize-codex-); all banked results are in this
  repo.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md at
  any line. Never read the sibling round-30 dirs
  (k3_orientation_assembly, k3_allocation_inequality,
  k3_splitbc_transport). Prior-round dirs are readable.
- BLIND PRIORS: after reading ONLY the two anchors, append "## Pilot
  registrations" below (P(at least one real seam), the link you expect
  to be weakest, the expected row-bridge status) BEFORE any further
  read.
- REPORT: final artifact is REPORT.md in your dir. MISSES-FIRST.
  Every quantifier claim quoted file:line (CATCH-24C). Own-repo greps
  before any novelty claim (CATCH-24A).
- Banked scripts run from scratch copies only (copy into your dir).
