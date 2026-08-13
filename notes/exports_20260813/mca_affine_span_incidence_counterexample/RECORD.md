# Export record: MCA affine-span incidence counterexample (2026-08-13)

- **PR:** https://github.com/przchojecki/rs-mca/pull/1165
- **Branch:** `AllenGrahamHart:agent/mca-affine-span-counterexample`
  against upstream `main@93fba1be`.
- **Upstream commits:** `809c8e31` for the counterexample and retraction;
  `75c61ae4` for the corrected occupancy theorem and exact walls.
- **Local source:**
  `rate_half_mca_affine_span_incidence_counterexample@27be48115`.
- **Result:** an exact `GF(1009)` same-support pair-noncontained,
  direction-separated family has 31 slopes against the printed
  affine-span MCA bound 23.
- **Upstream repair:** replace `thm:affine-span-mca` by the counterexample,
  withdraw its two active-row payments, prove `thm:proper-subspace-mca`, and
  add three exact verifiers.
- **Dependency alerts:** PRs `#1163` and `#1164` were notified that their
  inherited fixed-core codeword-affine-span staircase is invalid.
- **Surviving scope:** common-core cancellation, directional Johnson,
  gauge equivalence, ordinary affine-span LIST, and the selector-free
  all-LineRay error-affine-core set-pair theorem are not refuted.
- **Validation:** all three upstream verifiers pass; the corrected checker
  includes eight adjacent wall crossings, 616 zero-normal cases, the bound
  471 counterexample regression, and 540 exhaustive `GF(3)` toy families;
  `grande_finale.tex` builds to a 93-page PDF; `git diff --check` passes.
