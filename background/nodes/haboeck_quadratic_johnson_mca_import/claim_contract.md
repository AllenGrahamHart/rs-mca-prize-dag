# Claim contract

- **Claim:** Haboeck Theorem 2, restricted to two received words and finite
  affine slopes, with the exact repository dimension reindexing.
- **Input:** an arbitrary Reed-Solomon evaluation set over a finite field and
  an integer `m>=3` for which `gamma_m>0`.
- **Output:** the bad-slope numerator bound `(HJ1)`.
- **Consumers:** exact finite-row MCA safe brackets, beginning with
  `rate_half_haboeck_quadratic_johnson_safe_bracket`.
- **Nonclaims:** no BCHKS25 linear bound, no curve sampler of degree greater
  than one, no projective-slope normalization, no ordinary LIST bound, and no
  beyond-Johnson conclusion.
- **Falsifier:** a mismatch between the source event and the repository's
  same-support MCA event, an incorrect `K-1` reindexing, or an unproved
  source step needed for `(HJ1)`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/haboeck_quadratic_johnson_mca_import/verify.py`.
