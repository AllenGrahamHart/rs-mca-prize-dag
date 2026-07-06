# proof: petal_residue_kernel_linear_bound

The proved upstream packet `l1_coset_chart_residue_bridge` identifies the
full-petal growing-excess configurations with the residue-line map

```text
pi_{>d} R_{I,d}.
```

The proved L1 defect-layer packet `l1_defect_layer_bounds` includes Lemma 13
for this exact full-petal residue-line setting. In the notation used by the
Modal helper for `petal_excess_induction`, Lemma 13 states that the kernel

```text
K_{I,d} = ker(pi_{>d} R_{I,d})
```

has dimension at most `c+1`, where `c=d-ell`.

This proves the linear ceiling on the residue-line kernel. It does not by
itself prove the flatness needed by `petal_residue_line_uniformity`; that
stronger statement is isolated in `petal_residue_kernel_flatness`.
