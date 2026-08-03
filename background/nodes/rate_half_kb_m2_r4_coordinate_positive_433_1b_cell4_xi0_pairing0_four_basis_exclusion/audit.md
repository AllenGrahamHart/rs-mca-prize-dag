# Audit

- The norm is used only in the sound direction `target-free element zero`
  implies `multiplication determinant zero`; no field or irreducibility
  assumption is made for the second quadratic algebra.
- Every inverse introduced by base normalization, `b` normalization, linear
  `c` recovery, and missing-record evaluation is included in the candidate
  root union.  Denominator roots are not silently discarded.
- Candidate roots are lifted before exclusion.  The five early rejections are
  exactly `r=0`, `r^2=1`, or `r^2=-1`; the other two satisfy `t^2=-1`.
- The independent audit reconstructs field-root gcds from the stored
  polynomials; it does not trust the compiler's printed root lists.
- Target-lane multiplication is valid because neither `sigma_c` nor `sigma_o`
  occurs in the target-free opposite-`DE` cut.
- The result pays one of `7*15=105` missing/matching slices only.
