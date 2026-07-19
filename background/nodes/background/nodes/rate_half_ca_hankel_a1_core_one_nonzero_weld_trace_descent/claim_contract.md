# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_core_one_nonzero_weld_trace_descent`
- **mathematical statement:** every defect-domain and exceptional-slope trace
  of the nonzero weld has an exact gcd factorization `K=-HJ`; if all such
  traces vanish, the full split defect factor divides `K` and the weld
  descends to `W_1B_1-1=QK_1` in a strictly smaller degree box
- **scope:** only the official `A=1,s=1,e=2^38-1,ell=0` face
- **dependency:** the zero-weld exclusion, together with its inherited
  component capacity and two-sided complement identities
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **new open content:** exclude the active-trace factorizations and the
  reduced unit-product branch
- **falsifier:** a defect trace violating `(NWT4)` or `(NWT7)`, or a
  trace-free weld for which `B_XE_Z` does not divide `K`
- **nonclaims:** no exclusion of either branch, no claim that `K` is globally
  split, and no closure outside this one face
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_nonzero_weld_trace_descent/verify.py`
- **upstream mapping:** exact SPI ledger / nonzero shift-pair trace and
  factor-descent router
