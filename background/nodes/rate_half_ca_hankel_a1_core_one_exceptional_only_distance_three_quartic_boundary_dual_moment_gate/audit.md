# Audit

1. There are `d-5=2e-5` checks, indexed by `0<=j<=d-6`. An endpoint of
   `d-5` would add a false parity check.
2. The denominator cancellation uses `C(a)A'(a)`, not `C(a)` alone. This is
   why neither `C` nor `A'` appears in `(QBM2)`.
3. The trace in `(QBM3)` is the algebra trace from the split quadratic
   algebra `F[X]/(D_k)`. It is not a field-extension hypothesis.
4. Linear independence is asserted for the abstract RS parity checks on
   arbitrary boundary values. The specialized pair-Lagrange equations may
   have dependencies, and none are ruled out here.
5. The random `F_97` fixture is a negative control outside the external
   design. Its nonzero moment proves that pair-Lagrange and subgroup support
   data do not make the gate tautological.
