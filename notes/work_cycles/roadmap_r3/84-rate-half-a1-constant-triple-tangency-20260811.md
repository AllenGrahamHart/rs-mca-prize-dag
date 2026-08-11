# Cycle 84: `A=1` constant-residual triple-tangency packets (2026-08-11)

## Cycle pins

```text
our start:       f2e22940a
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   38 PRs; no new overlap
critical open:   28
```

## Local cube charge

Away from the heavy roots of the small scalar residual, the cancelled
ambient identity is locally

```text
L_gamma=unit*s_F^3.
```

Thus the horizontal intersection multiplicity is divisible by three and
the specialized excess factor pays at least two degrees. If `I_0` counts
these ordinary incidences and `I_E` those on residual roots, then

```text
2I_0+I_E<=sum c_gamma<=Delta.
```

The core-free degree-two residual now has exactly two distinguished heavy
rows. Their deficits are `{1,1}` with no ordinary incidence or `{1,2}`
with one. The core-one degree-one residual has one distinguished heavy row
of deficit `2..6`; its exact gap ledger has six packets and at most two
ordinary incidences.

The proved leaf is
`rate_half_ca_hankel_a1_first_degree_constant_triple_tangency_packets`.

## Audit boundary

The proof uses local intersection length on a Cartier curve and does not
assume transverse incidences. It does not identify the changed pole divisor
with the original one, and it does not exclude the resulting packets.

## Burn-down

```text
result:                  CLASSIFIED smallest scalar residuals into 2+6 packets
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   none
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next combine the distinguished core-one row of deficit at most six with the
bounded-error Forney/Pade machinery, and test whether `O=Delta` closes the
two core-free packets.
