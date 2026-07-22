# Dependency sub-DAG

```text
f3_h3_dsp8_smooth_trace_substar_router [PROVED]
    \
     -> f3_h3_dsp8_nodal_smooth_high_tail_domination [PROVED]
    /
f3_h3_dsp8_disjoint_six_multiplicity_gate [PROVED]

f3_h3_dsp8_nodal_smooth_high_tail_domination
    -ev-> f3_h3_dsp8_correlation_bound [TARGET]
```

The first dependency supplies the maximum-degree-three nodal graph. The
second supplies the disjoint-edge lower bounds and rich-fiber multiplicity
thresholds. The evidence edge records a structural reduction only.
