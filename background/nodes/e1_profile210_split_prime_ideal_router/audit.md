# Audit

- The local census uses all even residual supports of size at most ten; it is
  a necessary valuation classification, not an assumption of distinct
  residues modulo `16`.
- Empty residual support is routed to valuation at least `16` and removed by
  the exact cofactor bound.
- The norm sieve checks prime exponents against multiplicative orders modulo
  `256`; it does not assume that all odd cofactor parts are prime.
- `257` and `769` occur to exponent one and split completely, yielding 128
  possible prime ideals each.
- Equal rational cofactors are not enough for a unit ratio: the extra prime
  ideal `Q_s` is fixed first.
- The height comparison is reused only after the ratio is proved to be an
  algebraic unit.
- Every surviving ideal family is restored as a full 256-vector orbit in the
  weighted charge.

