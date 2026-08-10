# Incidence-only rational-trace route fence

- **status:** PROVED
- **closure:** exact finite-field construction
- **consumer:** `rate_half_band_crossing_location`

Over `F_97`, there is an explicit strict-endpoint incidence pattern with

```text
m=2,       N=32,       rho=7,       T=9=rho+2,
sum_x(2-d_x)=1,       O=0.                              (IRF1)
```

Every supported slope has seven roots. A selected pair `(g,h)=(0,1)` has a
canonical minimum pair union `W` of size 12; every pair union has size at
least 12, and every pair intersection has size at most two. The unique
deficient point lies outside `W`. The pattern violates the closing overlap
cap used by the bounded bad-pattern campaign:

```text
max_(gamma notin {g,h}) |S_gamma intersect W|=2>1.    (IRF2)
```

Choose `W` as six inverse pairs in the order-32 subgroup. The third-root
datum is

```text
nu_x=x+x^(-1)=(x^2+1)/x.                              (IRF3)
```

Thus the rational-interpolation certificate has

```text
P(X)=X,       Q(X)=X^2+1,       deg P,deg Q<3,
```

where `3=|W|-(4m+1)`. The old deficiency-aware matrix has

```text
rank(M_W)=11<12,                                      (IRF4)
```

and its one-dimensional kernel is nonzero in every coordinate block.

The witness fails the official locator-extension condition: its coefficient
values do not extend to `X`-degree at most `rho`. Accordingly, the
strengthened matrix satisfies

```text
rank(C_W)=rank([M_W;E_W])=12.                         (IRF5)
```

## Scope

This is not a Hankel-pencil or Prize counterexample. It proves that the
`T=rho+2` incidence ledger, minimum-pair choice, bad overlap, saturation on
`W`, and the old matrix `M_W` do not alone imply full rank. Any continuation
must use the locator-extension rows or stronger outside/Hankel structure.
