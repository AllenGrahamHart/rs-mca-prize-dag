# Audit

- The character convention is pinned by `chi(3^j)=zeta_128^j` and the prime
  `q_1=(257,zeta_128-9)`.
- The valuation bit is `1-carry`, not `carry`; direct reduction at `q_1`
  catches this orientation error.
- The coefficients are ordinary integers, including negative entries, so
  `alpha` is a fractional cyclotomic integer.
- The relation is checked at all 64 primes above 257, not only at the four
  primes in its support.
- No class-number coordinate or annihilator-only inference is used.
