# Claim contract

- **Claim:** exact pinning, normal form, and coupled match-budget rigidity for
  non-tangent sparse MCA witnesses, plus tangent payment for official
  rate-half fields of at least 168 bits.
- **Quantifiers:** every RS code and every sub-capacity agreement `a=k+tau`
  with `1<=tau<=n-k-1`; `(PR4)` specializes to the official rate-half row.
- **Dependencies:** Reed-Solomon root counting and support-wise MCA
  definitions.
- **Consumer:** sparse-mutual term exposed by
  `rate_half_mca_sparse_layer_reduction`.
- **Nonclaims:** no count of the non-tangent coupled system and no far-pair CA
  bound.
- **Falsifier:** a non-tangent bad slope with `e<=tau`, no active matched
  coordinate, cofactor degree above `e-tau-1`, or violation of `(PR3)`.
- **Upstream crosswalk:** `tex/towards-prize.tex`, Theorems
  `thm:sparse-threshold`, `thm:pinning`, and `thm:rigidity`.
