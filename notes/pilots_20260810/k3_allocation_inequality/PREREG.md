# PREREG — k3_allocation_inequality (round 30)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation beyond the two
named anchors. AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `critical/nodes/rate_half_kb_m2_r4_k3_allocation_inequality/node.json`
2. `critical/nodes/rate_half_kb_m2_r4_k3_distinct_slope_budget_ledger/node.json`

## Mandate

This node (TARGET) demands: print the exact integers U_positive,
U_sourcecover, U_K3 = U_positive + U_sourcecover, and U_K3_allocation,
bind each input to its proof certificate and manifest digest, and prove
by exact integer arithmetic that U_K3 <= U_K3_allocation. Its falsifier
bans floating point, owner renormalization, omitted line multiplicity,
and any allocation imported from a different row or partition. Codex
closed the raw 433-1b workboard (wave 55) and the cell-11 uncolored
branch (wave 56); NOBODY has assembled the allocation dry run. YOUR
JOB: the provenance map and the dry-run inequality, at audit grade.

## Deliverables

**D1 — THE PROVENANCE MAP.** For each of the four integers: where is
it defined, produced, or gated (file:line)? Specifically: which closed
workboards feed U_positive; whether U_sourcecover is gated on the open
orientation_assembly TARGET (if so, say so and bound it instead); and
WHICH ledger/subtraction-table row defines U_K3_allocation — quote it
and verify the row/partition contract matches the K3 manifests (the
falsifier's imported-allocation clause is the seam to check).

**D2 — COMPUTE WHAT IS COMPUTABLE TODAY.** By exact integer arithmetic
from banked manifests (compute law below; stream-parse, checkpoint if
long). Pre-register every integer you extract, each with its manifest
digest. If a needed manifest is too large for the RAM law, checkpoint
in batches and record the batch boundaries.

**D3 — THE DRY-RUN INEQUALITY.** With today's integers: does
U_K3 <= U_K3_allocation hold, with how much slack, under which honest
placeholder for any unavailable summand? Report exact integers only.
An honest "blocked on certificate X" beats an estimated total.

**D4 — THE BINDING SCHEMA.** Draft what "bind each input to its proof
certificate and manifest digest" requires as a checkable artifact (a
schema the eventual verifier can enforce). Draft only, in your dir.

## Constraints (binding)

- COMPUTE LAW: never bare python3. `tools/ramguard tiny -- python3 ...`
  (256M/60s) for peeks, `tools/ramguard local -- python3 ...` (1G/5min)
  for real runs, from the repo root, literal `--`. This includes JSON
  peeks and file patching. Stdlib only. No Modal, no network, no git.
- RAM DISCIPLINE: file-at-a-time reads; NEVER open dag.json (use
  critical/nodes/*/node.json shards + grep); stream-parse large result
  JSONs; no bulk loads.
- WRITE SCOPE: you write ONLY inside
  notes/pilots_20260810/k3_allocation_inequality/. No dag/, nodes/,
  tools/ edits. No git operations. Do not read or write the Codex
  worktree (any path containing prize-codex-); all banked results are
  in this repo.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md at
  any line. Never read the sibling round-30 dirs
  (k3_orientation_assembly, k3_splitbc_transport, k3_chain_seams).
  Prior-round dirs are readable.
- BLIND PRIORS: after reading ONLY the two anchors, append "## Pilot
  registrations" below with your priors (where you expect
  U_K3_allocation to live, whether the dry run will be computable,
  expected slack sign) BEFORE any further read.
- REPORT: final artifact is REPORT.md in your dir. MISSES-FIRST.
  Every quantifier claim quoted file:line (CATCH-24C). Own-repo greps
  before any novelty claim (CATCH-24A). Zero-power declarations on any
  max-quantified claim.
- Banked scripts run from scratch copies only (copy into your dir).

## Pilot registrations

Registered after reading ONLY the two named anchors
(`critical/nodes/rate_half_kb_m2_r4_k3_allocation_inequality/node.json`,
`critical/nodes/rate_half_kb_m2_r4_k3_distinct_slope_budget_ledger/node.json`)
and BEFORE any other read, grep, or interpreter invocation.

### P1 — Where U_K3_allocation lives

P1a (60%): U_K3_allocation is defined in a *subtraction-table* /
budget-ledger note under `notes/` (prose or a small JSON), keyed by the
rate-1/2 KoalaBear row and a per-arm partition (K1/K2/K3/...), NOT in a
`critical/nodes/*/node.json` shard. Rationale: the anchor node's
falsifier speaks of "a different row or partition", which is
subtraction-table vocabulary, and the ledger node names an "active
allocation" as an external budget the K3 arm must fit inside.

P1b (25%): it lives in a machine-readable manifest/result JSON
(`results/` or similar) as a named field like `allocation` /
`budget_K3`, with a digest already banked.

P1c (15%): it is NOT pinned anywhere yet — only implied by a global
budget minus sibling-arm allocations, i.e. the row contract has to be
derived, which would itself be a MISS worth reporting.

I expect the *partition seam* (does the row that defines the allocation
use the same K1/K2/K3 partition and the same owner convention as the K3
manifests?) to be the weakest link, per the falsifier's
imported-allocation clause. Prior that I find at least one genuine
row/partition/owner mismatch or ambiguity: 45%.

### P2 — Computability of the dry run today

P2a (65%): PARTIALLY computable. I expect U_positive to be recoverable
by exact integer arithmetic from banked workboard manifests (waves 55
and 56 are described as closed), while U_sourcecover is gated on the
open `rate_half_kb_m2_r4_k3_orientation_assembly` TARGET and can only
be *bounded*, not printed. So the honest D3 output is an inequality
with a placeholder/bound for U_sourcecover, not a closed total.

P2b (20%): FULLY computable — both summands already banked with
digests, and the node is TARGET only because nobody assembled them.

P2c (15%): NEITHER summand is cleanly extractable at audit grade
(multiplicity or owner conventions unresolved), so the deliverable
degrades to a provenance map plus an explicit blocked-on-certificate
list.

Prior that I can print an exact integer for U_positive with a pinned
digest: 55%. For U_sourcecover: 25%.

### P3 — Expected slack sign

P3a (70%): the inequality HOLDS, i.e. U_K3 <= U_K3_allocation, with
strictly positive slack. Rationale: the ledger node is CONDITIONAL (not
refuted) and the arm was designed to fit; a designed-to-fit budget
usually carries deliberate headroom.

P3b (20%): it holds with slack exactly 0 (tight/saturated allocation) —
which would be a notable finding because any omitted line multiplicity
then flips the falsifier immediately.

P3c (10%): it FAILS with today's integers under the honest placeholder,
i.e. negative slack, most likely because a bound for U_sourcecover is
too coarse rather than because the true total exceeds the budget.

Prior that today's evidence is strong enough to *decide* the sign at
audit grade (rather than report "blocked"): 40%.

### P4 — Process priors

- Prior that some banked artifact already contains a floating-point
  comparison or a renormalized owner count that would trip this node's
  falsifier if imported verbatim: 35%.
- Prior that "line multiplicity" is recorded per-line somewhere but is
  summed with multiplicity dropped in at least one place: 30%.
- Zero-power warning registered in advance: any claim of the form "no
  file in the repo defines U_K3_allocation" will be made only if I have
  run greps over the whole repo for the token families I list in the
  report; otherwise I will declare zero power.

