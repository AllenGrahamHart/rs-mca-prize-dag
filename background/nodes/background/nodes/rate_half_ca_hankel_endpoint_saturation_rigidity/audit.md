# Audit

- The proof counts roots of `Q_gamma`, not merely roots of the specialized
  minimal generator.  Divisibility transfers all `rho-c_gamma` split roots
  to `Q_gamma`.
- `s=0` is essential: it makes every `Q_Z(x)` nonzero as a parameter
  polynomial, so each domain column has capacity at most `e=m`.
- Exceptional slopes are retained.  Their missing roots form `O`, and
  `O<=sum c_gamma<=m-1`; no generic-rank assumption is silently imposed on
  every supported slope.
- The `15/16` conclusion is a lower bound on saturated domain columns, not a
  claim that their chosen parameter-root subsets coincide.
- Divisibility by `H_Z` is pointwise after evaluating the binary variable at
  a saturated domain point.  It is not a global factorization of
  `Q_Z(X)` in `F[X,Z]`.
- The verifier checks the exact integer identities, adjacent-count mutation,
  deficit bound, and DAG wiring.  It does not certify nonexistence of the
  extremal incidence configuration.
