# Claim contract

- **Claim:** cyclic rotation modulo the quotient-domain equation reduces the
  rate-half fixed-tail pigeonhole denominator from `q^d` to
  `N q^(d-1)`, giving the general `(CR1)--(CR2)` theorem. At the prize-max
  rate-half row, `c=2^33,d=1,s=c-1` yields at least
  `ceil(C(255,129)/256)>2^238` codewords at agreement `k+2^34-1`.
- **Quantifiers:** every finite field, multiplicative coset domain, divisor
  `c|n/2`, tail `0<s<c`, and `1<=d<=N/2-1`; the cap consequence is the printed
  official rate-half row.
- **Dependencies:** elementary finite-field and polynomial arithmetic only.
- **Nonclaim:** no MCA/CA lower witness, no list upper bound, and no assertion
  about the rate-half MCA crossing or an asymptotic list family.
- **Falsifier:** a variable coefficient outside `(a_0,...,a_(d-1))` appearing
  in degree at least `k`, more than `N` possible constant terms, a root created
  or lost by the cyclic reduction on `D`, failure of the exact Johnson gate
  `a^2<n(k-1)`, or failure of the cap comparison at `q=2^256`.

> QUANTIFIER UPDATE (wave-9, 2026-07-17): the band quantifier extends to
> 1 <= sigma <= sigma_max = 8,594,128,895 via the s = c-1 lemma
> (s-independence of the count); the sigma* form above is the historical
> first statement.

> OPTIMIZED UPDATE (wave-10, 2026-07-18): `c=2^33,d=1,s=c-1`
> supersedes the wave-9 endpoint. The proved unsafe band is
> `1<=sigma<=2^34-1`; the earlier `8,594,128,895` endpoint is historical.
