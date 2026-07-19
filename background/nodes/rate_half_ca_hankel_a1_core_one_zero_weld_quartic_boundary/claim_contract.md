# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_core_one_zero_weld_quartic_boundary`
- **mathematical statement:** the two-sided weld can have `K=0` only when
  `b=0,D_*=1`; that branch is exactly a one-quarter bidegree factor
  `F-G_0=Q_*V_0` with split degrees `(4e,8e+4)` and exactly three omitted
  residual-domain factors
- **scope:** the official core-one maximal-degree sharp cap
- **dependency:** the two-sided complement weld and its component-degree
  bounds
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **new open content:** exclude the quartic separated-factor boundary and the
  nonzero-`K` welded branch
- **falsifier:** a zero-weld profile with `b>0`, `D_*=0`, exceptional factor
  allocated to `B`, or separated degrees other than `(4e,8e+4)`
- **nonclaims:** no classification of factors of `F-G_0` and no assertion
  about `K!=0`
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_zero_weld_quartic_boundary/verify.py`
- **upstream mapping:** split-pencil exact SPI ledger / quartic separated
  boundary
