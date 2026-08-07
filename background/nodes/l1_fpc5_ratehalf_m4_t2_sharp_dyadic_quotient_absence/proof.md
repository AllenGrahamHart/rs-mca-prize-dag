# Proof: sharp rate-half FPC5 pure dyadic quotient absence

The sharp locator degree

```text
j=2ell-3
```

is odd. Every proper divisor `M>1` of `n=2^41` is even. If
`F(X)=g(X^M)`, then

```text
deg F=M deg g,
```

so `M|j`, which is impossible.

Equivalently, multiplication by `mu_M` acts freely on the nonzero evaluation
domain `H_n`: if `zeta*x=x`, then `zeta=1`. Every complete orbit therefore
has size `M`, and a union of complete orbits has cardinality divisible by
`M`. It cannot have the odd cardinality `j`.

Thus the proper pure multiplicative periodic stratum is empty before any flat
or exact-contributor filters are imposed. QED.
