# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_core_one_active_trace_core_reduction`
- **mathematical statement:** cancelling all zero defect traces gives the
  exact active-core system `(ACR4)`; either every bad-domain trace is active,
  or one zero trace occurs in one of the two `b=0,D_*=1` boundary profiles
  in `(ACR6)`
- **scope:** only the official `A=1,s=1,e=2^38-1,ell=0` face
- **dependency:** trace-free weld exclusion and the inherited local trace
  factorizations
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **new open content:** exclude the all-active domain cores and the two
  one-zero-row boundary cores
- **falsifier:** a zero domain trace not dividing `A,B,K`, a failure of
  `(ACR4)`, or a zero-trace capacity profile outside `(ACR6)`
- **nonclaims:** no exclusion of any active core and no assertion that the
  exceptional trace is always active
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_active_trace_core_reduction/verify.py`
- **upstream mapping:** exact SPI ledger / minimal active shift-pair core
