# Dependency sub-DAG - PMA sigma-one B11 scope

```text
pma_b11_first_match_router [PROVED]
              |
              v
pma_sigma_one_b11_scope [PROVED]
              |
              v evidence
pma_wide_residual [REFUTED]
```

The source router supplies the exact cells and certificate. This node
specializes them, proves the finite route cut, and feeds the red leaf only as
proved evidence. It creates no speculative conditional below the red leaf.
