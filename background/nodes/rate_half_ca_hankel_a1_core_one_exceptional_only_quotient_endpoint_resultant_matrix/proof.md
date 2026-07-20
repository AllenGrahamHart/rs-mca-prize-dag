# Proof

The endpoint resultant-profile theorem gives the two entries in the `Q`
column. In the flat profile they are

```text
Res(A,Q)=kappa_A z^(2e)P_ord^alpha,
Res(H,Q)=kappa_H P_ord^beta.                           (1)
```

The exponent identities

```text
alpha+beta=2e+1=r                                    (2)
```

and resultant multiplicativity recover the known full `Q` resultant.

Now evaluate the factor-descent identity

```text
QV+P_XW=P
```

at every root of `A` and of `H`. Resultant multiplication gives

```text
Res(A,Q)Res(A,V)=P^(deg A)=P^(2e),
Res(H,Q)Res(H,V)=P^(deg H)=P^(6e+6),                  (3)
```

up to nonzero convention scalars. Divide `(3)` by `(1)`. Since

```text
2e-alpha=gamma,       6e+6-beta=delta,                (4)
```

the two `V` entries in `(QRM3)` follow. Their product has exponents

```text
gamma+delta=6e+5,                                    (5)
```

and all `z^(6e+6)` lies in the `H,V` entry. This is exactly the full `V`
resultant from two-sided saturation, proving every identity in `(QRM5)`.

In the swapped profile, the endpoint theorem multiplies the `A,Q` entry by
`L` and the `H,Q` entry by `L^(-1)`. Each row product in `(3)` is a pure
power of `P` and contains no such deviation. Therefore the corresponding
`V` entry has the inverse factor in each row. This gives the checkerboard in
`(QRM4)`. The denominator factors cancel against `P_ord`, as already proved
for the two `Q` entries and then forced by `(3)` for the two `V` entries.
QED.
