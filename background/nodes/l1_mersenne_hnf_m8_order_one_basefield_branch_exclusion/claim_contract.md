# Claim contract

| field | value |
|---|---|
| claim | Every official `m=8,h=7` order-one survivor has `t notin F_p`; the entire base-field conic-parameter branch is empty. |
| status | PROVED |
| dependency | `l1_mersenne_hnf_m8_order_one_basefield_conic_router` |
| key bound | At most six possible split roots versus seven distinct roots of `P`. |
| consumer | `l1_mixed_petal_amplification` |
| open residue | `t notin F_p`, plus all non-`h=7` L1 chambers. |

## Falsifier

An official base-field-parameter point whose degree-seven `P` passes the
inherited cyclotomic condition, or a seventh distinct solution of (5) outside
the six-point color bound.
