# Claim contract

- **Claim:** after the exact row scaling `s_x=B(x)G_x(0)`, every external
  complement is a fixed quadratic conic in the row coordinate modulo `I`,
  plus a unique degree-`e` kernel lift; all lifts jointly obey the exact
  perfect-power identity `(CKL6)`.
- **Scope:** the official `A=1`, core-one, exceptional-only,
  quotient-distance-three pair-Lagrange external design.
- **Dependencies:** pair-Lagrange normal form, exact external split-design
  saturation, and the calibrated complement-residue gate.
- **Consumer:** `rate_half_band_closure`; theorem interface for the saturated
  generic branch and for `CR-003-CLIFT`.
- **Falsifier:** a valid design for which `(CKL5)` fails with the printed
  interpolation data, `[z^e]J_x!=s_x`, or the product exponent is not
  `4e+2`.
- **Nonclaims:** no low rank, bounded row degree, pencil decomposition, or
  exclusion theorem for the kernel lifts is asserted.
