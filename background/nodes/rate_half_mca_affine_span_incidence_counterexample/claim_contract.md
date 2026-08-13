# Claim contract

- **claim id:** `rate_half_mca_affine_span_incidence_counterexample`
- **status:** `PROVED`
- **field:** `GF(1009)`
- **row:** `(n,K,m,w,s)=(100,1,21,20,1)`
- **selected slopes:** `31`
- **affine-span bound:** `23`
- **direction-support bounds:** `22`
- **direction separation:** maximum direction agreement `20<m`
- **kill scope:** `rate_half_mca_supportwise_affine_span_compiler`,
  `rate_half_mca_direction_support_affine_basis_payment`, and
  `rate_half_mca_direction_support_common_zero_envelope`
- **survivors:** ordinary affine-span list decoding, gauge equivalence,
  directional Johnson, and the abstract shortening recurrence
- **replay:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_affine_span_incidence_counterexample/verify.py`
- **independent audit:** `tools/ramguard tiny -- python3 background/nodes/rate_half_mca_affine_span_incidence_counterexample/verify_audit.py`
