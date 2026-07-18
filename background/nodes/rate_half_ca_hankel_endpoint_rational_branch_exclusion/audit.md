# Audit

- Factorization is over `Fbar[X,U,V]`.  Core-freeness removes content in `X`,
  parameter primitivity removes content in `(U,V)`, and Gauss's lemma makes
  the same factors irreducible over `Fbar(X)`.
- Every component specialization is nonzero.  An identically zero domain or
  parameter specialization would supply a forbidden univariate factor.
- `I_i` counts distinct zeros of component `i`.  The sum can exceed the
  distinct zero count of `Q` only through component overlap; retaining the
  nonnegative overlap `E` strengthens `(5)`.
- No parameter-root multiplicity or transversality is used in this theorem.
  The two elementary root bounds in `(3)` apply to arbitrary irreducible
  bidegree components.
- The defect sum is exactly one because `rho=4m-1`.  This arithmetic is what
  selects one dominant `(4e-1,e)` component rather than merely proving that
  some nonlinear component exists.
- The `m>1` hypothesis is needed only to infer that the dominant parameter
  degree is at least two.  The small fixture `1-ZX^3` is unaffected.
- The verifier checks all component upper bounds through `m=256`, small
  profile partitions, official constants, and DAG wiring.  It does not test
  the nonlinear-cover exclusion still required.
