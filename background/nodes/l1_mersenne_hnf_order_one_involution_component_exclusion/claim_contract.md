# Claim contract

| field | value |
|---|---|
| claim | The `c=-1` component of the order-one hypergeometric curve is empty on all five official next-to-maximal rows. |
| status | PROVED |
| dependency | `l1_mersenne_hnf_order_one_frobenius_gate` |
| exact rows | Four `m=8,h=7` rows and one `m=16,h=15` row. |
| residual | `Psi_7=0` of bidegree `(2,4)` and `Psi_15=0` of bidegree `(6,12)`, plus the reciprocal, Frobenius, cyclotomic, and inner equations. |
| consumer | `l1_mixed_petal_amplification` |

## Falsifier

An official row with `q|n`, a nonzero odd coefficient in (1), or a mismatch
between the reconstructed residual degrees and (IOC2).
