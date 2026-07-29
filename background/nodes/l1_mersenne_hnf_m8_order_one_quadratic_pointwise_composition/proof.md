# Proof - L1 Mersenne HNF m=8 order-one quadratic pointwise composition

For every reduced root `x` put

```text
epsilon=E(x)=x^(p+1).
```

Since `epsilon in mu_8` and `p=-1 mod 8`, taking Frobenius and substituting
`x^p=epsilon/x` gives

```text
A^p epsilon^3+B^p x epsilon^2+C^p x^2 epsilon-x^2=0. (1)
```

Therefore all six roots of `L` vanish on

```text
J(W)=A^p E(W)^3+B^p W E(W)^2+C^p W^2 E(W)-W^2.      (2)
```

The polynomial `J` has degree six and leading coefficient `A^p A^3`.
The reduced polynomial `L` is monic, degree six, and squarefree. Hence
`L` divides `J`, and degree and leader comparison prove (QPC2).

Write

```text
L(W)=W^6+l_1W^5+...+l_5W+l_6.
```

The HNF coefficient formulas give

```text
l_1=6/d,
l_5/l_6=-6d/(r-1),
l_6=d^(-6)g(1).                                     (3)
```

The exceptional value `r=1` is already impossible in the first derivative
identity `(r-1)g'(1)/g(1)=r-7`, so the displayed denominator is safe.

Put

```text
T=3B+B^p/A^p.                                       (4)
```

The `W^5`, constant, and `W` coefficients in (QPC2) are respectively

```text
T/A=l_1,
(C/A)^3=l_6,
T/C=l_5/l_6.                                        (5)
```

The first equation and `d!=0` show `T!=0`. Dividing the first and third
equations in (5), then using (3), gives

```text
C/A=-(r-1)/d^2=(1-r)/d^2,
```

which is (QPC3). The constant equation in (5) and the last equation in (3)
now give

```text
d^(-6)g(1)=(1-r)^3/d^6.
```

This is (QPC4). QED.
