# Claim contract

| field | value |
|---|---|
| claim | A retained J-zero role candidate has a complete finite outer replay in `F_(p^8)`: reconstruct its normalized color cubic, check one norm and one degree-six pointwise Frobenius congruence over at most 42 normalized roles and eight global colors, and full `P | W^(8(p+1))-1` follows. |
| status | PROVED |
| dependencies | J-zero role/`P_4` compiler; cubic `3+2+1` factor reduction; official Frobenius-role split; order-one Frobenius gate; coefficient-field degree-eight router |
| consumer | `l1_mixed_petal_amplification` |
| equivalence guards | Every inherited coefficient-chart guard; `q*d*(q-d)*D*K_6*R*S*Delta*W!=0`; the common-quadratic/exact-fiber guards; `B!=0`; and coprimality of `W+1/d` with `L`. |
| exact replay | Match `eta` to normalized `(beta,gamma)`, reconstruct `F,G,L,E`; require `d^(8(p+1))=1` and `W^(p+1)=tau E mod L` for some `tau in mu_8`. |
| consequence | Exact color multiplicities, pointwise Frobenius, the order-one `c^p` relation, and full outer cyclotomic divisibility. |
| open residue | Eight-filter common-root results, every guard result, the norm and pointwise-congruence results, the separate global inner lift, other h=7 shapes, and the critical consumer. |
| nonclaim | No candidate is asserted to exist, survive, or lift; no inner-lift theorem or critical close is claimed. |
| replay | `verify.py` checks the DAG and scaling contract; `verify_audit.py` independently checks the normalized color/factor identity over exact rationals. Both are intentionally unexecuted locally under the Modal-only computation rule. |
