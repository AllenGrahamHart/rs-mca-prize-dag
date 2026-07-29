# Claim contract

| field | value |
|---|---|
| claim | On the retained `J_*=L_*=0` coefficient chart, `X_*=0` gives `Q_0=q^2/3`; the original `Q_0` equation reconstructs `G_2`, and all remaining structural definitions are equivalent to two filters that become univariate of degrees at most 24 and 16. |
| status | PROVED |
| dependency | `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_j0_affine_router` |
| consumer | `l1_mixed_petal_amplification` |
| equivalence guards | Inherited `b*(b+3)*D_*!=0`, all earlier saturations, and the proved `T!=0` guard from the dependency. |
| complete compiled endpoint | `Bhat=Ehat=Fhat=Xhat=Zhat_D^j=Zhat_R^j=0`, with `q=5bM/T` and every guard retained. |
| open residue | A common-root and ambient-degree verdict for the six filters, followed by the selected role-discriminant weld, `P_4`, saturations, and arithmetic lifts. |
| nonclaim | No common gcd is asserted unit, no ambient quadratic root is asserted to exist or not exist, and no chart or critical node is asserted empty or closed. |
| replay | `verify.py` constructs exact sparse-polynomial numerator representatives and checks the degree/DAG packet; `verify_audit.py` independently checks the reversible structural identities on rational samples. Both are intentionally unexecuted locally under the Modal-only computation rule. |
