# Audit

- The affine center line is codeword-valued, so subtracting its derivative
  does not change syndrome moments in the degree range used by the pairing.
- `Q_min,alpha^2` kills the entire `S_alpha` contribution, including the
  overlap `S_alpha intersect S_beta`.
- Every remaining weight is nonzero: dual multipliers and actual error
  values are nonzero, and `Q_min,alpha` does not vanish off `S_alpha`.
- The rank bound is valid despite cancellation because it is a sum of
  rank-one evaluation forms.
- Vandermonde inversion is used only when the number of source points is
  exactly `c_alpha`.
- The `w=1` exceptional line is not silently discarded.
