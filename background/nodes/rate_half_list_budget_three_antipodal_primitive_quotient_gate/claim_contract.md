# Claim contract

- **claim id:** `rate_half_list_budget_three_antipodal_primitive_quotient_gate`
- **mathematical statement:** the antipodal welded map has odd degree `s-1`,
  so it is neither a nontrivial cyclic/dihedral quotient pullback nor the
  direct four-coset partition with one deletion per fiber
- **scope:** dyadic `d=4s` with `s>=4` inside the direct equal-fiber linear
  `K_4` antipodal component
- **consumer:** `rate_half_list_adjacent_crossing`
- **status:** `PROVED`
- **proved dependency:** antipodal Mobius weld
- **new open content:** exclude or construct the remaining primitive,
  nonperiodic solutions of the quartic norm equation
- **falsifier:** a valid welded solution of quotient-pullback form, or a
  four-coset partition whose deleted factors span dimension two
- **nonclaim:** no exclusion of arbitrary primitive pencils
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_list_budget_three_antipodal_primitive_quotient_gate/verify.py`
- **upstream mapping:** base-field-normalized split-pencil census, primitive
  versus quotient-periodic stratum
