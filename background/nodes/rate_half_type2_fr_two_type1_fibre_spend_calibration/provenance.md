# Provenance

- **local arithmetic parent:**
  `rate_half_type2_fr_exact_spend_calibration` at local commit `410284e7f`;
- **local structural parent:**
  `rate_half_ca_hankel_endpoint_saturation_rigidity`, as compiled at the
  same commit;
- **notation and representation-pair source:**
  `notes/pilots_20260810/rh_type2_stratum/PREREG.md:82-94` and
  `REPORT.md:15-19,232`, pinned by local commit `410284e7f`; the proof here
  extends the banked supported-supported comparison to a supported vector
  and an arbitrary distinct projective member by writing their two syndrome
  directions explicitly;
- **coordination check:** canonical Fable tree at committed head
  `45cf661a6`; its Round-32 pilot files were dirty and are explicitly not
  imported as evidence;
- **upstream check:** `przchojecki/rs-mca` main
  `93fba1be3f3299b0ba4708d88715377bbb656e45`; 11 open PRs were inspected
  on 2026-08-10, and none states this endpoint calibration;
- **novelty scope:** the projective fibre identity is elementary. The
  bankable contribution is its exact composition with the corrected
  `9m/4+1` spend target and the resulting `25m/4` concentration threshold;
- **computation:** none beyond deterministic integer replay under RAMguard.
