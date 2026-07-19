# Dependency sub-DAG

```text
rate_half_ca_hankel_split_pencil_equivalence [PROVED]
                    |
                    v
rate_half_ca_hankel_fixed_kernel_branch [PROVED]
                    |
                    v
rate_half_band_closure [TARGET]
```

The incoming edge supplies the exact split-locator interpretation. The new
node contributes evidence to the target by removing the constant-kernel
rank-deficient branch; it does not close the moving-kernel branch.
