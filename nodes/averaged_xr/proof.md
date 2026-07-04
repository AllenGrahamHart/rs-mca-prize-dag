# averaged_xr proof

Let `A` be the random variable counting aligned supports in the averaged XR
model. Its second moment is a sum over ordered pairs of supports. Group the
pairs by Johnson exchange distance `s`.

The number of supports at distance `s` from a fixed `j`-support is

```text
N_s = binom(j,s) binom(n-j,s).
```

For a pair in the `s`-shell, `xr_ledger_qpower` gives the exact pair
correlation: same-slope correlations gain the extra factor
`q^(-min(s,t))` until the plateau, and distinct-slope correlations are
independent beyond the `t-1` ledger reach. Equivalently the q-power saving
relative to the first-moment scale is

```text
c(s,t) = min(s,t-1).
```

Therefore the second moment is the explicit Johnson-shell sum

```text
E[A^2] = sum_s N_s * PairMass(s),
```

with `PairMass(s)` supplied in closed form by `xr_ledger_qpower`.

For `s < t`, the extra correlation is the close-pair factor
`q^(-min(s,t))`; for `s >= t`, the distinct-slope term is exactly the product
of the first moments. Thus the variance is supported by the close Johnson
shells, while the far shells contribute the independent plateau. This is the
claimed averaged-XR second-moment table.
