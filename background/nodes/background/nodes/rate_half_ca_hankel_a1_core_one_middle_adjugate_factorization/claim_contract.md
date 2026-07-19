# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_core_one_middle_adjugate_factorization`
- **mathematical statement:** on the `A=1`, `s=1`, `e=2m-1` face, the
  contracted middle-Hankel adjugate is exactly `lambda q q^T`, where `q` is
  the primitive residual apolar vector and `lambda` is the unique linear
  regular factor; all residual rank loss and root omission occur at its one
  projective root
- **scope:** the core-one maximal-degree face, with the norm-degree corollary
  restricted to sharp slope cap
- **dependency:** the core-stratified `A=1` residual router
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **new open content:** combine the maximal-minor products with the split-fiber
  and dominant rank-at-least-five constraints to exclude the mixed component
- **falsifier:** a maximal minor not divisible by the same linear form, a
  cofactor quotient not equal to `q_iq_j`, or a second residual rank-drop
  slope
- **nonclaims:** the adjugate identity does not classify the dominant
  component or close the face
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_middle_adjugate_factorization/verify.py`
- **upstream mapping:** exact SPI second-moment ledger / symmetric Hankel
  cofactor certificate
