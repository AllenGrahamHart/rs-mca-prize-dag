# Claim contract

| field | value |
|---|---|
| claim | The official `m=16,h=15`, order-zero outer HNF chamber is empty. |
| status | PROVED |
| dependencies | `l1_mersenne_next_to_maximal_hypergeometric_normal_form`, `l1_mersenne_hnf_frobenius_reciprocal_gate` |
| exact row | `(n,p,m,h)=(131072,8191,16,15)` |
| certificate | Two bounded exact eliminants and a degree-17 radical over `F_8191`. |
| consumer | `l1_mixed_petal_amplification` |
| open residue | Order one, lower value degrees, inner lifts, and global L1 payment. |

## Falsifier

An `s notin F_8191` satisfying the first three reciprocal coefficient
equations, a mismatch between the two exact constructions, or a nonzero
remainder of `s^8191-s` modulo the printed radical.
