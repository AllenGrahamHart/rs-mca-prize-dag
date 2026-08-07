# Proof

Write the monic polynomial of `S` as

```text
P_S(Y)=Y^5-e_1Y^4+e_2Y^3-e_3Y^2+e_4Y-1.              (1)
```

For `A(Y)=Y^2+c_1Y+c_0`, direct expansion gives

```text
Y A(Y)^2-(bY+1)^2
=Y^5+2c_1Y^4+(c_1^2+2c_0)Y^3
 +(2c_0c_1-b^2)Y^2+(c_0^2-2b)Y-1.                   (2)
```

Since `2` is invertible, matching the first two nonleading coefficients in
`(1)--(2)` forces

```text
c_1=-e_1/2,       c_0=(4e_2-e_1^2)/8=d/8.            (3)
```

The linear coefficient then forces

```text
b=(c_0^2-e_4)/2.                                     (4)
```

The remaining quadratic coefficient agrees exactly when

```text
b^2=e_3-e_1c_0.                                      (5)
```

Substitute `(3)--(4)` into `(5)` and multiply by `4096`. The result is
precisely `Psi(S)=0`. This proves the equivalence and uniqueness in
`(SH1)--(SH2)` over every odd field.

The proved odd next-boundary divisor descent identifies `(SH2)` with the
squares of normalized reduced weight-five relations. Its converse is valid
because `P_S` is squarefree: a common zero of `A(y)` and `by+1` would also be
a repeated zero of `Y A(Y)^2-(bY+1)^2`. This proves the first equivalence.

For `(SH3)`, expand the product of the 16 linear forms with sign product one.
After substituting `y_i=x_i^2` and reducing by `x_1x_2x_3x_4x_5-1`, its
integer coefficients agree term by term with `(SH1)`. The verifier performs
this sparse-polynomial calculation independently. Conceptually, each factor
chooses exactly one product-one lift of `S`; its vanishing is exactly the
first-moment relation already characterized above.

It remains to count the quotient in `(SH4)`. Identify `U` with `Z/256`.
The product-one condition is that the five exponents sum to zero modulo
`256`. For an odd multiplier `a`, decompose its permutation of `Z/256` into
cycles `C`. A fixed five-subset is a union of cycles, and its size and exponent
sum are recorded by

```text
product_C (1+z^|C| u^(sum C))  in Z[z,u]/(z^6,u^256-1). (6)
```

The coefficient of `z^5u^0` is its fixed-set count. Summing that coefficient
over the 128 odd multipliers gives `36,997,504`; Burnside division gives
`36,997,504/128=289,043`. For the identity multiplier, `(6)` gives
`34,412,301` normalized subsets. The verifier recomputes every cycle and
coefficient from the definitions. QED.
