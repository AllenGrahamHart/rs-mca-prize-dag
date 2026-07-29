# Claim contract

| field | value |
|---|---|
| claim | The fixed `a_2=0` exceptional coefficient chart (FEQ8) is empty in each of the four official characteristics. |
| status | PROVED |
| dependency | `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_quadratic_router` |
| consumer | `l1_mixed_petal_amplification` |
| scope guards | `a_2=0`, (FEQ8), and `p` in `{8191,131071,524287,2147483647}`. |
| contradiction | `E_G=0` forces `b=115275930/45228187`, while `b^2=1575/247` would force the nonzero official obstruction `W` to vanish. |
| open residue | The generic exceptional endpoint, `S_1=S_0=0`, `J_*=0`, the ordinary coefficient chart, role and `P_4` conditions, saturations, arithmetic lifts, and all other `h=7` residue shapes. |
| falsifier | An official prime for which a required denominator or `C_b` vanishes, or for which the printed obstruction `W` has zero residue. |
| replay | `verify.py` reconstructs the rational derivation; `verify_audit.py` independently checks the four finite-field equations. Both are source-complete and intentionally unexecuted locally under the Modal-only computation rule. |
