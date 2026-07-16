# Dependency sub-DAG - PMA three-petal projective Johnson bound

```text
pma_three_petal_mu_basis_reduction [PROVED]
                 |
                 | req: primitive coefficient normal form and determinant
                 v
pma_three_petal_projective_johnson_bound [PROVED]
                 |
                 | ev: pays rate-quarter t=3 and positive-J rate-half cells
                 v
petal_mixed_amplification [TARGET] --req--> imgfib [CONDITIONAL]

pma_official_rate_small_source_degree_sieve [PROVED]
                 |
                 | req: exact official source arithmetic and residual scope
                 +------> pma_three_petal_projective_johnson_bound
```

The evidence edge leaves the nonpositive-`J` rate-half tail and every other
PMA branch explicit.
