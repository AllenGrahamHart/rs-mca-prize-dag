# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_core_one_component_norm_localization`
- **mathematical statement:** every component on the official core-one
  maximal-degree sharp cap has all omissions localized at the unique regular
  slope and satisfies its own exact norm-power and complementary
  factorization; the dominant residual degree is `e-5b-1+D_*`
- **scope:** only the official `A=1,s=1,e=2m-1,ell=0` face
- **dependencies:** unique dominant component localization and the
  middle-Hankel adjugate factorization
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **new open content:** exclude the dominant rank-at-least-five biform under
  `(CNL6)--(CNL8)`
- **falsifier:** a component omission away from `lambda=0`, a component
  deficit violating `(CNL5)`, or failure of a component norm identity
- **nonclaims:** no dominant-component classification or stratum closure
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_component_norm_localization/verify.py`
- **upstream mapping:** exact SPI component norm ledger / base-field-normalized
  split-pencil census
