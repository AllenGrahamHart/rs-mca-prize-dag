# Cycle 475: affine-reflection fixed-pencil cap

## Starting pins

```text
our SHA: 59bf9fecc
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream factor-synchronization tip: #1173 at 2788d5ec3
```

## Result: PROVED exact official-field cap

The preregistered census evaluated every nonzero additive constant modulo
`H`-scaling. All 1016 cosets completed in 93 shards, and the forward-bitset
and backward-exponent implementations agreed on every row. The exact output
is

```text
sum_j R_(3^j) = 2097151 = N-1,
max_j R_(3^j) = 2308,
argmax = {74},
3^74 mod p = 1177199610.
```

The maximizing reflection has no fixed point, so the sharp maximum number of
nonfixed two-cycles, hence disjoint split fibers in one fixed nonzero pencil
`X^2-cX+gamma`, is `1154`.

## Posedness correction

The preregistered numerical threshold `1154<=5523` passes with wide margin.
However, the proposed aggregate multiplication

```text
58361*1154=67348594
```

is not yet a heavy-ruling payment. The exception-SPI normal form constructs a
pencil from a selected twenty-record packet, and no theorem currently makes
that pencil canonical across packets from the same pair type. The exact
census closes the fixed-pencil leaf; packet-pencil synchronization remains
the route-defining structural gate.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +2 edges
critical status delta: none
route delta: nonzero affine fixed-pencil census closed exactly
new assumptions: none
next action: synchronize packet pencils or force a collision/owner
```

## Replay

```text
tools/ramguard tiny -- python3 experiments/prize_resolution/verify_rate_half_mca_rank11_affine_reflection_cyclotomic_census.py experiments/prize_resolution/rate_half_mca_rank11_affine_reflection_cyclotomic_census_result.json
tools/ramguard tiny -- python3 experiments/prize_resolution/verify_rate_half_mca_rank11_affine_reflection_cyclotomic_census.py experiments/prize_resolution/rate_half_mca_rank11_affine_reflection_cyclotomic_census_result.json --tamper-selftest
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_exception_spi_affine_reflection_fixed_pencil_cap/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_exception_spi_affine_reflection_fixed_pencil_cap/verify.py --tamper-selftest
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_exception_spi_affine_reflection_fixed_pencil_cap/verify_audit.py
```
