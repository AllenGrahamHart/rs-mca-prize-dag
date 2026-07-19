# Audit

- Expanded `V^3+qV^4` independently through degree three.
- Reduced both `u^2` and `u^3` by the monic quadratic and checked the printed
  coefficients `A,B` term by term.
- The verifier checks general exact polynomial fixtures and a degenerate
  fixture where the quadratic has two roots but the cubic remainder selects
  only the genuine one.
- The theorem leaves `A=B=0` open and does not infer polynomiality from the
  first three forbidden coefficients.
