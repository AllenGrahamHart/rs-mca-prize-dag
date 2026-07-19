# Dependency sub-DAG - DLI ell-two weight-six split-16 counterfixture

```text
dli_wcl_ell2_weight6_triple_cubic_router [PROVED]
              |
              | req (router semantics and guards)
              v
dli_wcl_ell2_weight6_split16_counterfixture [PROVED]
              |
              | ev (split-only route cut)
              v
dli_wcl_zone_coverage [TARGET]
```

The evidence edge forbids dropping the official `2^41` ambient split. It does
not add a new requirement to WCL-ZONE.
