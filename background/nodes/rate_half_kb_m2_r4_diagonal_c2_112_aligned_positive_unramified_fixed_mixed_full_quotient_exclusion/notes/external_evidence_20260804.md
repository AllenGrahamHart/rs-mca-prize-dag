
# External evidence, 2026-08-04 — Scott Hughes's PR #1149

External evidence, unmerged. PR #1149 (DRAFT), head
`55ac3e07477bd7a768190a3e755f22b0d44354b0`. CONTENT-REVIEWED, NOT REPLAYED.
This changes no status here and imports no theorem.

#1149 attacks a six-cell block it calls "the six aligned-positive unramified
cells", citing our #1143 workboard as the source of that instruction. It
proves named-open emptiness for two of them (F00-R11, F01-R11; named
localizer nilpotent of exact index three) and retains four as
two-dimensional q-slice schemes (F00/F01 x R02/R20). Certificate payload
`4adc4187bb5794ed70fce122055fb94916974c1adacf9451237aff002ebfd63e`.

Relation to this node, corrected 2026-08-07: the exact crosswalk is now
proved locally. The source templates are `fixed-moving=F00` and
`moving-moving=M00`; the allocations are `same=R20`, `swap=R02`, and
`mixed=R11`. Thus this node is exactly `F00-R11`. PR #1149 independently
proves named-open emptiness for that same cell and for `F01-R11`.

The former claim that our six canonical systems exhausted all literal
aligned-positive assignments was false in scope. They are
`{F00,M00} x {R02,R11,R20}`, not
`{F00,F01} x {R02,R11,R20}` and not the full 36-cell atlas. The branch-level
source-line theorem has therefore been downgraded to CONDITIONAL pending
literal-assignment coverage. PR #1149's four retained schemes remain OPEN,
not nonempty, and do not contradict any local cell theorem.

Note for readers of the sibling nodes: the `Still open: ...` lines in the
frontier files of the other five cells are CHECKPOINT-LOCAL (each was written
when that cell closed — "Four of six", "Five of six", "All six"). They are
historical, not stale, and must not be "corrected".
