# DRAFT — comment for przchojecki/rs-mca PR #750 (OUTWARD-FACING,
# awaiting maintainer approval before posting)

Thank you for the adversarial audit (`l1_imgfib_crosswalk_audit.md`) —
it's excellent work and it found a real gap. We've verified both
findings against our own artifacts and corrected our DAG accordingly:

1. **Clause 6 / the mixed-petal bucket — you are right, and we have
   demoted.** The `imgfib` node is re-demoted PROVED → CONDITIONAL on a
   newly minted open target `l1_mixed_petal_amplification` (the
   mixed-petal / diffuse partial-petal bucket, exactly as your §5
   identifies it). The cited "off-band induction" was indeed
   full-petal-only, and the mixed induction was retracted on our side
   on 2026-07-05. Our crosswalk's top-line is narrowed to what the
   artifacts support: **full-petal (top-band and below-top), periodic,
   and primitive instances are theorem-backed; the mixed bucket is
   open.** This matches your PROMOTE-WITH-CAVEATS recommendation; the
   HOLD on "L1 discharged" is correct.

2. **Clause 4 — accepted, and it's a strengthening.** The
   "entropy forces σ = Ω(n)" sentence is struck (false at the rows, as
   your recomputation shows). The surviving route is the one your audit
   states: clause (P) is proved at σ = 1, so the chain does not consume
   the H-scale hypothesis at all — dropped, not subsumed.

Both corrections are banked with full provenance (our catches #212 and
#213, crediting this audit) at
github.com/AllenGrahamHart/rs-mca-prize-dag (commit history + the
updated crosswalk annotations). The map at
allengrahamhart.github.io/prize-dag/ now shows the minted red.

One note that may interest your L1 lane: an autonomous campaign on our
side (~133 commits, 2026-07-13..15) appears to be attacking exactly this
diffuse/mixed allocation problem; we are audit-gating it now and will
present anything that survives through the same PR + crosswalk process,
with the narrower claim discipline this audit rightly enforced.
