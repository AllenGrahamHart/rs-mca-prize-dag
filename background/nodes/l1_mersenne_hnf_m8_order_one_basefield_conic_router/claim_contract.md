# Claim contract

| field | value |
|---|---|
| claim | The base-field conic-parameter branch is empty on the two smaller `m=8` rows and reduces to at most two explicit scalar packets on each larger row. |
| status | PROVED |
| dependencies | Conic reduction and the non-prime-field shifted-value gate. |
| closed rows in this branch | `p=8191,131071`. |
| residual rows in this branch | `p=524287,2147483647`, with (BCR2). |
| untouched branch | `t notin F_p`. |
| consumer | `l1_mixed_petal_amplification` |

## Falsifier

A base-field-parameter survivor outside (BCR2), a survivor on either
`z=-1` point, or a base-field-parameter point on one of the two smaller rows
that satisfies every inherited order-one gate.
