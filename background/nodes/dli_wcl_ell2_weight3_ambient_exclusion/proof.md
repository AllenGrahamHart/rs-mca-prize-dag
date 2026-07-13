# Proof certificate

Encode a negative reduced term `-X^e` by the full exponent `e+512` in
`Z/1024`. A reduced signed weight-3 polynomial is then a three-set with no
antipodal pair, modulo translation by 512 for global sign.

Translation sends any chosen term to zero. Therefore every orbit under

```text
e -> a e + b mod 1024,  a odd,
```

meets the normalized section of legal three-sets containing zero. The compiler
enumerates all 521,220 distinct signed keys in that section. For each new
representative it applies every odd dilation and translates each of the three
terms to zero. These are exactly the intersections of its full affine orbit
with the section. The 510 resulting disjoint normalized orbits exhaust the
section, so the normalization argument covers all
`C(512,3)2^2=88,954,880` raw signed polynomials.

Modal/FLINT computes `Res(X^512+1,P)` for every class and PARI supplies a
factor ledger. The independent verifier checks each resultant at all 512 odd
powers of an exact order-1024 root modulo certified 31-bit primes. Their CRT
product exceeds `2*3^512`, while the product of the 512 complex conjugate
magnitudes is at most `3^512`; hence the modular checks prove exact equality.
Factor products reconstruct those norms.

The prime verifier recursively checks complete factorizations of `r-1`, trial
primality at the leaves, and the Fermat and gcd conditions for every supplied
Pocklington witness. Thus all 1,141 factor roots are prime. Direct inspection
finds zero roots below `2^256` with 41-bit splitting and maximum depth 21.

An `ell=2` vanisher must satisfy its first odd-index equation `P(omega)=0` at
an order-1024 root. Then `q` divides the certified cyclotomic norm. The
ambient production split requires `2^41|q-1`, contradicting the factor
ledger. The second odd-index equation is not needed for this exclusion.
