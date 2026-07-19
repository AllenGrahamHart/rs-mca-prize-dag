# Proof

Fix `tau in F_p^*\{1}`. The change of variables

```text
U=x,             V=x/y
```

is a bijection of `H^2`, with inverse `(x,y)=(U,U/V)`. After multiplying
`(1-U)(1-U/V)=tau` by `V`, the product-fiber equation becomes

```text
Q_tau(U,V)=U^2-UV-U+(1-tau)V=0.                       (1)
```

This normalization preserves the subgroup domain. Its lowest nonzero
homogeneous part is

```text
-U+(1-tau)V,
```

which has two monomials because `tau!=1`.

## Algebraic hypotheses

Regard `(1)` as a polynomial in `V`:

```text
Q_tau(U,V)=U(U-1)+(1-tau-U)V.
```

A polynomial linear in `V` can factor only if its two coefficients have a
nonconstant common divisor. Their only possible common roots are `U=0,1`;
at these points `1-tau-U` is respectively `1-tau` and `-tau`. Both are
nonzero. Thus `Q_tau` is irreducible. Its bidegree is `(m,l)=(2,1)`. The
total degrees in its support are `2,2,1,1`, so the integer `g` in equation
(1.9) of Konyagin--Shparlinski--Vyugin is `1`.

We specialize the auxiliary-polynomial proof of their Theorem 1.2, Section
4, to one polynomial. The independence condition is then vacuous. We use the
displayed construction itself, checking its finite conditions, rather than
the theorem's unspecified large-order constant.

Put `x=n^(1/3)` and choose

```text
A0=floor(10x^2/11),       B=floor(11x/10),
C =floor(11x/5),          D=floor(3x^2/10).           (2)
```

For the three exceptional rows `s=14,16,17`, increase `C` by respectively
`2,1,2`. No other parameter changes.

For `h=g=1`, `m=2`, and `l=1`, equation (4.2) of the source proof is

```text
4(A0 D+3D^2)<A0 B C.                                (3)
```

The left side of `(3)` is at most

```text
4((10x^2/11)(3x^2/10)+3(3x^2/10)^2)=(597/275)x^4.
```

For `s>=21`, `x>=128`, while the unadjusted value of `C` gives

```text
A0 B C>(10x^2/11-1)(11x/10-1)(11x/5-1).
```

After division by `x^4`, each factor is positive and increasing for
`x>=128`. At `x=128`, its difference from `597/275` is

```text
410641581/73819750400>0.
```

This proves `(3)` from `s=21` onward. The remaining official rows are the
following exact integer checks; the displayed `C` includes the three
adjustments.

```text
s     A0    B    C     D       4(A0D+3D^2)       A0BC
13    369   22   44   121             354288      357192
14    586   27   57   193             899380      901854
15    930   35   70   307            2273028     2278500
16   1477   44   89   487            5723224     5783932
17   2345   55  113   774           14449032    14574175
18   3723   70  140  1228           36383184    36485400
19   5910   88  177  1950           91728000    92054160
20   9382  111  223  3096          231209280   232232646
```

Moreover, `10x^2/11` is never an integer on an official row: it is
irrational when `3` does not divide `s`, and when `3` divides `s` its
denominator `11` cannot divide a power of two. Hence

```text
A0 B<(10x^2/11)(11x/10)=n.
```

Also `B+C-1<n` for `x>=20`, including the three adjusted rows by direct
inspection. Consequently

```text
(B+C-1)n<n^2<=p.                                    (4)
```

Lemma 2.4 of the source therefore makes the auxiliary polynomial coprime to
`Q_tau`; the multiplicity and degree hypotheses are all satisfied.

## Explicit root count

Equation (2.3) and Lemma 2.1 of the source give

```text
P(tau)<=9+3(B+C-1)n/D.                              (5)
```

Away from the three adjusted rows, `B<=11x/10`, `C<=11x/5`, and
`D>3x^2/10-1`. Division of the right side of `(5)` by `x^2=n^(2/3)` gives
the strict upper bound

```text
9/x^2 + (99x^2-30x)/(3x^2-10).                    (6)
```

The difference between `33` and the second term of `(6)` is

```text
30(x-11)/(3x^2-10).
```

For `x>=20` this exceeds `9/x^2`, because clearing positive denominators
reduces the claim to

```text
10x^3-119x^2+30>0,
```

which holds at `20` and has positive derivative thereafter. The three
adjusted rows satisfy the same final inequality by the exact integer-cube
checks in `verify.py`. Thus `(5)<33x^2`, proving `(PF33)`.

Finally, because `tau` is nonzero, a solution of the unpruned equation cannot
have `x=1` or `y=1`. The count on `H^2` is therefore exactly the count on
`A^2`; no endpoint was introduced by the normalization.
