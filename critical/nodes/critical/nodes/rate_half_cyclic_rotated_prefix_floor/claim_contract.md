# Claim contract

- **Claim:** cyclic rotation modulo the quotient-domain equation reduces the
  rate-half fixed-tail pigeonhole denominator from `q^d` to
  `N q^(d-1)`, giving `(CR1)--(CR3)` and a full-cap list-unsafe witness.
- **Quantifiers:** every finite field, multiplicative coset domain, divisor
  `c|n/2`, tail `0<s<c`, and `1<=d<=N/2-1`; the cap consequence is the printed
  official rate-half row.
- **Dependencies:** elementary finite-field and polynomial arithmetic only.
- **Nonclaim:** no MCA/CA lower witness, no list upper bound, and no assertion
  about the rate-half MCA crossing.
- **Falsifier:** a variable coefficient outside `(a_0,...,a_(d-1))` appearing
  in degree at least `k`, more than `N` possible constant terms, a root created
  or lost by the cyclic reduction on `D`, or failure of `(CR3)` at `q=2^256`.

> QUANTIFIER UPDATE (wave-9, 2026-07-17): the band quantifier extends to
> 1 <= sigma <= sigma_max = 8,594,128,895 via the s = c-1 lemma
> (s-independence of the count); the sigma* form above is the historical
> first statement.
