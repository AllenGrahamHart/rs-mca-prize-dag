# Dependency sub-DAG - PMA official-rate small-source degree sieve

```text
pma_full_petal_band_composition [PROVED]
                 |
                 | req: exact remaining full-petal coordinates
                 v
pma_official_rate_small_source_degree_sieve [PROVED]
                 |
                 | ev: removes official small-M cells and pays one-projective branch
                 v
petal_mixed_amplification [TARGET] --req--> imgfib [CONDITIONAL]

pma_three_petal_mu_basis_reduction [PROVED]
                 |
                 | req: one-projective-point lower branch
                 +------> pma_official_rate_small_source_degree_sieve
```

The sieve is evidence for a smaller PMA residual. It does not count the
surviving upper mu-basis modules and therefore does not become a requirement
edge into the red target.
