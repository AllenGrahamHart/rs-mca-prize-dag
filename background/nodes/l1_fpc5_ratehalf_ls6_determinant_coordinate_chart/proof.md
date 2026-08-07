# Proof: LS6 determinant coordinate chart

## 1. The forward map

For any `D` in `A`, the pair-determinant theorem gives

```text
H_D=D_0Q-DQ_0=(DV_0-D_0V)/M,       deg H_D<=h.
```

If `H_D=H_G`, then

```text
D_0(Q_D-Q_G)=Q_0(D-G).
```

Since `gcd(D_0,Q_0)=1`, `D_0` divides `D-G`. Both locators are monic of
degree `j`, so `deg(D-G)<j=deg D_0`; hence `D=G`, and then `Q_D=Q_G`.
Thus `(DC1)` is injective.

## 2. Explicit inverse

Fix any `H` with `deg H<=h`. Since `Q_0` is invertible modulo `D_0`, define
`R_H,D_H` as in `(DC2)`. Then `deg R_H<j`, so `D_H` is monic of degree `j`,
and

```text
H+D_HQ_0==0 mod D_0.
```

Therefore `Q_H` is a polynomial. Its degree and leading coefficient equal
those of `Q_0`, because the lower-degree term `H` cannot alter the leading
term of `D_HQ_0`.

The base equation gives `V_0==-MQ_0 mod D_0`, while
`D_H==-H Q_0^(-1) mod D_0`. Consequently

```text
D_HV_0-MH==0 mod D_0,
```

so `V_H` is also a polynomial. Its numerator has degree at most

```text
max(j+s,2ell+h)=3ell-2a,
```

and division by the degree-`j=2ell-a` polynomial `D_0` gives
`deg V_H<=ell-a=s`.

Finally, multiply `D_HE-MQ_H` by `D_0` and use
`D_0E=MQ_0+V_0` and `D_0Q_H=H+D_HQ_0`. The result is

```text
D_0(D_HE-MQ_H)=D_HV_0-MH=D_0V_H.
```

Hence `D_HE=MQ_H+V_H`; the constructed `D_H` belongs to `A` and maps back
to `H`. This proves bijectivity without a dimension argument.

## 3. Collective determinants

For coordinates `H,G`, expand their definitions:

```text
D_HG-D_GH
 =D_H(D_0Q_G-D_GQ_0)-D_G(D_0Q_H-D_HQ_0)
 =D_0(D_HQ_G-D_GQ_H).
```

The pair theorem bounds the quotient degree by `h`, proving `(DC3)`. Since
every `H` of degree at most `h` occurs, formal determinant identities do not
cut down `A`.

## 4. Root-local primitive guard

At a root `x` of `D_0`, primitivity of the base gives `Q_0(x)!=0`, and

```text
H(x)=-D_H(x)Q_0(x).
```

This proves `(DC5)`. If `x` is a root of `D_H` but not of `D_0`, then
`H(x)=D_0(x)Q_H(x)`, so `Q_H(x)!=0` is equivalent to `H(x)!=0`.

If `x` is a common root, differentiate
`H=D_0Q_H-D_HQ_0`. The locators are squarefree, so `D_0'(x)!=0`, and

```text
H'(x)=D_0'(x)Q_H(x)-D_H'(x)Q_0(x).
```

Thus `Q_H(x)!=0` is equivalent to the second inequality in `(DC4)`.
Checking all roots of the split squarefree `D_H` is exactly
`gcd(D_H,Q_H)=1`. QED.
