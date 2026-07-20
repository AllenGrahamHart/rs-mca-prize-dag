# Claim contract

- **claim id:**
  `rate_half_list_budget_three_antipodal_pure_harmonic_binary_quartic_norm_gate`
- **mathematical statement:** the eight lift-sign harmonic tests are exactly
  one symmetric degree-24 support norm, with both a three-step quadratic-norm
  certificate and a radical-free three-pair base-field formula
- **scope:** split squarefree deleted quartics with nonzero square roots in
  characteristic different from `2,3`
- **consumer:** `rate_half_list_adjacent_crossing`
- **status:** `PROVED`
- **proved dependency:** pure harmonic-Fermat router
- **new open content:** exclude the support norm zero locus after imposing
  the matched Fermat decomposition and ramification passport
- **falsifier:** a squarefree support for which `(BQN2)` depends on ordering
  or root choices, for which `(BQN4)--(BQN5)` disagrees with it, or for which
  its vanishing disagrees with harmonicity
- **nonclaims:** the norm is not nonzero on all official supports, and no
  harmonic-Fermat survivor is excluded by this node alone
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_list_budget_three_antipodal_pure_harmonic_binary_quartic_norm_gate/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census / pure
  harmonic SPI component
