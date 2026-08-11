# Cycle 110: quadratic gap-four regular quartic pin (2026-08-11)

## Cycle pins

```text
our start:       6e2c2a164
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         none
critical open:   28
```

## Quartic regular residual

The core-one regular determinant has degree `e-2`. Exact `u=4` rank losses
consume `e-6` degrees, leaving one quartic:

```text
double root: D_1=a g_*E_4;
two simple:  D_1=a G_1G_2E_4.
```

The marked determinants consequently become

```text
double: tau ac^2 E_4g_*^3S_B^6;
simple 1: tau ac_1^2E_4G_1^5G_2S_1^6;
simple 2: tau ac_2^2E_4G_1G_2^5S_2^6.
```

The quartic may be nonreduced and may share roots with the displayed
factors. It is not identified with any correction divisor.

## Burn-down

```text
result:                  REDUCED unallocated regular divisor to degree four
DAG delta:               +1 PROVED leaf, +3 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next classify `E_4` through the coefficient chain or prove a relation with
the total degree-four correction divisor. Do not assume that relation.
