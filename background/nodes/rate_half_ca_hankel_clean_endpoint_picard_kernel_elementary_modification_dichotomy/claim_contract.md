# Claim contract

- **Claim:** `K_Q` is the single-point positive elementary modification
  `(KED3)` and has exactly the two splittings `(KED4a)/(KED4b)`; the former
  makes `C` rational.
- **Dependency:**
  `rate_half_ca_hankel_clean_endpoint_picard_multiplication_injectivity_reduction`.
- **Output:** an exact two-branch clean frontier and a certified refutation of
  bare injectivity/all-negative splitting as a closure route.
- **Consumer:** the clean branch of `rate_half_band_crossing_location`.
- **Nonclaim:** neither splitting branch is excluded here.
- **Falsifier:** a different splitting of `pi_*O_C`, a modification length
  other than one, a third orbit of elementary modifications, or a branch
  `(KED4a)` whose degree-one pencil does not make `C` rational.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_clean_endpoint_picard_kernel_elementary_modification_dichotomy/verify.py`
  and `verify_audit.py`.
