# Proof

Let `E_d` be the Euler operator

```text
E_d(F)=dF-YF'.                                         (1)
```

On `Y^m` with `0<=m<d`, it acts by the nonzero scalar `d-m`. Therefore
`(ESR1)` is well-defined and gives

```text
E_d(S_Phi)=Phi+d.                                      (2)
```

Since `E_d(H)=-d`, the monic degree-`d` polynomial

```text
A_Phi=H+S_Phi                                         (3)
```

is the unique monic degree-`d` solution of

```text
E_d(A_Phi)=Phi.                                        (4)
```

Uniqueness follows because the kernel of `E_d` on polynomials of degree at
most `d` is the line spanned by `Y^d`, and monicity fixes its coefficient.

Suppose first that a pure norm packet `(ESR3)` exists. Put

```text
A=DU^4,       B=e_4DV^4.                              (5)
```

Then `A+B=H` and `E_d(A)=Phi`, so uniqueness in `(4)` gives

```text
A=H+S_Phi,       B=-S_Phi.                            (6)
```

Moreover,

```text
gcd(S_Phi,H)=gcd(-B,A+B)=gcd(A,B)=D,                  (7)
```

because `gcd(U,V)=1` and `D` is monic. Dividing `(6)` by `(7)` proves all
three tests in `(ESR4)`.

Conversely, assume `(ESR4)`. The definition of `D_Phi` makes both quotients
exact. Substituting them into `H=(H+S_Phi)-S_Phi` gives

```text
H=D_Phi(U^4+e_4V^4).                                  (8)
```

The full-gcd definition also gives

```text
gcd(U^4,V^4)=1,
```

hence `gcd(U,V)=1`. Since `H` is squarefree in the stated characteristic,
its divisor `D_Phi` is squarefree. The degree statements follow directly:
`S_Phi` has degree `N` because `phi_N!=0`, so the two quotients have degrees
`d-4=4r` and `N-4=4r-4`. Their fourth roots consequently have degrees `r`
and `r-1`. This reconstructs `(ESR3)`.

The monic gcd is unique. A monic fourth root of a monic polynomial is unique,
so `U` is unique. On the second side, `e_4` is the leading coefficient of
`-S_Phi/D_Phi`; division by it leaves a monic fourth power with unique monic
root `V`. This proves normalized uniqueness.

If `(ESR5)` holds, write the four distinct roots of `X^4+e_4` as `c_i`.
Then

```text
U^4+e_4V^4=product_i(U+c_iV).                         (9)
```

Two factors in `(9)` cannot share a root: subtracting them would force
`V=0`, and then either factor would force `U=0`, contrary to coprimality.
Thus `(ESR5)` reconstructs the centered split norm pencil. The harmonic
deleted-root matching is independent extra data, exactly as stated.

Finally, `(4)` and `(ESR4)` give

```text
Phi=E_d(D_Phi U^4)=U^3[dD_Phi U-Y(D_Phi'U+4D_Phi U')]
    =TU^3.                                            (10)
```

Likewise `(2)` and `-S_Phi=e_4D_Phi V^4` give

```text
Phi+d=dS_Phi-YS_Phi'
     =Y(-S_Phi)'-d(-S_Phi)
     =e_4V^3[4YD_Phi V'+V(YD_Phi'-dD_Phi)]
     =e_4V^3C.                                        (11)
```

This proves `(ESR6)` and completes both directions. QED.
