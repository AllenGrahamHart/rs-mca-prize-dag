# Dependency sub-DAG

```text
f3_affine_coset_pair_cubic_preimage_stepanov [PROVED] --req--+
f3_h3_dsp8_nodal_cube_preimage_envelope [PROVED] -----req--+
                                                              v
f3_h3_dsp8_nodal_stepanov_constant_barrier [PROVED]
    --ev--> f3_h3_dsp8_correlation_bound [TARGET]
```

The evidence edge removes parameter retuning as a closing route. It adds no
new premise to the target.
