# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_root_normal_forms`
- **mathematical statement:** the core-one scalar quadratic chamber starts
  at `u=4`; there it has only the heavy-double and two-heavy-simple root
  patterns `(QG44)` and `(QG46)--(QG48)`, with exact section count in the
  double branch
- **scope:** official first degree, core one, parameter-constant residual
  degree two, minimum gap `u=4`
- **dependencies:** constant heavy-incidence identity, scalar root-row cube
  correction, and core-stripped Forney contact section
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** `u<4`, a nonzero omission or ordinary incidence at `u=4`,
  another root pattern, another simple-root deficit pair, an unallocated
  contact zero, or a noncanonical section in the double branch
- **nonclaims:** neither pattern is excluded; `u>=5` is untreated
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_root_normal_forms/verify.py`
- **upstream mapping:** primitive shift-pair control / exact local
  second-moment ledger
