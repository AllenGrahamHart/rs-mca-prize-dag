# Export record: MCA affine-span incidence counterexample (2026-08-13)

- **PR:** https://github.com/przchojecki/rs-mca/pull/1165
- **Branch:** `AllenGrahamHart:agent/mca-affine-span-counterexample`
  against upstream `main@93fba1be`.
- **Upstream commit:** `809c8e31`.
- **Local source:**
  `rate_half_mca_affine_span_incidence_counterexample@27be48115`.
- **Result:** an exact `GF(1009)` same-support pair-noncontained,
  direction-separated family has 31 slopes against the printed
  affine-span MCA bound 23.
- **Upstream repair:** replace `thm:affine-span-mca` by the counterexample,
  withdraw its two active-row payments, and add two independent exact
  verifiers.
- **Dependency alerts:** PRs `#1163` and `#1164` were notified that their
  inherited fixed-core codeword-affine-span staircase is invalid.
- **Surviving scope:** common-core cancellation, directional Johnson,
  gauge equivalence, ordinary affine-span LIST, and the selector-free
  all-LineRay error-affine-core set-pair theorem are not refuted.
- **Validation:** both upstream verifiers pass; `grande_finale.tex` builds
  to a 92-page PDF; `git diff --check` passes.
