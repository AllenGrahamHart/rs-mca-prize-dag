# Claim contract

- **Claim:** deleting the marked row from the shifted/unshifted Hankel frame
  and combining the two sources gives a full-support dependence among at
  least `4m+1` quadratic Veronese tensors of saturated split locators.
- **Dependencies:** the four-Hankel frame, the clean one-deficit incidence
  profile, and the marked two-projection point.
- **Output:** a residual-free split-locator tensor dependence.
- **Consumer:** the clean branch of `rate_half_band_crossing_location`.
- **Nonclaim:** no general Veronese independence or official contradiction.
- **Falsifier:** a surviving `x_0` term, marked generic support below
  `4m+1`, a zero coefficient unavoidable in every source combination, or a row in
  `U` whose locator is not fully split and squarefree.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_clean_endpoint_marked_row_split_veronese_dependency/verify.py`
  and `verify_audit.py`.
