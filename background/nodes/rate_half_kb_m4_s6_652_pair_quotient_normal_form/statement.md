# KoalaBear m4 S6 (6,5,2) pair-quotient normal form

- **status:** PROVED
- **scope:** rigid passport `S6: 5.1,2.1.1.1.1,6`
- **dependency:** `rate_half_kb_m4_a6s6_genus_zero_passport_reduction`
- **consumer:** `rate_half_band_closure`

The rigid degree-15 outer cover with letter passport

```text
5.1, 2.1.1.1.1, 6
```

has the following rational normal form. Put

```text
Q4=u^4+176u^3+14520u^2+660176u+12576619,
Q6=u^6-330u^5+22143u^4+3380740u^3
   -372423117u^2-39333485730u-870224422859.
```

Then

```text
T(u)= -9566429400000 (u+44)^6 (u+55)^3
      / ((u+143) Q4(u)^2 Q6(u)),                    (KBM4-1)

T(u)-1= -(u+77)^5 (u^2-44u-4961)^5
         / ((u+143) Q4(u)^2 Q6(u)).                (KBM4-2)
```

The fibers over `0,1,infinity` have cycle profiles

```text
(6,6,3),       (5,5,5),       (2,2,2,2,1,1,1,1,1,1,1).
```

This map is the unordered-pair quotient of the rational degree-six BelyiDB
companion `6T16-[6,5,2]-6-51-21111-g0`.

For the KoalaBear field `K=F_(2130706433^6)`, the three order-five points of
`T=1` are

```text
-77,       22+33 sqrt(5),       22-33 sqrt(5),
```

and all three lie in `K`. Thus after replacing `T` by `T/(T-1)`, the required
three-point pole divisor splits over the challenge field.

## Falsifier

A failure of the exact pair-remainder determinant, conic parametrization, or
identities `(KBM4-1)`--`(KBM4-2)`; a repeated or shared factor in the printed
denominator; a different branch profile; or failure of `sqrt(5)` to belong to
the even-degree KoalaBear extension.
