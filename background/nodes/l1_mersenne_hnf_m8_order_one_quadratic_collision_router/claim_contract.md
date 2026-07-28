# Claim contract

| field | value |
|---|---|
| claim | A quadratic colored interpolant with two repeated colors is even; its collision pattern is exactly two antipodal pairs and it satisfies `r(18+d-d^2)+192=0`. |
| status | PROVED |
| dependencies | `l1_mersenne_hnf_order_one_frobenius_gate`, `l1_mersenne_hnf_m8_order_one_conic_reduction` |
| consumer | `l1_mixed_petal_amplification` |
| exact rows | Four official `(m,h)=(8,7)` rows. |
| routed strata | Collision-free, exactly one repeat, or exactly two antipodal repeats with the scalar equation. |
| open residue | All three quadratic strata, color degrees three through five, cyclotomic converse, and inner lifts. |
| nonclaim | No quadratic chamber is declared empty and L1 is not promoted. |
