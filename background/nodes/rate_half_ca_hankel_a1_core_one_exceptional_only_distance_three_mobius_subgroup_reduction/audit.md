# Audit

- The matching contributes ordered solutions: every fixed-point-free pair
  contributes both `(a_i,b_i)` and `(b_i,a_i)`.
- The absolutely irreducible curve bound is used only when
  `alpha gamma!=0` or after subgroup inversion when
  `gamma=0,alpha beta!=0`; all its printed hypotheses are checked.
- The `gamma=0,beta!=0` case is converted by subgroup inversion to a
  bidegree-`(1,1)` line with nonzero constant term before applying the same
  curve bound.
- The two cases outside those theorem hypotheses are retained exactly as
  the antipodal and constant-product dihedral branches.
- The verifier checks the official integer comparisons by exact integer
  powers, the field-size margins, and both surviving involutions.
