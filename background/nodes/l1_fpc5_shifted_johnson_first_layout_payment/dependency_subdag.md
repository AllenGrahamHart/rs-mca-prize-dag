# Dependency sub-DAG

```text
l1_general_first_layout_domination [PROVED] --------req-->
l1_fpc5_shifted_johnson_grs_shell_cap [PROVED] -----req-->
  l1_fpc5_shifted_johnson_first_layout_payment
    [PROVED] ----------------------------------------ev-->
      l1_fpc5_large_source_payment [TARGET]
```

The first supplier removes source-layout multiplicity and adds only the
planted-anchor remainder. The second supplies the exact fixed touched-cell
bound.
