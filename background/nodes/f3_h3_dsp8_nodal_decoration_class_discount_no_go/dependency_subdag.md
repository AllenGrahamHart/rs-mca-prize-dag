# Dependency sub-DAG

```text
f3_h3_dsp8_unit_product_trace_normal_form -----------req--+
                                                          +--> this node
f3_h3_dsp8_nodal_target_divisor_pruning -------------req--+

this node --ev--> f3_h3_dsp8_correlation_bound
```

The evidence edge is a route prohibition. It does not add a premise to DSP8
or alter the target's truth status.
