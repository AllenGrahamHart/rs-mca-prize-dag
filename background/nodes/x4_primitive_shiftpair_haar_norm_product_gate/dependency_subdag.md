# Dependency sub-DAG

```text
x4_primitive_shiftpair_dyadic_norm_router [PROVED] --------req--+
x4_general_shiftpair_difference_degree_partition [PROVED] -req--+
                                                                    v
       x4_primitive_shiftpair_haar_norm_product_gate [PROVED] --ev-->
                                      x4_primitive_star_u1_coverage [TARGET]
```

The router supplies the per-fold lower and upper norms.  The new node proves
their shared energy identity and exact product optimization.
