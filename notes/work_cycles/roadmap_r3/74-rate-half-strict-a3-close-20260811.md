# Cycle 74: strict `A=3` branch closure (2026-08-11)

## Cycle pins

```text
our start:       0dadd61f5
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   11 PRs; no new overlap
critical open:   28
```

## Complete-fibre contradiction

On the normalization of the final strict-corner curve, write

```text
D_G=K+Z_+,       D_H=K+P_-,       p=deg P_-<=O<=1.
```

The common divisor `K` is supported exactly at the distinct grid
incidences. Its total multiplicity in excess of one per incidence is

```text
deg K-(T rho-O)=O-p<=1-p.
```

The Picard-pin identity gives

```text
3P_*+Z_+ + dE_F-P_-=pi_X^* div(A_d),       d<=1.
```

The right side is a union of complete domain fibres. If the clearing fibre
does not contain `P_*`, fibre degree forces `K=3P_*`, which already costs two
units of excess. If it does contain `P_*`, the only possible complete-fibre
coefficient forces

```text
K+P_-=3P_*.
```

This costs `2-p` units of excess, whereas the exact incidence ledger permits
only `1-p`. Both cases are impossible. The proved node is
`rate_half_ca_hankel_strict_a3_final_corner_divisor_exclusion`.

## Burn-down

```text
result:                  CLOSED every strict A=3 moving-kernel profile
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   none; A=1, crossing, and unsafe branches remain
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The rate-half target no longer needs strict `A=3` parameter sweeps or corner
geometry. The next algebraic endpoint is the residual `A=1` profile; the
independent crossing and adjacent-unsafe obligations remain live.
