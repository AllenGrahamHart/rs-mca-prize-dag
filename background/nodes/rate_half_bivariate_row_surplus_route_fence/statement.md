# Bivariate row-surplus route fence

- **status:** PROVED
- **closure:** exact finite-field rank certificate
- **consumer:** `rate_half_band_crossing_location`

Apply the deficiency-aware matrix reduction to the proved strict `m=1`
witness over `F_17`:

```text
N=16,       rho=3,       T=5,
Q(Y;X)=X^3+(9+4Y)X^2+12YX+7.                         (BRS1)
```

Its five supported root triples partition `F_17^* \ {14}`. For every one of
the ten canonical supports `W=S_g union S_h`:

```text
|W|=6,
the unique deficient point 14 lies outside W,
M_W has shape 15 x 6,
rank_(F_17)(M_W)=5,
nullity_(F_17)(M_W)=1.                                (BRS2)
```

Thus every coordinate of `W` is saturated and the scalar-column model is
exact, yet the matrix is not full rank despite having `5/2` times as many
rows as columns.

## Scope

This is a route fence, not an official counterexample. It proves that raw
row surplus, saturation of every coordinate in `W`, and the published
bivariate product shape do not by themselves imply full column rank
uniformly in `m`. An official proof may still exploit structure that excludes
the rank-one separated `m=1` family or emerges only for `m>1`.
