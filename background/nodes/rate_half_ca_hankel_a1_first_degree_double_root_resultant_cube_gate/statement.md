# `A=1` first-degree double-root resultant cube gate

- **status:** PROVED
- **closure:** exact base-field norm test for the radical cube bridge
- **consumer:** `rate_half_band_crossing_location`

Work over the prize base field `F`. Let `K_C` be the finite reduced total
quotient algebra of `C` over `F(z)`. Let

```text
Q(z;X)=q_d(z)X^d+... in F(z)[X],       q_d!=0,        (RCG1)
```

be either retained scalar double-root residual curve, and let `H(z)` be the
squarefree supported-slope locator. Define the locator numerator

```text
P_3(X)=(X-x_s)^2(X-x_d)G_L(X)       in the core-free cubic branch,
P_2(X)=(X-x_d)G_L(X)                in the core-one quadratic branch. (RCG2)
```

For `P=P_3` or `P_2`, put

```text
Xi_P(z)=Res_X(Q(z;X),P(X))
        /(q_d(z)^deg(P) H(z)^d) in F(z)^x.            (RCG3)
```

Then the corresponding double-root packet necessarily satisfies

```text
Xi_P in F(z)^(x3).                                    (RCG4)
```

More exactly, if `W` is the radical quotient from the cube bridge, then

```text
Xi_P=Norm_(K_C/F(z))(W)^3.                            (RCG5)
```

Thus `(RCG4)` is an exact branch-killing test. In characteristic different
from three, it is equivalent to every irreducible numerator/denominator
valuation being divisible by three and the remaining constant lying in
`F^(x3)`. In characteristic three, since `F` is perfect,

```text
Xi_P in F(z)^(x3)  iff  d Xi_P/dz=0.                 (RCG6)
```

## Scope

The gate is necessary, not sufficient. Passing it does not construct the
cube root on `C`, the recurrence, or a prize counterexample. The resultant
uses the actual leading coefficient `q_d`; dropping that factor changes the
cube class and invalidates the test.
