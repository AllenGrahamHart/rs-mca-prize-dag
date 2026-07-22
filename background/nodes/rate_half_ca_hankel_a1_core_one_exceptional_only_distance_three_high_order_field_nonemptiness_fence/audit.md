# Audit

- Probable-prime output is not trusted. The verifier recursively checks full
  `n-1` factorizations and Lucas witnesses using only integer arithmetic.
- The interval test uses exact floor division by `2^128`.
- The `e/3` example contains no factor `3` in `p-1`; the `e` example contains
  all three prime factors of `e`.
- Neither top-level factorization contains a prime factor of
  `r=7*79*8191*121369`, so the dual power map is bijective in both examples.
- This is a negative route result: it prevents an arithmetic-only exclusion
  but supplies no support, locator, or split-pencil data.
