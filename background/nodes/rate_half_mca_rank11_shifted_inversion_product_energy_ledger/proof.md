# Proof

For `x in H` with `x!=-tau`, the shifted involution

```text
phi(x)=kappa/(x+tau)-tau
```

lies in `H` exactly when `(x,phi(x))` is counted by `R`. Its fixed points are
exactly the solutions counted by `F`. Every other point belongs to a
two-cycle, proving the interpretation of `I` and its evenness.

There are `N-z_tau` choices of `x in H` for which `x+tau` is nonzero, and
the same number of choices for `y`. Every ordered pair determines one unique
nonzero product `kappa`. Summing over `kappa` gives the first identity in
`(PE1)`. Every eligible `x` determines the unique nonzero square
`kappa=(x+tau)^2`, giving the second. Subtraction gives the third.

The number `R(tau,kappa)` is the multiplicative representation function of
`kappa` by the set `A_tau`. Squaring it and summing over nonzero `kappa`
counts quadruples in `A_tau^4` with equal products, which is `(PE2)`.

For `h in H`, the bijection `(x,y)=(hX,hY)` changes

```text
(x+h*tau)(y+h*tau)=h^2(X+tau)(Y+tau).
```

It preserves equality of the two coordinates, proving all of `(PE3)`.

Finally set `u=x^(-1),v=y^(-1)`, a bijection of `H^2`. Expanding the product
equation and multiplying by `uv` gives

```text
1+tau(u+v)+(tau^2-kappa)uv=0.                         (1)
```

If `A=tau^2-kappa!=0`, divide `(1)` by `A` and complete the product:

```text
(u+tau/A)(v+tau/A)=kappa/A^2.
```

Inversion preserves the diagonal, so both `R` and `F` obey `(PE4)`. If
`A=0`, equation `(1)` is `u+v=-1/tau`, proving `(PE5)`. QED.
