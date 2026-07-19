# Proof

Retain the universal equation

```text
V^3(1+qV)=1.                                         (1)
```

Write

```text
V=1+aq+bq^2+cq^3+eq^4 mod q^5.                      (2)
```

The preceding gate gives

```text
a=-1/3,       b=1/3,       c=-35/81.
```

The coefficient of `q^4` in `V^3+qV^4` is

```text
3e+6ac+3b^2+3a^2b+4c+12ab+4a^3=3e-154/81.
```

It vanishes exactly when `e=154/243`, proving `(IH4Q2)`. Substituting
`q=u z^hC_*/B` gives

```text
C_u=C_*-(u/3)z^hC_*^2/B+(u^2/3)z^(2h)C_*^3/B^2
       -(35u^3/81)z^(3h)C_*^4/B^3
       +(154u^4/243)z^(4h)C_*^5/B^4 mod z^(5h).     (3)
```

At degree `4h`, the final factor in `(3)` contributes its constant term one.
The preceding four terms contribute the coefficients in `(IH4Q1)`. The
degree bound `deg C_u<=2h-2` forces the coefficient to vanish; multiplication
by `243` proves `(IH4Q3)`.

The monic quadratic gate gives

```text
u^2=du-3k,
u^3=(d^2-3k)u-3dk,
u^4=(d^3-6dk)u-3kd^2+9k^2.                          (4)
```

Substitute `(4)` into `(IH4Q3)`. The coefficient of `u` is `C`, and the
constant coefficient is `D`, exactly as printed in `(IH4Q4)`. This proves
`(IH4Q5)` and the alternatives in `(IH4Q6)`. All earlier certifier conditions
remain necessary and sufficient after a scalar is selected. QED.
