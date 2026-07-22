# Proof - L1 decorated shift-pair gcd descent and sharpness

## 1. Gcd descent

Since `D` divides both cofactors in `(GD1)`, it divides their linear
combination `R`. Dividing by the monic `D` gives `(GD2)--(GD3)`, including
the degree bounds. Maximality of the gcd gives `gcd(q_1,q_2)=1`.

The cross-coprimality in `(GD1)` makes every factor of `D` coprime to `BN`
and to `AN`; hence it is coprime to `A`, `B`, and `N`, proving `(GD4)`. Since
the domain locator factors as `GABN`, any domain root of `D` must therefore
lie in `G`.

The reduced parameters are `(GD5)`. The primitive uniqueness condition
`e'<=w'` is

```text
e-c<=w+c,
```

which is `(GD6)`. Finally, `D|R` and `R!=0` give
`c<=deg R<=d-w-1`.

## 2. The explicit family

Direct multiplication of the polynomials in `(GD7)` by the displayed `A,B`
gives `(GD8)`. Their difference is

```text
Q_(2,t)-Q_(1,t)=Z+4t+5.
```

At its only possible common root `Z=-4t-5`, one has

```text
Q_(1,t)(-4t-5)=2 mod 13.
```

Thus the two quadratics are coprime for every `t`, proving `(GD9)`.

At `t=4`, the residual in `(GD8)` is zero and the two cofactors become `B`
and `A`, so this is not a distinct cross-coprime shell pair. At `t=0`,
`Q_(1,t)` vanishes at the `N` root zero; at `t=12`, `Q_(2,t)` does. For every
other `t`, the two cofactors are nonzero on the opposite tail and on `N`.

Equation `(GD8)` now gives

```text
U_t-P_(1,t)=GAQ_(1,t),
U_t-P_(2,t)=GBQ_(2,t).
```

The cross-coprimality just checked makes the two displayed agreement sets
exact. Their sizes are `a=3`, while `k=2`, `w=1`, and both cofactors have
degree `e=2`. There are `13-3=10` valid parameters, proving sharpness.
