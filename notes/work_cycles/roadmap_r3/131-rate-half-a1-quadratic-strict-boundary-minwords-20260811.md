# Cycle 131: rate-half quadratic strict-boundary minimum words (2026-08-11)

## Cycle pins

```text
starting source:  1c967ff948037490f8e7903aa45d168e63ad843f
canonical prize:  3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:    93fba1be3f3299b0ba4708d88715377bbb656e45
compute:          exact integer replay only
critical open:    28
```

## First strict boundary

Retain the strict pair branch at `|S_alpha union S_beta|=rho+p=3p`.
Cycle 127 makes the endpoint codeword line contain exactly two centers.
The noncore endpoint-missing classes are disjoint, have sizes
`p+r_alpha,p+r_beta`, and leave `p-1-r_A` coordinates present at both
endpoints.

Across the `3e+1` off-line slopes, exact incidence gives

```text
sum a_delta=p,
a_delta=|U union S_delta|-(2rho+1)>=0.
```

Thus at least `p+2` off-line center differences are exact nonzero RS
minimum words. Removing every positive-deficit slope adversarially leaves
at least `(e+15)/2+r_A` clean minimum words. At the official integers these
lower bounds are `274877906946` and `91625968989+r_A`.

## Burn-down

```text
result:                  PROVED strict-boundary minimum-word reduction
DAG delta:               +1 PROVED
critical status delta:   none
terminal delta:          strict branch now has a macroscopic exact family
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next pass this exact family through the fixed-line Hankel source and dual
GRS interpolation, keeping the two-center degree shift explicit.
