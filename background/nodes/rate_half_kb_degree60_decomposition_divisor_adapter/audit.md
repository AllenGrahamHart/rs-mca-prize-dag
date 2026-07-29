# Audit

- Divisors, not affine formulas, include zeros and poles at infinity.
- Reducedness of `D_act` is load-bearing: order one forces both the outer
  zero and the inner map to be simple there.
- Degree exhaustion `n*m=60` prevents an omitted nonactive preimage.
- The source count is checked both by pullback degree and by the identity
  `a*m+b*m/5=12`.
- All eight rows are replayed independently by `verify.py` and
  `verify_audit.py`.
- Geometric fiber preservation is not promoted to coefficient-field descent.
