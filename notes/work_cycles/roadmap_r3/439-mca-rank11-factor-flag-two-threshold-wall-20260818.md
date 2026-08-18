# Cycle 439: rank-eleven factor-flag two-threshold wall

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
our SHA: fe73b5407
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
relevant open PRs: #1173 (2788d5ec3), #1172, #1171, #1170
critical mandatory-open count: 28 TARGET nodes
```

Canonical and upstream sources are unchanged. No source tree was modified.

## Action

Test whether one additional ordered-basis rich-flat band can strengthen the
`18166`-coordinate residual output of the exact `2 x 5` factor router.

## Result: METHOD EXHAUSTED

`rate_half_mca_rank11_factor_flag_residual_two_threshold_route_wall` is
PROVED. For every proposed output `S>=18167`, if the intermediate band is
nonempty its dimension-two and dimension-three terms alone cost

```text
187184 R_4 + 3381 R_6 = 66303977459889028,
```

over the residual allowance by `1136007786173558`. If the band is empty, the
formula is the parent one-threshold scan and has maximum output `18166`.

The common-base adapter was also widened from a pencil base to a common base
of either factor space: a common zero of `P` or `B` makes all of `C'=span(PB)`
vanish and therefore routes to `(C)`.

## Burn-down

```text
node/workboard item: KoalaBear rank-eleven serial factor-flag recursion
result: METHOD EXHAUSTED
DAG delta: +1 PROVED background node; critical open count remains 28
upstream delta: exact no-go fence retained for successor packet
delta-star movement: none
new assumptions: none
live compute requests: none
Modal spend: zero
next action: factor-presentation existence, locator synchronization,
             Wronskian/subspace-design collision, or chronology
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_factor_flag_residual_two_threshold_route_wall/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_factor_flag_residual_two_threshold_route_wall/verify_audit.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_factor_flag_residual_two_threshold_route_wall/verify.py --tamper-selftest
tools/ramguard local -- python3 tools/verify_prize_dag.py
```

## Upstream posture

This is a compact, constants-first fence aligned with the successor theorem
named in `#1173`. Export it with the factor-flag packet as justification for
the coupling target, not as evidence against that target.
