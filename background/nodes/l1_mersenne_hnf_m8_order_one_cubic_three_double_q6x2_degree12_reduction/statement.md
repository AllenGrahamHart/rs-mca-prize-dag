# L1 Mersenne HNF m=8 order-one cubic three-double q=-6x^2 degree-12 reduction

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_double_linear_remainder_reduction`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the exceptional `q=-6x^2` branch of the h=7 cubic `2+2+2` profile

Put `y=x^2` and define

```text
A=11d^2+27d+27,
B=d^4+4d^3+7d^2+6d+3,
s=d^2+3d+3,
u=d^2+2d+2,
D=5d^4+21d^3+37d^2+32d+15.                       (QDR1)
```

The residual conic becomes

```text
C_y=105y^2-7Ay+10B=0.                              (QDR2)
```

Modulo (QDR2), the reduced fifth equation factors as

```text
(d+6y)(5x(s-y)+2(d+2)u)=0.                         (QDR3)
```

The first factor is impossible because `q=-6y` and `d+6y=0` would give
`q=d`, while `q-d=d(r-1)` is saturated. Hence every survivor satisfies

```text
Q_y=25y(s-y)^2-4(d+2)^2u^2=0.                      (QDR4)
```

Define

```text
E=14(2d^2+9d+9)^2-75B,
F=5B(19d^2+63d+63)-126(d+2)^2u^2.                  (QDR5)
```

The exact remainder is

```text
rem_(C_y)(Q_y)=2(Ey+F)/63.                         (QDR6)
```

Consequently every survivor has

```text
R_12(d)=105F^2+7AFE+10BE^2=0.                      (QDR7)
```

The polynomial `R_12` has degree exactly 12 and leading coefficient
`149868`. Thus 32 degree-12 norm gcds

```text
gcd(R_12(X),X^(p+1)-zeta)                           (QDR8)
```

cover all four official rows and eight norm colors. Unit gcds close this
complete exceptional branch. No gcd verdict or converse lift from a root of
`R_12` is claimed here.
