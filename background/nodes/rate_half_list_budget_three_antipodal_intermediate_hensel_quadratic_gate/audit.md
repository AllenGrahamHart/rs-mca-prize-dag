# Audit

- Re-derived the universal equation after substituting `C_u=C_*V`.
- Checked both coefficients of `V^3(1+qV)-1` through degree two.
- Checked the `z^(2h-1)` and `z^(2h)` extractions separately; the quadratic
  leading coefficient is one and therefore cannot degenerate.
- The verifier includes nondegenerate fixtures and an exact degenerate
  fixture where the quadratic has two roots, so “at most two” is sharp as a
  scalar gate.
- No polynomiality or split/Möbius conclusion is inferred from the two
  coefficient equations alone.
