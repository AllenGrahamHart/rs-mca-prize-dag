# Claim contract

- **claim id:**
  `rate_half_list_budget_three_antipodal_pure_euler_ramification_router`
- **mathematical statement:** the pure quartic norm is equivalently one cubic
  Euler identity whose derivative is `U^2V^2L` with `L` linear, so its
  associated degree-`4r` polynomial has at most three finite critical values
- **scope:** maximal-row budget-three antipodal pure-quartic boundary; the
  algebraic theorem itself is stated for `d=4r+4` in good characteristic
- **consumer:** `rate_half_list_adjacent_crossing`
- **status:** `PROVED`
- **proved dependencies:** pure-quartic degree rigidity and exact reverse
  residual stratification
- **new open content:** classify the resulting low-critical-value polynomial
  together with the harmonic deleted-root and Fermat-factor matching
- **falsifier:** a valid pure norm packet failing the cubic identity, the
  derivative factorization, or the one-point defect localization
- **nonclaims:** low critical-value structure is not an emptiness theorem;
  no harmonic orbit, Fermat decomposition, generic/intermediate stratum, or
  budget-three crossing is excluded
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_list_budget_three_antipodal_pure_euler_ramification_router/verify.py`
- **upstream mapping:** exact finite split-pencil census, pure exceptional
  ramification interface
