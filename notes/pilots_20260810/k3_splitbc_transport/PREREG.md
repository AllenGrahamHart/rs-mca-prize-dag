# PREREG — k3_splitbc_transport (round 30)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation beyond the two
named anchors. AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/work_cycles/roadmap_r3/17-positive-433-repeat-bc-20260810.md`
2. `critical/nodes/rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment/node.json`

## Mandate

On route 433-1b -> O0b, the residual owner partition after the wave-55/56
closures is exact: split-BC product-rank-five (360 common rows, 37,800
raw outside labels — the BIG block), repeated-BC cells 1/2 (1,680), and
the cell-11/14 remainder Codex is actively paying. Codex's own
pre-registered next step for the split block: "the split-principal
block ... should first receive a transport/quotient audit against the
closed O0a owner machinery. Only then should another elimination
campaign be selected, preferring an exact transport or quotient over a
fresh per-system census." Codex is busy on cell 11. YOUR JOB: that
transport audit, done properly, delivered as a draft brief Codex can
execute. Do NOT run any census yourself.

## Deliverables

**D1 — THE MACHINERY MAP.** Locate (file:line) the closed O0a split-BC
owner machinery: which nodes/certificates closed the O0a split block,
by which mechanism (rank-drop locus, guard factorization, resultant
atlas, quotient). Then the O0b split-BC rank-five block's exact
definition. Table the differences: charts, guards, ideals, sign
conventions, role cells.

**D2 — TRANSPORT FEASIBILITY, PIECE BY PIECE.** For each O0a
component: does it transport to O0b exactly (by which quotient or
symmetry), or does it fail — and why, precisely? Acknowledge the
upstream PR #1155 fence as a hard datum: the 433-1a signed-pair guard
factorization does NOT transplant in at least one source chart, an
exact guarded necessary signed-pair point survives, so a guard-only
closure is unavailable and the residual quadratic cover must be
counted or routed to an owner. Your verdict must be consistent with
that fence or explicitly refute it with a certificate-level argument.

**D3 — THE DRAFT CODEX BRIEF.** A pre-registered attack shape for the
37,800-label block: transport where exact, census only for the
residue, with exact case counts per piece and the certificates each
piece would need. Draft only, in your dir; the coordinator decides
whether it ships to notes/codex_briefs/.

**D4 — MISSES AND SEAMS.** Anything the partition theorem quietly
assumes; anything in the 105-label outside ledger that does not
partition as claimed; any label double-counted or dropped between the
three blocks. Misses first.

## Constraints (binding)

- COMPUTE LAW: never bare python3. `tools/ramguard tiny -- python3 ...`
  (256M/60s) for peeks, `tools/ramguard local -- python3 ...` (1G/5min)
  for real runs, from the repo root, literal `--`. This includes JSON
  peeks and file patching. Stdlib only. No Modal, no network, no git.
- RAM DISCIPLINE: file-at-a-time reads; NEVER open dag.json (use
  node.json shards + grep); stream-parse large result JSONs; no bulk
  loads. The O0a/O0b result shards are LARGE — targeted reads only.
- WRITE SCOPE: you write ONLY inside
  notes/pilots_20260810/k3_splitbc_transport/. No dag/, nodes/, tools/
  edits. No git operations. Do not read or write the Codex worktree
  (any path containing prize-codex-); all banked results are in this
  repo.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md at
  any line. Never read the sibling round-30 dirs
  (k3_orientation_assembly, k3_allocation_inequality, k3_chain_seams).
  Prior-round dirs are readable.
- BLIND PRIORS: after reading ONLY the two anchors, append "## Pilot
  registrations" below (expected transportable fraction, expected
  failure mechanism, expected residue size order) BEFORE any further
  read.
- REPORT: final artifact is REPORT.md in your dir. MISSES-FIRST.
  Every quantifier claim quoted file:line (CATCH-24C). Own-repo greps
  before any novelty claim (CATCH-24A). Zero-power declarations on any
  max-quantified claim.
- Banked scripts run from scratch copies only (copy into your dir).
