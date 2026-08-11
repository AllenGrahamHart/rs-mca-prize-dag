# Audit

- The contracted matrix is square because `s=1` gives `d+1=rho`; this is
  not asserted for core-free or core-two profiles.
- The adjugate is nonzero because generic corank is exactly one.
- Primitivity is used twice: to make the rational kernel factor polynomial
  and to identify the scalar common cofactor factor.
- A root of `D` can have repeated Smith order or rank loss greater than one.
  Only `c_gamma<=ord_gamma D` is used.
- The pole divisor is pushed forward with multiplicity. Several pole points
  over one slope contribute a corresponding power of its linear form.
- `(GMA5)` uses the local pole-to-omission-to-rank-loss chain, not only its
  global degree inequality.
