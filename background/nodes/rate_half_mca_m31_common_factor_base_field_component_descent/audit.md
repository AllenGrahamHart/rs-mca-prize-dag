# Audit

- The rational objects being counted are polynomial pairs in
  `F[X]_<6^2`, hence points of the affine `(Y,Z)`-plane over `F(X)`.
- The characteristic guard is load-bearing.  It excludes a purely
  inseparable component field of definition before conjugation is used.
- Bezout is applied component by component to two distinct geometric
  irreducible curves, never to a component and itself.
- Points lying on several components are assigned once; the union bound
  therefore overcounts safely.
- Multiplicities in the full gcd are discarded by taking its radical.
- `sum delta_i^2<=d^2` remains valid when `P` has repeated factors.
- The one-component lower bound `132` is not used as if all `5079`
  cores belonged to that component.
- The verifier scans every degree `2..43`; the independent audit enumerates
  every degree partition through integer-partition recursion.
