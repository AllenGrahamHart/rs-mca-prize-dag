# Dependency sub-DAG

```text
x4_primitive_shiftpair_dyadic_norm_router [PROVED] -------req--+
x4_primitive_shiftpair_haar_norm_product_gate [PROVED] ----req--+
                                                                   v
 x4_primitive_shiftpair_zero_fold_norm_divisibility [PROVED] --ev-->
                                     x4_primitive_star_u1_coverage [TARGET]
```

The new node adds the exact structural-zero factors to the existing
residue-degree and shared-energy norm product.
