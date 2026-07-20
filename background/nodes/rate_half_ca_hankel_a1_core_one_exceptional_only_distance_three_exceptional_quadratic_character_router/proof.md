# Proof

Use the matching-free boundary values

```text
K_A(a)=P_X'(a)/(B(a)^4A'(a)^4),       Y_a=K_A(a)^e. (1)
```

A boundary-compatible matching pairs the `2e` values `Y_a` as `y,-y`.
There are `e` pairs, and the official `e=2^38-1` is odd. Therefore

```text
product_(a in R_A)Y_a
 =(-1)^e product_(pairs)y^2
 =-product_(pairs)y^2.                               (2)
```

Thus `-product_a Y_a` is a square. Since `Y_a=K_A(a)^e` and `e` is odd,
raising to `e` does not change a quadratic character. Hence

```text
-product_(a in R_A)K_A(a) in (F_p^*)^2.             (3)
```

The denominator in `(1)`, multiplied over `a`, is a fourth power. It has no
effect on `(3)`, so `(3)` is equivalent to

```text
-product_(a in R_A)P_X'(a) in (F_p^*)^2.            (4)
```

On the smooth multiplicative domain of size `N=8e+8`, the boundary
derivative identity is

```text
P_X'(a)=N a^(-1)/((a-s)(a-x_0)).                    (5)
```

The degree of `A` is `2e`, which is even. Since `A` is monic,

```text
product_a a=A(0),
product_a(a-s)=A(s),
product_a(a-x_0)=A(x_0).                            (6)
```

Multiplying `(5)` and using `(6)` gives

```text
product_a P_X'(a)=N^(2e)/(A(0)A(s)A(x_0)).          (7)
```

The numerator is a square. Consequently `(4)` says that
`-1/(A(0)A(s)A(x_0))` is a square. Multiplication by the square
`(A(0)A(s)A(x_0))^2` gives exactly `(EQR1)`. Euler's criterion over the
prime field gives `(EQR2)`. QED.
