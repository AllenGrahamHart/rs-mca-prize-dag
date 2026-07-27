# Claim contract

- **claim id:** `f3_h3_dsp8_nodal_cube_preimage_envelope`
- **mathematical statement:** all singular-trace subgroup points form one
  affine intersection in the cube-preimage subgroup of order `gn`, yielding
  `(NCE3)--(NCE5)`
- **scope:** every official H3 row and all singular traces simultaneously
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **status:** `PROVED`
- **proved dependencies:** the exact nodal parameter router and the Mattarei
  affine coset-pair transport
- **new open content:** pay the smooth trace contribution in both
  characteristic classes while retaining quotient and class correlation
- **falsifier:** a singular subgroup point absent from `(NCE2)`, a parameter
  in `(NCE2)` with no unique singular trace, or a failure of `(NCE3)--(NCE5)`
- **nonclaims:** no smooth-trace estimate and no combined DSP8 payment;
  `892` is retained only as the historical stronger F-round target
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_dsp8_nodal_cube_preimage_envelope/verify.py`
