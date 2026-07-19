# Claim contract

- **claim id:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_factor_descent`
- **mathematical statement:** the `b=0,D_*=1,c=z=1` exceptional-only active
  core factors through an exact complement square with one explicit
  degree-`D_0-r` correction polynomial
- **scope:** only the official core-one maximal-degree exceptional-only
  profile `(EFD1)`
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **proved dependency:** active-partition incidence reconstruction and its
  inherited active-core/component-norm chain
- **new open content:** exclude or classify the one-degree-relaxed square
  `(EFD6)` while imposing the Hankel chain, adjugate identity, and dominant
  irreducibility
- **falsifier:** valid data satisfying `(EFD1)--(EFD2)` for which `q_0` does
  not divide `P_X`, or for which the exact descent `(EFD4)--(EFD7)` fails
- **nonclaims:** no exclusion of the exceptional-only profile, no reuse of
  the trace-free degree contradiction, no closure of the other active
  profile, and no promotion of `rate_half_band_closure`
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_factor_descent/verify.py`
- **upstream mapping:** exact SPI / split-pencil one-exception active-factor
  descent
