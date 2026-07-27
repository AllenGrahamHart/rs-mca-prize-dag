# Claim contract

| field | value |
|---|---|
| claim | The reduced reciprocal equations are exactly Newton equations comparing the `m`th-power traces of the star roots with the inverse roots; no `m`th-power resultant is required. |
| status | PROVED |
| dependency | `l1_mersenne_hnf_order_one_frobenius_gate` |
| exact rows | Four `m=8,h=7` rows and one `m=16,h=15` row. |
| first-three powers | `8,16,24` and `16,32,48`. |
| consumer | `l1_mixed_petal_amplification` |
| open residue | Eliminate the trace equations on `Psi_h=0`, then impose pointwise Frobenius, cyclotomic divisibility, and inner lifts on retained components. |

## Falsifier

A root multiset for which a reciprocal coefficient equation disagrees with
the corresponding Newton equality, or a required integer `j` not invertible
on an official row.
