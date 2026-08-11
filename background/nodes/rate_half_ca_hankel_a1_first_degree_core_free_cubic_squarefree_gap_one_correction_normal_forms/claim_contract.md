# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_first_degree_core_free_cubic_squarefree_gap_one_correction_normal_forms`
- **mathematical statement:** every squarefree core-free cubic packet at
  `u=1` has one of the three global charge regimes `(SGN1)`, exactly one
  correction row with `q=3`, and one of the local vertical/contact forms
  `(SGN5)--(SGN7)`
- **scope:** official first degree, core zero, scalar residual degree three,
  squarefree branch, `u=1`
- **dependencies:** cubic root multiplicity router and core-free Forney
  contact section
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** a fourth global charge regime, two corrected rows, an
  incorrect local multiplicity, residual contact degree outside `(SGN8)`,
  or a different Picard degree
- **nonclaims:** no positive deficit partition or packet is excluded
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_first_degree_core_free_cubic_squarefree_gap_one_correction_normal_forms/verify.py`
- **upstream mapping:** primitive shift-pair control / exact local
  second-moment ledger
