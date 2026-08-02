# Source evidence

- Exact generic primitive polynomial: Modal app
  `ap-oyB5HrYYmeguXMKmqODnsw`.
- Exact generic factorization: Modal app
  `ap-yP081HXaVybgPvzsNW5FUX`.
- Primitive result:
  `rate_half_kb_positive_433_1a_cell5_pair_primitive_polynomial_result.json`.
- Factor result:
  `rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization_result.json`.
- Independent exact checkers:
  `check_rate_half_kb_positive_433_1a_cell5_pair_primitive_polynomial.py` and
  `check_rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization.py`.
- Hostile audits use the corresponding `audit_*.py` scripts.

A separate SymPy 1.14 audit was attempted but its fraction-field conversion
and multivariate finite-field factorization are unimplemented.  It supplies
no proof claim and its artifacts were discarded.  Both successful Modal apps
are stopped.
