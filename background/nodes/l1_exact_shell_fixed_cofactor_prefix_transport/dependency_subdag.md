# Dependency sub-DAG

```text
l1_exact_shell_complement_toeplitz_normal_form [PROVED]
                         |
                        req
                         v
l1_exact_shell_fixed_cofactor_prefix_transport [PROVED]
         |                 |                         |
        req               req                        ev
         v                 v                         v
l1_cofactor_depth_  l1_cofactor_prefix_       l1_mixed_petal_amplification
budget_cancellation  pade_graph_normal_form              [TARGET]
      [PROVED]             [PROVED]
```
