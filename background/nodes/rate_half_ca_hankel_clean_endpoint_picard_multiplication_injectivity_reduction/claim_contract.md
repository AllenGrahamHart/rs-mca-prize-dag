# Claim contract

- **Claim:** a clean endpoint failure gives a nonzero kernel for `(PMI2)`,
  equivalently a nonnegative splitting summand in the explicit rank-`m`
  bundle `K_Q` of degree `m(5-4m)`.
- **Dependencies:** the degree-one Picard pin and four-Hankel bi-isotropic
  frame.
- **Output:** the exact cohomology map and kernel bundle subsequently
  classified by the elementary-modification child.
- **Consumer:** the clean branch of `rate_half_band_crossing_location`.
- **Nonclaim:** negative total degree is not promoted to injectivity, and no
  semistability of `K_Q` is assumed; the child proves injectivity impossible.
- **Falsifier:** a Picard section not mapping to `ker mu_Q`, an incorrect
  cohomology dimension, failure of fibrewise surjectivity, or a clean failure
  with `H^0(K_Q)=0`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_clean_endpoint_picard_multiplication_injectivity_reduction/verify.py`
  and `verify_audit.py`.
