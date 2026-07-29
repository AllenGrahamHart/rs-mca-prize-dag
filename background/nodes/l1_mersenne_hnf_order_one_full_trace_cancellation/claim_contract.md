# Claim contract

| field | value |
|---|---|
| claim | The automatic order-one root contributes identically to the star and inverse `m`-power traces, so every initial reduced reciprocal system is exactly the corresponding full-`P` trace system. |
| status | PROVED |
| dependency | `l1_mersenne_hnf_order_one_newton_reciprocal_reduction` |
| exact rows | Four `(m,h)=(8,7)` rows and one `(m,h)=(16,15)` row. |
| representation gain | No division by the known root and no `Qtilde` construction. |
| consumer | `l1_mixed_petal_amplification` |
| open residue | Eliminate the full-trace equations on `Psi_h=0`, then impose pointwise Frobenius, torsion, cyclotomic divisibility, and inner lifts. |

## Falsifier

An official order-one parameter point for which
`(x_0^star)^(mj) != x_0^(-mj)`, or a reduced coefficient equation that is
not equivalent to the corresponding initial trace equalities.
