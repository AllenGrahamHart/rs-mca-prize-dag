# Claim contract

- **claim id:** `rate_half_list_budget_three_multifiber_vandermonde_exclusion`
- **mathematical statement:** one-root-deleted locators from equal-size unions
  of fibers of one monomial quotient map are Vandermonde-independent whenever
  the fiber size is at least the number of locators
- **scope:** direct one-map, equal-fiber completions; applied to the four cycle
  locators and the three path tight-triangle locators
- **consumer:** `rate_half_list_adjacent_crossing`
- **status:** `PROVED`
- **proved dependency:** budget-three linear Grassmann atlas
- **falsifier:** distinct `r_i`, `t<=m`, and nonzero constants `lambda_i` for
  which the locators `(MVE1)` satisfy `sum lambda_i A_i=0`
- **nonclaims:** no exclusion of fiber sizes one or two, mixed or incomplete
  fibers, different quotient maps, primitive locators, or the other seven
  budget-three chambers
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_list_budget_three_multifiber_vandermonde_exclusion/verify.py`
- **upstream mapping:** finite adjacent-row base-field-normalized split-pencil
  census / quotient-periodic exclusion
