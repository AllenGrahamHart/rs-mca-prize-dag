# Audit

- `H=B(I-J/n)B^T` is positive semidefinite and has rank at most `n-1`.
- The chord inequality is used only when `2A^2>=nc`, which makes its slope
  nonpositive for the lower bound on the total off-diagonal sum.
- The exact denominator identity is checked without floating point:
  `n^2*((A-p)^2-(n-1)p(c-p))=A^2*T`.
- Raw cumulative caps need not be monotone across the Johnson/Gram
  transition.  The suffix minimum is a proved closure, not an arithmetic
  convenience.
- The profile counts explanations first and applies deficit-dependent slope
  ownership separately.
- KoalaBear stops on a negative `T`; Mersenne stops on a valid but
  over-budget profile.  Neither is an unsafe certificate.
- All finite scans use exact integers and negligible memory.
