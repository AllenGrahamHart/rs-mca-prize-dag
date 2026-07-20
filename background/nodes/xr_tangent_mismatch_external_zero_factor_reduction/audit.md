# Audit

The reduction retains the witness support and therefore avoids the invalid
existential-support inference. Its key invariant is the cancellation of the
same external-zero count `d` from agreement and dimension.

`verify.py` exhausts all nonzero degree-below-three polynomials, all
four-point witnesses, and all discrepancy sets on a six-point `F_7` domain.
For every admissible external-zero chart it checks divisibility, scaled
agreement, degree, radius, and invariant excess directly.
