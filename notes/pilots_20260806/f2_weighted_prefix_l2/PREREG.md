# F2 weighted odd-prefix L2 identity - preregistration

- **date:** 2026-08-06
- **candidate node:** `f2_admissible_weighted_prefix_l2_identity`
- **candidate status:** PROVED

For four finite half-system rows, independently enumerate every subset
fiber and every ternary vector.  Check the exact integer identity

```text
sum_v N(v)^2 = 2^S sum_(kernel eps) 2^-wt(eps),
```

the diagonal and Cauchy lower bounds, and the final DAG requirement/evidence
edges.  Run in one fresh Modal worker with one CPU, 1 GiB RAM, a 120-second
function cap, a 90-second subprocess cap, and zero retries.  Only a zero
return code and the printed PASS marker authorize banking.  The finite rows
audit the normalization; the theorem rests on the written bijection.

## Result

Modal app `ap-Lik7i7u6TSwxHdBhbDIxzK` returned PASS.  The four rows contained
4,688 ordered subset collisions and 404 ternary kernel words, with exact
agreement and the complete DAG contract.  The captured result has SHA-256
`a4def485e2604a26a38decb915209f1a02e91f2f76574529d8364f4d0181d408`.
