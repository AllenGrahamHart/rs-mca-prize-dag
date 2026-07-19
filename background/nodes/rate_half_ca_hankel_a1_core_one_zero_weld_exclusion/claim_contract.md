# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_core_one_zero_weld_exclusion`
- **mathematical statement:** the zero-weld quartic boundary violates the
  exact dominant-component capacity ledger, so `K!=0` on every profile of the
  official core-one maximal-degree sharp cap
- **scope:** only the official `A=1,s=1,e=2^38-1,ell=0` face
- **dependency:** the exact zero-weld quartic-boundary classification, which
  in turn depends on the component norm ledger and two-sided weld
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **new open content:** exclude the remaining `K!=0` coupled matrix
  factorization
- **falsifier:** a zero-weld profile satisfying the dependency's exact
  capacity and quartic separated-factor identity
- **nonclaims:** no exclusion of `K!=0`, no exclusion of another core or
  degree, and no closure of the rate-half band
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_zero_weld_exclusion/verify.py`
- **upstream mapping:** exact SPI ledger / nonzero shift-pair weld
