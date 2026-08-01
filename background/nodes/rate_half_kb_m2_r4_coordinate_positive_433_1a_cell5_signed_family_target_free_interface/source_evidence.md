# Source evidence

- The universal target-elimination theorem supplies the signed `DE`, `DF`,
  `BE`, and `CF` record semantics.
- The cell-5 sparse kernel used by the ratio compiler gives `(KBSF-1)`.
- `experiments/prize_resolution/rate_half_kb_positive_433_1a_signed_family_target_free.py`
  checks the forward and converse rational identities exactly.
- Exact finite-field discovery runs found no seven-record independent Vieta
  completion among 368 common survivors over `F_17` or 1,072 over `F_29`:
  Modal apps `ap-kFi1MWruL9asXhwnUqi5US` and
  `ap-oEfa1ita3OEaMxXD5yKsxH`.  This is evidence only.
- The exact saturated common-curve quotient pilot
  `experiments/prize_resolution/rate_half_kb_positive_433_1a_cell5_signed_family_qring_modal.py`
  obtained common dimension six and basis size twelve after adjoining three
  source and two target variables.  Its six unsquared generators have
  `(degree,terms)=(15,96),(18,240)` repeated three times; quotient-compatible
  `std` timed out at 190 seconds in `ap-uG1IwuZNXrj32LwEaDaO5b`.
- Replacing the colored product row by the exact endpoint cubic gives a
  degree-14, 120-term generator but the combined basis still hit the same
  cap in `ap-OEAvKJxyhQn0ulMiNUF8Yq`; this is an algorithm boundary, not a
  survivor.
- Isolating only `DE+` and `DE-` leaves common-quotient dimension five,
  basis size twelve, and four 96/240-term unsquared generators.  Generic
  `std` still hit 190 seconds in `ap-cGvpVPiwsv1wiGLv3z4FHK`; the next
  required method is component decomposition, not a longer basis run.
- `experiments/prize_resolution/rate_half_kb_positive_433_1a_cell5_signed_family_decomposition_modal.py`
  recomputes the chart at the selected prime instead of reducing polynomials
  already normalized modulo the deployed prime.  Over `F_65521` it certifies
  one degree-four generic component (`ap-9rQUOuge1TNoa1ufF3u9MR`) and a
  reciprocal quartic with an exact quadratic trace lift
  (`ap-KCxeFPbJGAalI2aKR9nxem`).
- The resulting finite signed-pair system has cut ledgers
  `(9,24),(8,32),(9,24),(8,32)` but its `slimgb` computation timed out at
  240 seconds in `ap-F0mNsrUqkAmnr1ADk2V20i`.  The sealed telemetry is
  `experiments/prize_resolution/rate_half_kb_positive_433_1a_cell5_signed_family_decomposition_result.json`.
  These statements are exact over the probe field only.
- A deployed-characteristic replay reaches the 12-element affine common
  basis, then Singular rejects the function-field remap because
  `2130706433 > 2^29` (`ap-JwQiY0HAW4TvF01vmVmtPj`).  This is a backend
  limit, not algebraic evidence.
- The ordinary block-elimination replacement succeeds at the deployed prime.
  PROVED node
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_cell5_reciprocal_trace_quadratic`
  gives the one-generator reciprocal projection and its residual trace conic
  (`ap-D4GXYWOVhTEiEfabnKO9Ht`).
