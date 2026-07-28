# Audit

- The proof uses no sampled or floating-point inequality.
- `verify.py` checks the local chord inequality exhaustively over all chord
  multiplicities allowed by this profile.
- The verifier reconstructs all 52, 57, and 73 layer profiles and the exact
  maxima `Phi=4702,5118,5950`.
- The Hermite coefficients and moment substitution are checked as exact
  linear forms in `log 15` and `log 66`.
- All strict logarithmic comparisons use rational atanh partial sums and
  explicit geometric tails.
- The exact field-floor comparison is performed after raising to the fifth
  power; no decimal approximation to `2^259.8` is used.
- The primary normalized census scanned all `320292000` vectors in Modal app
  `ap-xUAM32cidKtQXwQEyFjKZM`. An independent lexicographic engine using a
  full 128-slot convolution agrees on every chamber and `(E,L)` cell after
  its complete run `ap-PPOc61mOxwR0pClp4jTjwI`.
- The dual census has `V=10` empty and exactly `540332` vectors through
  `V=106`. These counts guide the next attack, but no count is load-bearing
  for the analytic theorem proved by this node.
