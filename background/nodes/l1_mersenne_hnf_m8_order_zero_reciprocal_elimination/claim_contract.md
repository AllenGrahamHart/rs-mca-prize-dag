# Claim contract

| field | value |
|---|---|
| claim | The complete `m=8,h=7` order-zero outer HNF chamber is empty on all four official rows. |
| status | PROVED |
| dependencies | `l1_mersenne_next_to_maximal_hypergeometric_normal_form`, `l1_mersenne_hnf_frobenius_reciprocal_gate` |
| exact rows | `(n,p)=(65536,8191),(1048576,131071),(4194304,524287),(17179869184,2147483647)` |
| consumer | `l1_mixed_petal_amplification` |
| proof object | Two exact reciprocal-coefficient eliminants per row; their degree-1032 gcd has only prime-field roots. |
| independent audit | Reconstructs `Q_s` from companion matrices and Newton traces, then repeats all interpolation and gcd arithmetic without a symbolic resultant. |
| excluded stratum | `ord_0(T)=0`, `m=8`, `h=7`, every colored-interpolant degree. |
| open residue | The `m=16` order-zero chamber, order one, other checkpoint widths, and the aggregate L1 payment. |
| nonclaim | No critical node, complete HNF endpoint family, L1 numerator, or prize endpoint is closed. |
