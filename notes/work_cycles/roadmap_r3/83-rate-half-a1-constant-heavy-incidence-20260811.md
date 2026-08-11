# Cycle 83: `A=1` constant heavy-incidence pin (2026-08-11)

## Cycle pins

```text
our start:       9ea483897
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   38 PRs; no new overlap
critical open:   28
```

## Heavy incidence charge

For a parameter-constant residual, cancelling the heavy split factor makes
every supported incidence on a removed row a zero of the Forney numerator.
The specialized factorization then places it in the excess recurrence
factor. Hence

```text
I_H<=sum c_gamma<=Delta.
```

The light rows are saturated, and exact incidence balance gives

```text
s=0: I_H+O=(6-a)e-3,       Delta=2e-1;
s=1: I_H+O=(3-a)e-6,       Delta=e-2.
```

This sharpens the two constant residual ranges to

```text
s=0: a in {2,3,4,5};
s=1: a in {1,2}.
```

At the smallest values, the independent deficits from the two upper bounds
sum to one and two. The proved leaf is
`rate_half_ca_hankel_a1_first_degree_constant_heavy_incidence_pin`.

## Audit correction

Cancelling the heavy factor changes the pole divisor by exposing supported
points on the removed domain rows. No step identifies that divisor with the
original pole divisor. A stronger contact-divisor shortcut based on that
identification was rejected before DAG registration.

## Burn-down

```text
result:                  NARROWED constant residual degrees to 2..5 / 1..2
DAG delta:               +1 PROVED leaf, +3 req edges, +1 ev edge
critical status delta:   none
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next classify the core-one degree-one/two constant residuals and the
core-free degree-two near-saturated gap allocations.
