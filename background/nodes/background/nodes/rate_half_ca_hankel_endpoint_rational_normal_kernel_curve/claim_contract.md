# Claim contract

- **Claim:** at the official first strict `A=3,e=m` endpoint, the unique
  right Kronecker block is `L_m`; therefore the `m+1` parameter coefficients
  of the full primitive generator are independent, its separation rank is
  exactly `m+1`, and its projective kernel family is a degree-`m` rational
  normal curve.  The proved endpoint split-fiber counts become the stated
  hyperplane-incidence counts on that curve.
- **Scope:** only the full primitive generator at the first strict endpoint
  `m=2^37`, not each irreducible component and not the remaining endpoint
  rows.
- **Dependencies:** `rate_half_ca_hankel_minimal_index_budget` supplies the
  common minimal index and Kronecker block description;
  `rate_half_ca_hankel_endpoint_component_defect_localization` supplies
  core-freeness and the split, saturated, and transverse fiber counts.
- **Consumer:** the strict `e=m`, `A=3` branch of
  `rate_half_band_closure`.
- **Nonclaims:** a general rational normal curve is not excluded; no
  contradiction follows from the incidence counts alone; the dominant
  irreducible component need not itself have maximal separation rank.
- **Next exact gate:** exploit the Hankel/apolar coefficient-chain equations,
  the multiplicative-domain evaluation hyperplanes, or the norm/Bezout
  factorization to rule out the printed rational-normal incidence profile.
