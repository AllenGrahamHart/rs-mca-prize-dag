# Dependency sub-DAG

```text
f3_h3_dsp8_unit_trace_elliptic_curve_router [PROVED] --------req-->
                                                                        f3_h3_dsp8_nodal_trace_parameter_router [PROVED]
f3_affine_coset_pair_optimized_stepanov [PROVED] --------------req-->              |
                                                                                 req
                                                                                   |
                                                                                   v
                                                    f3_h3_dsp8_nodal_target_divisor_pruning [PROVED]
```
