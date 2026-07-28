# Claim contract

| field | value |
|---|---|
| claim | The six roots remaining after the automatic order-one root is removed cannot all have the same `p+1` Frobenius color. |
| status | PROVED |
| dependency | `l1_mersenne_hnf_order_one_frobenius_gate` |
| consumer | `l1_mixed_petal_amplification` |
| exact rows | Four official `(m,h)=(8,7)` rows with `n=8(p+1)`. |
| excluded stratum | Constant colored Frobenius interpolant on the six reduced roots. |
| open residue | Nonconstant color assignments in the `t notin F_p` conic branch, plus all other declared L1 chambers. |
| nonclaim | No nonconstant degree stratum, cyclotomic converse, inner lift, or global L1 conclusion is proved. |
