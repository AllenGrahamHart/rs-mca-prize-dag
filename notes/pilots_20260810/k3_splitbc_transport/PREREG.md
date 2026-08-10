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

## Pilot registrations

Written after reading ONLY the two named anchors
(`notes/work_cycles/roadmap_r3/17-positive-433-repeat-bc-20260810.md` and
`critical/nodes/rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment/node.json`)
and before any other read, grep, or interpreter invocation.

### R1 — Expected transportable fraction

I expect the transport to be **asymmetric between the common side and the
outside side**, and I register that asymmetry as my headline prediction:

- **Common/source side: ~100% transportable.** The anchor already says the
  six `O0b` split lanes "share the certified split-common rank-drop locus
  from the closed `O0a` campaign" (cycle-17 note, Split-BC section). I
  predict the same holds one level up: the split-common tower, the
  product-rank stratification, and the `A/B` kernel reconstruction for the
  rank-five stratum are `O0b`-independent, because they are statements about
  the *source* system only, and the O0a/O0b distinction is an *outside*
  (target-endpoint) distinction. Predicted transportable fraction of the
  O0a **common-side** machinery: 90-100%.
- **Outside side: ~0-20% transportable as an emptiness certificate.** The
  same anchor sentence says explicitly "The outside graph is not
  transported; it is rebuilt for the six `O0b` lanes." I predict that
  generalizes: no O0a outside-emptiness certificate transports to O0b as a
  proof of emptiness. Predicted fraction of the 37,800 raw outside labels
  closed by pure transport of an existing O0a certificate: **0%**, with a
  1-in-4 subjective chance that a sign/role symmetry pays a clean half.
- **Quotient side: I predict a factor between 2 and 6 of exact label
  reduction** (not closure) from sign and role symmetries — specifically a
  `d -> -d`-type quotient (the cells-3/6 section used exactly that) and a
  `sigma_o in {-1,+1}` outside-sign quotient, possibly a third from the
  `S0 / SDE / SDF` lane structure. Point prediction: **4x**.

### R2 — Expected failure mechanism

Primary prediction: **the guard factorization fails to transplant, chart by
chart, because O0b's target guard is a different ideal from O0a's, so the
localization that made the O0a necessary ideal the unit ideal is not
available in O0b.** In concrete terms I predict the failure is *not* that
the source geometry differs, and *not* a rank drop; it is that the O0a
closure was "unit ideal after localizing by the complete target guard" and
the O0b target guard does not contain the same factor. This is the same
mechanism the PR #1155 fence describes for `433-1a` signed-pair guards, and
I predict the split block inherits it rather than escaping it.

Secondary prediction (30%): a second, independent failure at the
**rank-five vs rank-at-most-four boundary** — the closed branch is "split-BC
product rank at most four" (cycle-17), so the residual block is exactly the
open stratum where the product rank is maximal (five); I predict at least
one O0a component was proved only on the rank-<=4 locus and therefore has
*no content* on the rank-five stratum, i.e. it transports vacuously rather
than usefully. I flag in advance that "transports vacuously" must not be
scored as a success.

Tertiary prediction (20%): a sign-convention seam — the `sigma_o` outside
sign or the `epsilon_1 epsilon_2` source sign is fixed by a different
convention on the two sides, so a naive transport is off by a sign and
would silently pay the wrong half of the lanes.

I explicitly register that I expect my verdict to be **consistent with the
PR #1155 fence, not a refutation of it**. If I find myself concluding that
a guard-only closure of the split block IS available, I will treat that as
evidence of my own error first.

### R3 — Expected residue size order

- Raw block: 37,800 labels = 360 common rows x 105 outside labels/row. I
  register the arithmetic identity **37,800 = 360 x 105** and predict the
  same 105-per-row factor holds for the other two blocks
  (1,680 = 16 x 105 and 3,360 = 32 x 105) — if it does not, the "105-label
  outside ledger" is not uniform and D4 has a real miss.
- After the symmetry quotients of R1 I predict the residue that actually
  needs a census is **order 10^4, point estimate 9,000-10,000 raw labels**
  (37,800 / 4), and that the count of *representative systems* an eventual
  Codex census must run is **order 10^3, point estimate 1,000-3,000** (the
  cycle-17 precedents ran 720, 840, and 10,080 cases).
- I predict the eventual attack shape is **not** a monolithic per-system
  census: cycle-17 already records a 300s Modal cap on the monolithic
  all-variable outside ideal for cell 11, and I predict the split block is
  strictly harder per system, so a function-field / generic-rank atlas plus
  a finite boundary replay is the only viable shape. Predicted formal
  boundary degree to replay: order 10^2.

### R4 — Pre-registered misses I will look for (D4)

1. Does 360 + 16 + 32 = 408 actually equal the post-closure common-row
   count, or does the partition theorem quietly assume the closed blocks'
   rows are disjoint from the residual rows?
2. Is the 105-label outside ledger uniform across all three blocks, and is
   it the same 105 labels (same ledger) or three different ledgers of size
   105?
3. Are the 16 rank-drop points in common role cells 9/10 inside or outside
   the 360 rank-five rows? If inside, a row is double-counted; if outside,
   the "exhaustive" claim needs the 16 to be listed in some block.
4. Does the split block's "360 common rows" coincide numerically with the
   "360 representative residual-pairing systems" of the cells-3/6 uncolored
   payment? If so, is that a real coincidence or an index collision?
5. Does "raw outside labels" mean pre-quotient? If the 42,840 total is raw
   and the closed blocks were counted post-quotient, the totals are not
   commensurable.

### R5 — Zero-power pre-declaration

I register in advance that a null result from a grep over this repo has
**no power** to establish that a certificate does not exist upstream (the
Codex worktree is quarantined for me and PRs live on GitHub, which I cannot
reach). Any "no such certificate exists" claim in my report will be
downgraded to "no such certificate is banked in this repo at
<paths searched>", with the search paths quoted.

