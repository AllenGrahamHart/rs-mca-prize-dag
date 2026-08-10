# Cycle 57: rate-half bivariate row-surplus fence (2026-08-10)

## Exact control

The deficiency-aware matrix route was tested on the smallest genuine failing
pencil, the proved `m=1`, `q=17` five-slope Hankel witness. Its five root
triples partition the domain except for the unique deficient point `14`.
That point lies outside every one of the ten canonical pair unions.

For each pair union, the scalar-column model is therefore exact and gives

```text
M_W: 15 x 6,       rank(M_W)=5,       nullity(M_W)=1.
```

The upper rank bound is certified by the explicit all-nonzero quotient vector
`(4x^2+12x)_(x in W)`. The lower bound is certified by a nonzero `5 x 5`
minor for every pair. Primary Gaussian-elimination replay and an independent
Cramer-rule/minor replay both pass.

## Route consequence

`rate_half_bivariate_row_surplus_route_fence` is added as a proved leaf. It
shows that raw overdetermination is not enough: even `15` equations in `6`
fully saturated scalar columns can have the exact one-dimensional kernel
needed by a real Hankel failure.

The route is not dead at official scale. Its next theorem must exploit a
structure absent from the rank-one separated `m=1` family, such as a banked
`m>1` component/separation exclusion, or prove rank only on the bad
intersection patterns. No critical status changes.
