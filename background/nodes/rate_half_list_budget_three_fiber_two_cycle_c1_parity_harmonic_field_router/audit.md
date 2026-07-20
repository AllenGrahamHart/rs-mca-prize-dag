# Audit

1. The cyclotomic field bound is denominator-only and transfers; the matched
   source equations do not.
2. The surviving field is `F_(p^2)` with `p=1 mod 2^40`, not
   unconditionally `p=1 mod 2^41`.
3. Both residual harmonic equations separately force `r in F_p`.
4. The `H_P` trace starts at `8/5` and needs 41 updates.
5. The `H_R` trace has an algebraic initial sign, but after one update is
   the rational value 16; it needs 40 further updates.
6. Composite candidate moduli remain useful no-hit supersets. Multiples of
   five are rejected as composite before division.

