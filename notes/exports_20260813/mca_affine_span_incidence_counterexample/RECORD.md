# Export record: MCA affine-span incidence counterexample (2026-08-13)

- **PR:** https://github.com/przchojecki/rs-mca/pull/1165
- **Branch:** `AllenGrahamHart:agent/mca-affine-span-counterexample`
  against upstream `main@93fba1be`.
- **Upstream commits:** `809c8e31` for the counterexample and retraction;
  `75c61ae4` for the corrected occupancy theorem and exact walls; and
  `0a4960f6` for the full-explanation lifted-rank dichotomy and top-rank
  branch split.
- **Local source:**
  `rate_half_mca_affine_span_incidence_counterexample@27be48115`.
- **Result:** an exact `GF(1009)` same-support pair-noncontained,
  direction-separated family has 31 slopes against the printed
  affine-span MCA bound 23.
- **Upstream repair:** replace `thm:affine-span-mca` by the counterexample,
  withdraw its two active-row payments, prove `thm:proper-subspace-mca`,
  prove the exact lifted-rank `K` versus `K+1` gauge dichotomy, and add four
  exact verifiers.
- **Top-rank narrowing:** the gauge-drop branches inherit the penultimate-rank
  suffixes `e>=992852` on KoalaBear and `e>=1037876` on Mersenne-31.  The
  full-lift branches retain `e>=1044239` and `e>=1044242`; their middle
  intervals remain open.
- **Dependency alerts:** PRs `#1163` and `#1164` were notified that their
  inherited fixed-core codeword-affine-span staircase is invalid.
- **Surviving scope:** common-core cancellation, directional Johnson,
  gauge equivalence, ordinary affine-span LIST, and the selector-free
  all-LineRay error-affine-core set-pair theorem are not refuted.
- **Validation:** all four upstream verifiers pass; the corrected checker
  includes eight adjacent wall crossings, 616 zero-normal cases, the bound
  471 counterexample regression, and 540 exhaustive `GF(3)` toy families.
  The lifted-rank checker exhausts 625 small-field gauges, one hostile
  perturbation, and both deployed adjacent rank-drop walls;
  `grande_finale.tex` builds to a 94-page PDF; `git diff --check` passes.
