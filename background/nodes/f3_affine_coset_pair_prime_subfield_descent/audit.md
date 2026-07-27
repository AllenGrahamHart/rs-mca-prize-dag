# Audit

- The argument is descent, not an extension of Mattarei: membership in the
  first prime-field affine form already forces the parameter into `F_p`.
- Nonzero slope is load-bearing. A constant first form would not force
  descent.
- Both the subgroup and affine coefficients must lie in the prime subfield.
  Merely placing the ambient curve over `F_(p^e)` is insufficient.
- Nonproportionality remains load-bearing for the Mattarei dependency.
- KoalaBear passes by exact divisibility and exact index arithmetic even
  though `p<n^2`; the dependency needs `d^3>=4m`, which holds directly.
- Mersenne-31 is explicitly fenced because its order-`2^21` subgroup is not
  prime-field-valued.
