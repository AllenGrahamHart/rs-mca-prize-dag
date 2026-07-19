# Proof

The preceding certifier gives

```text
H=C_u^3(1+u z^h C_u/B),       H=C_*^3.              (1)
```

Set `C_u=C_*V` and `q=u z^hC_*/B`. Cancelling `C_*^3` in `(1)` gives

```text
V^3(1+qV)=1.                                        (2)
```

Its derivative with respect to `V` at `(q,V)=(0,1)` is three, so it has a
unique normalized formal solution. Write

```text
V=1+a q+b q^2 mod q^3.                              (3)
```

The coefficients of `q` and `q^2` in `(2)` are

```text
3a+1,       3b+3a^2+4a.
```

They vanish exactly for `a=-1/3,b=1/3`, proving `(IHQ3)`. Substitution of
`q` from `(IHQ2)` proves `(IHQ4)` because `ord_0 q=h`.

The coefficient at `z^(2h-1)` in `(IHQ4)` is

```text
kappa-(u/3)Delta,
```

recovering the first equation `(IHQ5)`. At `z^(2h)`, the three terms in
`(IHQ4)` contribute

```text
kappa_1,       -(u/3)Delta_1,       u^2/3,
```

respectively; the last constant is one because `C_*(0)=B(0)=1`. The degree
bound `deg C_u<=2h-2` forces this coefficient to vanish, proving the monic
quadratic in `(IHQ5)`.

If `Delta!=0`, the linear gate fixes the only possible scalar and the
quadratic is an additional rejection test. If `Delta=0,kappa!=0`, the linear
gate is impossible. If both vanish, the monic quadratic has at most two
roots in the base field and cannot vanish identically. These are exactly the
alternatives `(IHQ6)`. All remaining certifier conditions are inherited
unchanged from `(IHC9)`. QED.
