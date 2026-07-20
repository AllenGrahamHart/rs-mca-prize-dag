# Claim contract

- **scope:** official prime-field pair-Lagrange quotient-distance-three chart
- **input:** `Q`, internal slopes/scalars, core `s`, omitted row `x_0`, and
  the sparse subgroup polynomial `X^N-1`
- **currency:** multiplicativity of one resultant and explicit special-fiber
  resultants at `A` and `B`
- **output:** `(SSN4)--(SSN7)` and a sparse implementation of the exact
  resultant-power criterion
- **consumer:** `rate_half_band_closure`
- **load-bearing hypotheses:** exact support partition
  `(X^N-1)=(X-s)(X-x_0)ABC` and pair-Lagrange specializations
- **nonclaim:** the sparse norm identity does not prove that its quotient
  fails the split perfect-power test
- **failure certificate:** a nonzero coefficient in either side of `(SSN4)`
  after the printed scalar normalization
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_sparse_subgroup_norm_router/verify.py`
- **upstream mapping:** exact finite primitive shift-pair sparse subgroup-norm
  ledger
