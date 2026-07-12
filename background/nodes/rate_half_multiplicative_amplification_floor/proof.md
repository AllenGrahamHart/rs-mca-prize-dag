# Proof

Write

```text
sigma* = 2^33 + 2,978,146.
```

First take `e<=33` and set `r=2^(33-e)`.  Then `N_e=256r`, while the strict
inequality `sigma*>2^33` gives `d_e>=r+1`.  The elementary entropy bound
`C(N,m)<=2^N` therefore gives

```text
F_e <= 2^(N_e-256(d_e-1)) <= 2^(256r-256r) = 1.
```

Now take `e>=34`.  Since `0<sigma*<2^34<=c`, one has `d_e=1`, so

```text
F_e = C(N_e,N_e/2+1),     N_e<=128.
```

This binomial is nondecreasing when the dyadic value `N` is doubled.  Indeed,
map an `(N/2+1)`-subset of an `N`-set to a `(N+1)`-subset of a disjoint
`2N`-set by adjoining one fixed set of `N/2` new elements.  Hence the maximum
over `e>=34` occurs at `e=34`, where `N_e=128`, and equals `C(128,65)`.
This is greater than `1`, proving the asserted global maximum.

If a construction changes no term except to multiply `F_e` by `L`, crossing
the strict trigger requires `L F_e>2^216`.  The largest available `F_e` gives
the weakest necessary condition, and integer rounding yields exactly

```text
L >= floor(2^216/C(128,65)) + 1.
```

The conclusion is deliberately scoped to multiplicative amplification; it
makes no assertion about mechanisms that alter the floor itself.
