# Claim contract

- **Claim:** every nonzero tangent support mismatch factors to a punctured
  GRS close-slope chart with invariant excess `h=A-K`.
- **Input:** one exact-`A` witness, one recovered codeword pair, and its
  discrepancy support.
- **Output:** external locator `P_W`, dimension `K-d`, agreement `A-d`, and
  radius `R-h` on `T`.
- **Consumer:** the official XR tangent/support-mismatch bridge.
- **Nonclaim:** no canonical atlas, no sum over `W`, and no `16n^3` bound.
- **Falsifier:** a nonzero witness for which `P_W` does not divide `q_z` or
  the excess changes after division.
