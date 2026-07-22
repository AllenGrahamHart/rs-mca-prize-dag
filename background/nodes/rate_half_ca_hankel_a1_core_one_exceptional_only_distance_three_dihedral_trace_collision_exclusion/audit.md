# Audit

- The count uses all nonexceptional orbit pairs, not only the lower-bound
  subfamily. Replacing their number by `3e-3` only weakens `(4)`.
- A block meeting both rows of an omitted exceptional orbit does not hurt
  `(4)`: a block with `2e+1` rows still meets at most `2e+1` members of the
  nonexceptional pair family.
- Quadratic classes are affine equality classes, not merely proportional
  coefficient vectors. This is required by the common value in `(2)`.
- The class-size cap uses only the leading `U^2` coefficient. It remains
  valid when that coefficient is zero because `M_0(xi_i)=mu_i!=0`.
- The threshold is exact for this argument: `e>=31` makes `d>=5`
  incompatible with `(6)`. The official `e=2^38-1` is far above it.
- No finite-field search, genericity assumption, or unproved injectivity of
  `gamma -> q_gamma` is used.
