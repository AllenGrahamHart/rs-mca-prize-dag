# KoalaBear m4 S6 (5,6,2) pair-quotient normal form

- **status:** PROVED
- **scope:** rigid passport `S6: 5.1,2.2.2,3.2.1`
- **dependency:** `rate_half_kb_m4_a6s6_genus_zero_passport_reduction`
- **consumer:** `rate_half_band_closure`

Put

```text
A2=25444u^2-50922u+15129,
C3=14658356u^3-31403007u^2-8441982u+33495606,
C6=915512069923328u^6+6554290056691968u^5
   -83250949083482880u^4+290661295480797960u^3
   -474965645409866205u^2+379227334439635443u
   -119893424310248247.
```

Then the rigid degree-15 outer cover with letter passport
`5.1,2.2.2,3.2.1` has rational normal form

```text
T(u)=177147(188u-287)^5 A2(u)^5/(C3(u)C6(u)^2).      (KBM4-3)
```

Moreover,

```text
numerator(T)-denominator(T)
=3125(88u+123)^2(89u-123)^3(208u-369)^6
       (683u-1107)^3(980u-1599).                    (KBM4-4)
```

The fibers over `0,1,infinity` have profiles

```text
(5,5,5),       (6,3,3,2,1),       (2,2,2,2,2,2,1,1,1).
```

This is the unordered-pair quotient of BelyiDB's rational degree-six
companion `6T16-[5,6,2]-51-321-222-g0`.

For `K=F_(2130706433^6)`, the three order-five points are

```text
287/188,
(25461+7257 sqrt(5))/25444,
(25461-7257 sqrt(5))/25444,
```

and all lie in `K`. Thus after replacing `T` by `1/T`, the required
three-point pole divisor splits over the challenge field.

## Falsifier

A failure of the pair-remainder determinant, cubic-adjoint residual
factorization, identities `(KBM4-3)`--`(KBM4-4)`, denominator coprimality,
branch profile, or even-extension pole descent.
