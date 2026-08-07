# Dependency sub-DAG

```text
x4_general_shiftpair_difference_degree_partition [PROVED] --req--+
upstream_sp_coefficient_scale_quotient_sieve [PROVED] ------req--+
dli_norm_gate_energy_ceiling [PROVED] ----------------------req--+
                                                                    v
          x4_primitive_shiftpair_dyadic_norm_router [PROVED] --ev-->
                                      x4_primitive_star_u1_coverage [TARGET]
```

The dependencies identify the residual shift-pair object, remove its common
coefficient-scale branch, and provide the general integer-vector norm
ceiling.  The new node proves the exact adapter between those interfaces.
