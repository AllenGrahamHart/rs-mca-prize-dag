# Audit

- The norm is formed from all `N` nonzero homogeneous column forms, so its
  parameter degree is exactly `Nm`; no affine root at infinity is discarded.
- `u_gamma` counts distinct domain roots.  Extra multiplicity at a supported
  slope is deliberately left in `S`, making the divisibility argument valid
  without a transversality assumption.
- The omission form `J` records `rho-u_gamma`, not rank loss directly.  The
  preceding theorem proves only the required aggregate inequality
  `deg J=O<=m-1`.
- The positive deficit `1+O` implies that at least one column is nonsaturated;
  `(ENF3)` therefore has the lower bound `b>=1`.
- Complementary interpolation is coefficient-wise in the homogeneous
  parameter form.  Division by `P_sat` is exact because the identity vanishes
  as a polynomial in `(U,V)` at each distinct root of `P_sat`.
- The Bezout coefficient `Vbar` is only an interpolated complementary factor.
  Treating it as a second Hankel/apolar generator would be an unsupported
  strengthening.
- The clean-fiber count does not charge omitted-root slopes separately:
  `o_gamma<=c_gamma` puts them inside the rank-drop set.  It unions only the
  rank-drop and residual-multiplicity sets; overlap improves the lower bound.
- The product-code statement is near equality relative to every nonzero row
  and column.  It is not a claim that `M` is near the unrestricted global
  minimum distance, which permits entire zero rows or columns.
- The verifier checks degree identities, endpoint mutations, official
  arithmetic, clean-fiber and MDS-excess bounds, and DAG wiring.  It does not
  certify impossibility of the norm identity.
