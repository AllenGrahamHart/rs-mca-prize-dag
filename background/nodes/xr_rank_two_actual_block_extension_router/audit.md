# Audit

1. Polynomial division is by the monic extension locator `Lambda_T`, so the
   decomposition and dimensions are canonical.
2. The selected trade row removes one support-local dimension, not one
   extension-sensitive dimension.
3. The residual count is exactly `(d-z_i)+tau_i=h-1`; the `-1` is not hidden
   in the extension size.
4. Support interpolation uses all `d+1-z_i` local checks and is unique because
   `|S_i|>=a+1`.
5. The external zero set excludes `S_i`; otherwise `(AR9)` would overcount
   blocks by reselecting support coordinates.
6. Extensions may include points of the active zero set `Z_i`. No false
   disjointness between `T_i` and `Z_i` is imposed.
7. The binomial count is per fixed support and slope. It does not enforce
   pairwise block caps or first-core ownership across a family.
8. No Modal or candidate-row computation is used.
