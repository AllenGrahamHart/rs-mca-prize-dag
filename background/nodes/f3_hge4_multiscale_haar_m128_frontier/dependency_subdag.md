# Dependency sub-DAG

```text
f3_hge4_multiscale_haar_m64_level_close
        |  (general multiscale norm product and integer gate)
        v
f3_hge4_multiscale_haar_m128_frontier
        ^
        |-- f3_hge4_cyclotomic_norm_quarter_width_exclusion
        `-- f3_hge4_nonfull_complement_third_gate

f3_hge4_multiscale_haar_m128_frontier
        --ev--> f3_hge4_norm_gate_count
```

All three incoming edges are requirements. The outgoing edge is evidence:
the node closes one exact level above a width cutoff but not the complete
aggregate.
