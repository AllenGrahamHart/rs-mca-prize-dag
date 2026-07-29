# Proof - L1 Mersenne HNF m=8 order-one cubic three-double linear remainder reduction

Scale the factor variables from the dependency by `d`. The monic sextic in
the variable `Z=dW` is

```text
prod_i (Z^2+x_iZ+x_i^2-ax_i+c),                     (1)
```

where the elementary symmetric functions of the three `x_i` are
`6,b,t`. The triangular equations (TSC2) become

```text
c=(b+k)/3,
t=t_1b+t_0.                                         (2)
```

The scaled HNF coefficients are

```text
L_2=15+q/2,
L_3=20+q(d+8)/3,
L_4=15+q(d^2+7d+23)/4+q^2/8,
L_5=-6dG/(q-d),
L_6=G.                                               (3)
```

Substitute (2) in (TSC4) and subtract the printed `L_4`. Direct collection
in `b` gives

```text
b^2/3+Hb+K=0,                                       (4)
```

which is equivalent to (TLR3).

For the fifth coefficient, (TSC5) first simplifies to

```text
L_5=t(3a^2-12a+b-3c)+2cb(3-a)+6c^2.                (5)
```

The coefficient multiplying `t` loses its `b` term because `3c=b+k`.
Before reduction by (4), (5) is

```text
2(1-x)b^2/3+(2-x)(3x^2+4x-8-q/6)b
 +t_0(3x^2-6-q/2)+2k^2/3.                          (6)
```

Use `b^2=-3Hb-3K`. The resulting coefficient of `b` factors as

```text
(2-x)(3x^2+4x-8-q/6)-2(1-x)H
 =-x(x^2+q/6)=A_5,                                 (7)
```

and the constant term expands to `B_5` in (TLR4). Combining the reduced
identity with `L_5=-6dG/(q-d)` proves (TLR5). The inherited saturation
`r-1!=0` and `d!=0` is exactly `q-d!=0`, so the slope vanishes only on the
two loci (TLR9).

For completeness, collect (TSC6) before reducing. With the abbreviations in
(TLR6), it is exactly

```text
L_6=C_3b^3+C_2b^2+C_1b+C_0.                        (8)
```

The quadratic relation (TLR3) gives

```text
b^2=-3Hb-3K,
b^3=(9H^2-3K)b+9HK.                                (9)
```

Substitution of (9) in (8), followed by `L_6=G`, is precisely
`A_6b+B_6=0`, proving (TLR7). Scaling the residual conic by `q=dr` gives
(TLR8). All divisions used are by `2`, `3`, `5`, or the inherited nonzero
quantities `d` and `q-d`; none vanishes in an official characteristic or
on the saturated chamber. QED.
