# Cycle 104: core-one marked source frame (2026-08-11)

## Cycle pins

```text
our start:       dbf5ffe92
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         none
critical open:   28
```

## Source-side determinant target

The symmetric minimal-vector coefficient chain makes the `e+1` kernel
coefficients a common totally isotropic plane for both endpoint Hankel
forms. In contracted source coordinates this gives two exact rank-one frame
cancellations. Cauchy--Binet then turns the marked determinant into

```text
sum_(|J|=d) Vand(x_*,J)^2 product_(x in J)mu_x
 =c^2D_1g_*^2S_B^6.
```

This is the first exact source-weight formula for the retained quadratic
double-root packet. It isolates cancellation as the remaining issue; no
positivity or termwise noncancellation has been assumed.

## Burn-down

```text
result:                  EXPOSED coefficient frame and source subset sum
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next determine whether the actual RS antiweights force a noncancellation,
valuation, or characteristic-three obstruction at either quadratic root of
`S_B`. A generic finite-field subset sum is not enough.
