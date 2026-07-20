# Claim contract

- **claim id:** `f3_h3_dsp8_primitive_shift_pair_adapter`
- **mathematical statement:** decorated ordered DSP8 edges are exactly a
  coefficient-primitive degree-three/depth-one split-locator shift-pair
  subclass, with `J=4K=8D`
- **scope:** every official dyadic H3 row and every retained DSP8 target
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **status:** `PROVED`
- **proved dependency:** the disjoint distance-six split-pencil router
- **new open content:** prove the quotient-weighted primitive-SP estimate in
  the current `f3_h3_dsp8_correlation_bound` contract; `(SPA7)` is the former
  stronger uniform target
- **falsifier:** one DSP8 edge whose decorated cubics fail `(SPA2)`, one
  admissible decorated record not reconstructed by `(SPA4)--(SPA6)`, or one
  nontrivial coefficient quotient scale at dyadic order and degree three
- **nonclaims:** no primitive-SP count, no marginal-to-correlated conversion,
  and no DSP8 or C36 promotion
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_dsp8_primitive_shift_pair_adapter/verify.py`
- **upstream mapping:** Przemek's `SP` terminology, specialized to the
  equal-constant degree-three/depth-one stratum and retaining the affine
  quotient-line weight
