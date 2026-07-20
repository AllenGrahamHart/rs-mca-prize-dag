# Audit

- `P(t)` counts ordered product representations; every generic unordered
  vertex is non-diagonal and consumes exactly two of them. This is why
  `2g(t)<=P(t)` has no diagonal correction.
- `N_6^disj(t)` is a subset of all unordered pairs of generic vertices. The
  proof does not assume every pair is a distance-six edge.
- The coefficient conversion is exact: `K=2D`, so the class weights `10,17`
  become `20,34` on `D`, and division by the edge ceiling eight yields
  `(10,17)/4` on `F`.
- Replacing the class-sensitive coefficients by the worst coefficient `17`
  is used only for `(RFC3)`. It is deliberately not used in `(RFC2)`.
- The factorial moment includes all `t!=1`, while `F_25` retains only the
  DSP8 cutoff. Nonnegativity makes this enlargement sound.
- A violation of `(RFC2)` or `(RFC3)` does not refute DSP8; those are
  sufficient moment routes, not equivalent reformulations.
