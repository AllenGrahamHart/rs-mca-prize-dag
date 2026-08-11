# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_first_degree_bounded_residual_table`
- **mathematical statement:** capacity forces the six first-degree ambient
  lifts, after removing all heavy domain rows, into residual bidegrees
  `(5,0),(12,1),(18,2),(2,0),(9,1),(15,2)`
- **scope:** `s in {0,1}`, `e=ceil((rho-1)/3)`, `j in {0,1,2}`
- **dependency:** first-degree ambient row-defect factorization and exact
  core-stratified capacity ledger
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** a profile whose capacity is compatible with fewer heavy
  rows than the table, or an arithmetic endpoint differing from
  `rho=3e-1`
- **nonclaims:** the bounded residual forms may still exist
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_first_degree_bounded_residual_table/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census
