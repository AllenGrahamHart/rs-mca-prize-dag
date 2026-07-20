# Audit

- Used the two-to-one trace map on inverse pairs; neither torsion root set
  contains `z=+/-1` after the stated exclusion.
- Squared both resultants, so the odd-degree resultant sign is immaterial.
- Included the Chebyshev leading coefficient `2^(2M-1)` on both branches.
- Kept all plus-branch exact orders `4,8,...,4M`; it is not one primitive
  cyclotomic factor.
- Replayed `U_(2M-1)=2M product_j T_(2^j)` with its scalar. Omitting `2M`
  changes the resultant by `(2M)^M`.
- Checked each `Phi_(4m)` level against the squared `T_m` resultant with the
  leading-coefficient denominator `2^(2M(m-1))`.
- Kept the `(-1)^M` in the quadratic norm of the minus factor; it is positive
  at official even `M` but negative in the `M=1` control.
- The odd-prime valuation statement uses rational valuations and does not
  assert that the norms are integers under an unstated normalization.
- Exact rational controls and an independent finite-field inverse-pair audit
  pass at small dyadic orders. No remote computation was used.
