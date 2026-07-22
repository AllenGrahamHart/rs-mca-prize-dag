# Dependency sub-DAG

```text
l1_exact_shell_fixed_cofactor_prefix_transport [PROVED]
                         |
                        req
                         v
l1_cofactor_depth_budget_cancellation [PROVED]
                         |
                         ev
                         v
l1_mixed_petal_amplification [TARGET]
```

The ambient or full-image locator-prefix estimate appearing in `(CD2)--(CD5)`
is a parameterized input, not a hidden proved dependency.  No such estimate
is consumed to prove the accounting identities.
