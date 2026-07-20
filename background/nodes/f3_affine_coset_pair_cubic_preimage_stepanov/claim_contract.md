# Claim contract

- **claim id:** `f3_affine_coset_pair_cubic_preimage_stepanov`
- **mathematical statement:** every fixed pair of nonproportional affine
  subgroup-coset conditions has fewer than `(51/16)m^(2/3)` solutions for
  `m=n` or `m=3n` at official H3 ambient rows
- **scope:** all official exponents `13<=s<=41`, whenever the stated subgroup
  of order `m` exists
- **consumer:** `f3_h3_dsp8_nodal_cube_preimage_envelope`
- **status:** `PROVED`
- **proved dependency:** the in-house Stepanov construction and sparse
  nonvanishing lemma
- **falsifier:** a failed parameter inequality in `(3)` or `(7)`, or an
  affine pair with at least `(51/16)m^(2/3)` solutions
- **nonclaims:** no sum over many affine fibers, no energy estimate, and no
  DSP8 payment by itself
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_affine_coset_pair_cubic_preimage_stepanov/verify.py`
