# Claim contract

| field | value |
|---|---|
| claim | Unit gcd against `X^(8(p+1))-1` over `F_p` is equivalent to eight unit norm-color gcds after adjoining `mu_8`. |
| status | PROVED |
| dependency | `l1_mersenne_hnf_order_one_frobenius_gate` |
| consumer | `l1_mixed_petal_amplification` |
| compression | 32 color rows become four aggregate prime rows per fixed endpoint polynomial. |
| hit handling | A nonunit aggregate row must be split by `zeta` and is not a packet witness. |
| open residue | Every actual endpoint gcd verdict and all post-gcd reconstruction filters. |
