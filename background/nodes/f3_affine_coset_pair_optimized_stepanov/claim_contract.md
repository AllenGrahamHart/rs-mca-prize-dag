# Claim contract

- **claim id:** `f3_affine_coset_pair_optimized_stepanov`
- **mathematical statement:** one fixed pair of nonproportional affine forms
  simultaneously taking values in an official dyadic subgroup has fewer than
  `4n^(2/3)` inputs
- **scope:** all 29 official subgroup orders and every prime-field row in the
  official aspect range
- **consumer:** `f3_h3_dsp8_nodal_trace_parameter_router`
- **status:** `PROVED`
- **proved dependency:** the in-house h=2 Stepanov auxiliary-polynomial and
  sparse nonvanishing theorem
- **falsifier:** an in-scope affine pair with at least `4n^(2/3)` solutions,
  or a failed inequality in `(6)`
- **nonclaims:** no `T>1` rich-coset improvement, no energy constant, and no
  DSP8 bound by itself
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_affine_coset_pair_optimized_stepanov/verify.py`
