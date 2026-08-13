# Mersenne common-factor weighted-degree bound

- **status:** PROVED
- **scope:** the common-factor branch at Mersenne `e=130237`
- **residual:** an MCA projective star, or factor `(Y,Z)`-degree `2..43`

Let `P` be the primitive full gcd of the weight-`(1,5,5)`,
degree-`264` interpolation kernel.  Then

```text
wdeg(P) <= 217,             deg_(Y,Z)(P) <= 43.
```

Consequently, in the higher-degree branch `2<=deg_(Y,Z)(P)<=43`, cofactor
Bezout captures at least

```text
7583-(52-2)^2 = 5083
```

selected degree-five polynomial pairs on `P`.  Their inside cores force
the received pair onto `P` at at least `126266` of the `130237`
inside coordinates, leaving at most `3971` exceptions.

This bounds the full gcd without assuming irreducibility.  It does not
classify or pay the higher-degree branch.
