# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_core_one_two_sided_complement_weld`
- **mathematical statement:** the dominant component's domain-saturated and
  slope-clean complementary factorizations eliminate to the exact weld
  `(TSW7),(TSW8)`, with a separated defect factor of bidegree at most
  `(e-5b-1+D_*,1)`
- **scope:** the official core-one maximal-degree sharp-cap dominant component
- **dependency:** componentwise norm localization
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **new open content:** classify or exclude the welded matrix factorization
  jointly with the middle-Hankel adjugate products
- **falsifier:** failure of either complement, nondivisibility in `(TSW7)`, or
  a degree of `K` exceeding `(TSW9)`
- **nonclaims:** no assertion that `K` is zero, constant, or low rank; no
  stratum closure
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_two_sided_complement_weld/verify.py`
- **upstream mapping:** split-pencil exact SPI ledger / two-sided complement
  matrix factorization
