# Proof

The preceding theorem reduced the Hensel equation to

```text
V^3(1+qV)=1.                                        (1)
```

Write

```text
V=1-q/3+q^2/3+cq^3 mod q^4.                        (2)
```

The coefficient of `q^3` in `V^3+qV^4` is

```text
3c+6(-1/3)(1/3)+(-1/3)^3+4(1/3)+6(-1/3)^2
 =3c+35/27.
```

Thus `c=-35/81`, proving `(IHCQ2)`. Substituting
`q=u z^hC_*/B` gives

```text
C_u=C_*-(u/3)z^hC_*^2/B+(u^2/3)z^(2h)C_*^3/B^2
          -(35u^3/81)z^(3h)C_*^4/B^3 mod z^(4h).   (3)
```

At degree `3h`, the last factor in `(3)` contributes its constant term one.
The other three contributions are exactly the coefficients in `(IHCQ1)`.
Because `deg C_u<=2h-2`, multiplying the resulting equation by `81` proves
`(IHCQ3)`.

The quadratic gate says

```text
u^2=Delta_1u-3kappa_1.                              (4)
```

Multiplying by `u` and applying `(4)` again gives

```text
u^3=(Delta_1^2-3kappa_1)u-3Delta_1kappa_1.          (5)
```

Substitute `(4)--(5)` into `(IHCQ3)`. Its coefficient of `u` is `A` and its
constant coefficient is `B` from `(IHCQ4)`, proving `(IHCQ5)`. The three
alternatives `(IHCQ6)` are immediate in a field. All earlier certifier gates
remain necessary and sufficient after a scalar is selected. QED.
