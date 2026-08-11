# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_first_degree_core_free_cubic_double_root_gap_one_normal_forms`
- **mathematical statement:** the `u=1` double-plus-simple cubic branch has
  exactly the four packets `(DGN2)`, the vertical/contact divisors `(DGN3)`,
  and the degree-one section counts `(DGN5)`
- **scope:** official first degree, core zero, scalar residual degree three,
  double-plus-simple branch, `u=1`
- **dependencies:** cubic root multiplicity router and core-free Forney
  contact section
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** excess degree outside the printed charges, another deficit
  partition, a different vertical/contact multiplicity, or an incorrect
  section count
- **nonclaims:** no packet is excluded
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_first_degree_core_free_cubic_double_root_gap_one_normal_forms/verify.py`
- **upstream mapping:** primitive shift-pair control / exact local
  second-moment ledger
