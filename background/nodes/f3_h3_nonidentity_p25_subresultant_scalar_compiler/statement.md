# H3 nonidentity P25 subresultant scalar compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound` (evidence/router)
- **dependencies:** `f3_h3_global_resultant_compression`,
  `f3_h3_shifted_product_sidon`

Let `n=2^s`, `d=n-1`, `R=Z[1/2]`, and put

```text
F_n(X)=((1-X)^n-1)/X,
G_n(T,X)=X^d F_n(T/X).                             (PSC1)
```

Both have degree `d` in `X`; the leading coefficients `1` and `-n` are
units in `R`. For `0<=j<=24`, let

```text
S_j(T,X)=Sres_j^X(F_n(X),G_n(T,X))
        =sum_(ell=0)^j C_(j,ell)(T)X^ell           (PSC2)
```

be the `j`th polynomial subresultant, padding missing coefficients by zero.
Introduce an inverse-selector variable `Y` and define

```text
K_(n,24)=(C_(j,ell)(T):0<=j<=24,0<=ell<=j,
          (T-1)Y-1) in R[T,Y].                     (PSC3)
```

The quotient by `K_(n,24)` is a finite torsion `R`-module. Hence its scalar
annihilator has a unique positive odd generator

```text
(b_(n,24)^neq)=K_(n,24) intersect R.               (PSC4)
```

For every prime `p=1 mod n`, every order-`n` subgroup `H<=F_p^*`, and
`A=(1-H)\{0}`, one has the exact identities

```text
deg gcd_X(F_n(X),G_n(t,X))=P(t),                   (PSC5)
p divides b_(n,24)^neq
  iff some t!=1 has P(t)>=25.                      (PSC6)
```

Thus a factorization of `b_(n,24)^neq` gives the exact characteristic support
of the vacuous-DSP8 obstruction, with no identity or diagonal-boundary false
positive. Equivalently, at a fixed row, a checked Bezout/unit-ideal
certificate for `(PSC3) mod p` proves `max_(t!=1)P(t)<=24`.

This compiler starts from two degree-`n-1` sparse binomial polynomials and
`325` coefficient polynomials from the first twenty-five subresultants. Its
zeroth subresultant is the degree-`(n-1)^2` global product resultant, so the
theorem does not claim that symbolic elimination, coefficient growth, or
factorization is cheap. It is an exact alternate implementation contract,
not an official-row certificate or DSP8 close.
