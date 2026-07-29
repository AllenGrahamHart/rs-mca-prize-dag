# Proof - L1 Mersenne HNF m=8 aggregate norm-gcd compiler

The eighth roots are the distinct roots of `T^8-1` because every official
characteristic is odd. Therefore

```text
product_(zeta in mu_8)(T-zeta)=T^8-1.               (1)
```

Substitution `T=X^(p+1)` proves (ANG1).

If (ANG2) holds, Bezout gives polynomials `A,B in F_p[X]` with

```text
A P+B(X^(8(p+1))-1)=1.                              (2)
```

The same identity holds after extension to `K`. Every individual
`X^(p+1)-zeta` divides the second polynomial in (2), so no one can have a
nonconstant common divisor with `P`. This proves (ANG3).

Conversely, a nonconstant aggregate common divisor remains a nonconstant
common divisor after base extension from `F_p` to `K`. Factor one of its
irreducible divisors in the UFD `K[X]`. By (ANG1), that irreducible divides
the product of the eight individual norm polynomials, so it divides at least
one factor `X^(p+1)-zeta`. The corresponding individual gcd is nonunit.
Equivalently, coprimality with every factor of (ANG1) implies coprimality with
their product. This proves the converse and the stated equivalence. QED.
