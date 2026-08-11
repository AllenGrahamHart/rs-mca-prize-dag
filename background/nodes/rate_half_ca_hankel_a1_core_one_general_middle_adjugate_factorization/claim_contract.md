# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_core_one_general_middle_adjugate_factorization`
- **mathematical statement:** every core-one residual square Hankel pencil
  has `adj M=Dqq^T` with `deg D=Delta`; the pole pushforward is an effective
  subdivisor of `div D`
- **scope:** every live half-distance `A=1,s=1` profile
- **dependencies:** core-stratified residual Kronecker and exceptional-root
  ledgers
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** a maximal minor outside the common factor `D`, a regular
  determinant of another degree, or a local pole multiplicity exceeding
  `ord_gamma D`
- **nonclaims:** `D` need not be squarefree, and its local order need not
  equal local rank loss or pole length
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_general_middle_adjugate_factorization/verify.py`
- **upstream mapping:** exact symmetric-Hankel / SPI second-moment ledger
