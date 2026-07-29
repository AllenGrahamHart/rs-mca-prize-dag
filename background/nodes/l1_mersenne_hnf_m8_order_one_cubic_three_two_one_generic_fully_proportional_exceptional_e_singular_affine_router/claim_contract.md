# Claim contract

| field | value |
|---|---|
| claim | On the exceptional `a_2!=0`, `S_1=S_0=0` chart, the coefficient-proportionality equations are equivalent to two explicit quartics `H=K=0` in `z=b^2`, with `b` reconstructed rationally. |
| status | PROVED |
| dependency | `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_quadratic_router` |
| consumer | `l1_mixed_petal_amplification` |
| equivalence guards | Inherited `b*A(z)!=0`; `163(z+27)` is proved a unit on every official solution. |
| retained coefficient equations | `F_b(z,q)=X_*(b,q)=0`; `E_G=0` follows from (FEQ3). |
| open residue | A common-root/ambient-degree verdict for `(H,K)`, then the retained `q`, `J_*`, structural, role, `P_4`, saturation, and arithmetic-lift equations. |
| nonclaim | No common gcd is asserted unit, no root is asserted to lie or not lie in the ambient quadratic field, and no chart is asserted empty. |
| replay | `verify.py` checks the polynomial identity and DAG packet; `verify_audit.py` independently reconstructs the normalized equations on official prime-field samples. Both are intentionally unexecuted locally under the Modal-only computation rule. |
