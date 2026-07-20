# Claim contract

- **claim:** every parameter choice satisfying the current one-polynomial
  Stepanov constraints has constant greater than `2^(5/3)`, so two such
  class-blind bounds cannot pay the three-cubic-root nodal DSP8 lane;
- **scope:** the auxiliary-polynomial ansatz used by
  `f3_affine_coset_pair_cubic_preimage_stepanov`, not all possible Stepanov or
  incidence arguments;
- **consumer:** `f3_h3_dsp8_correlation_bound` as a route barrier;
- **dependencies:** the proved affine-pair ansatz and its proved use in the
  nodal envelope;
- **falsifier:** positive `m,A,B,D` satisfying `(NSB1)` but violating
  `(NSB2)`, or failure of the exact allowance comparison `(NSB4)`;
- **nonclaims:** no lower bound on actual point or record counts, no
  falsification of DSP8, and no barrier to target-sensitive or multi-fiber
  methods;
- **upstream mapping:** primitive shift-pair residual-ray control; marginal
  affine-fiber parameter tuning is the wrong endpoint for this weighted
  correlation.
