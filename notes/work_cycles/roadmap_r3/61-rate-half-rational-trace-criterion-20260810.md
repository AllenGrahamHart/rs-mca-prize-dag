# Cycle 61: rate-half rational trace criterion (2026-08-10)

## Pivot-free equivalence

Put `s=4m+1`, `n=|W|`, and `r=n-s`. For scalar data `h:W->F`, the two-block
matrix with columns

```text
(x^i)_(0<=i<s)  and  (h(x)x^i)_(0<=i<s)
```

has full column rank exactly when there are no polynomials `0!=P,Q` with
`deg P,deg Q<r` and `Q(x)=h(x)P(x)` on `W`. If the unique clean-endpoint
deficient point belongs to `W`, its lower clone punctures that one agreement
condition. This follows from the exact dual Reed-Solomon kernel
`lambda_x=P(x)/sigma'_W(x)`.

For the official coefficient one below the top,

```text
h_m(x)=-(mu_x+sum_(gamma in A_x)gamma).
```

At `m=2` this differs by a constant from the third incidence root `nu_x`.
The remaining scalar theorem is therefore explicit: the official trace data
must avoid a numerator/denominator of degree below the residual width.

## Bounded falsification evidence

A 16-worker, 30-second-per-worker Modal profile over `F_97` covered `125,335`
bad canonical pair unions from `58,644` regular incidence systems. It found
`105,574` saturated and `19,761` one-deficient cases. Every complete matrix
had full rank, and each of the `j=1` and `j=2` coefficient blocks independently
had full residual rank in every case. The `j=0` block failed in `23,327`
saturated and `4,326` deficient cases, exactly exposing the zero-root scalar
factor and showing why the top trace coefficient is the robust choice.

This is falsification evidence at one small field, not an official-scale
proof. The proved leaf
`rate_half_bivariate_single_coefficient_rational_interpolation_criterion`
isolates the exact theorem still needed; no critical status changes.
