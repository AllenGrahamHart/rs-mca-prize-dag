# Audit

- The interpolation support is the fixed `e`-coordinate gauged support, not
  the full length `N`.
- The weight five on both value variables comes from `deg a,deg b<K=6`.
- Root counting uses 807 distinct evaluation points and degree at most 264.
- The 807 lower bound uses monotonicity in both the actual layer and the
  actual line size; neither is assumed equal to its forced minimum.
- Kernel dimension is only a rank-nullity lower bound; no generic-rank
  assumption is made.
- Bezout is applied over the algebraic closure of `F(X)` to two variables,
  where the total degree is at most 52.
- A common factor depending only on `X` is a unit over `F(X)` and is not the
  residual asserted by the theorem.
- The 2,705 pairs are distinct because each recursive step removes the whole
  affine explanation line.
- The threshold is evaluated after 2,704 charges, which is exactly what is
  required to force line 2,705.
- The theorem does not call the residual factor a split pencil; that requires
  a separate classification.
