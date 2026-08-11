# Cycle 108: quadratic gap-four two-simple center spread (2026-08-11)

## Cycle pins

```text
our start:       c13d02b9d
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         none
critical open:   28
```

## Squarefree `u=4` arm

The two heavy rows occur in `(e-3)/2` and `(e-9)/2` supported locator
blocks. Their incidence sets may overlap. At a slope containing
`r_gamma in {0,1,2}` heavy padded roots, zero omission and exact excess
degree give actual error weight `rho-r_gamma`.

For an affine codeword line through `h` assigned centers, column-farness
now gives

```text
h<=rho+1-sum r_gamma.
```

A fixed locator pair therefore has at least `3+r_alpha+r_beta` expanding
third blocks, between three and seven. This extends the exact joint
incidence/coding constraint to both `u=4` quadratic root patterns.

## Burn-down

```text
result:                  PINNED two-simple degrees and weighted center spread
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next constrain the overlap `Z_1 intersect Z_2` or the field-valued nearest
errors. Support degrees alone remain unlikely to close the packet.
