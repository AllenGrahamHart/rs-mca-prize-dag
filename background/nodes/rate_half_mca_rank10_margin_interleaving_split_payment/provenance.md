# Provenance

This node is a local composition of proved packets already present in the
DAG.  Its support-local transversality and reversible gauge inputs were
harvested from `przchojecki/rs-mca` PR #1166 at
`af0e7c63b3d60873bf3fe2fc898edad85848deb5`.  The affine-span list compiler
was previously reconstructed from upstream `thm:affine-span-list`; the
interleaving collapse and near-rational charge are local proved results.

The threshold split, fixed-pair exception-coordinate injection, and exact
KoalaBear optimization are new in this node.

## Independent convergence (2026-08-13 addendum, coordinator PR review)

Upstream PR `#1167` (scottdhughes, 2026-08-13 18:44 UTC, stacked on
`#1166` at `b67078c7c`) independently packaged THE SAME theorem: the
identical margin/interleaving split formula, the identical optimum
`T = 667` with `high = 5143522968716559`, `low = 56727790457914040`,
`total = 61871313426765543`, `slack = 213109414684629544`
(`total + slack = B_*` exactly), the identical rank-11 minimum
`1040506078215897711` at `T = 876`, and the same `T = 16` first-paying
robustness check. Our proof (cycle 232, committed 06:40 UTC, exported
on the `#1165` comment thread) predates the PR by ~11 hours; the m2
export-collision protocol applies — record, do not contest; the
convergence is itself a strong external check.

`#1167` additionally contributes a `GF(11)` actual-record star proving
the fixed-pair `n-A` multiplicity cannot be improved from the current
local hypotheses (a sharpness control this node had not recorded), and
an explicit sextic-field guard note (`|F| = 2130706433^6`; the
sub-square test fails over the base prime field — consistent with this
node's field scope). Its isolated math and custody reviews are GREEN.
