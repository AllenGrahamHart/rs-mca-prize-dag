# conditional: petal_residue_line_uniformity

## Predicate nodes

- `petal_residue_kernel_linear_bound`
- `petal_realizable_extra_uniformity`

## Claim

Conditional on the proved linear residue-kernel accounting and realizable-extra
uniformity, the coset-chart residue-line contribution is uniformly bounded in
the sense needed by the growing-excess petal induction.

## Proof

The proved `l1_coset_chart_residue_bridge` identifies the new full-petal
configurations with the residue-line kernel

```text
K_{I,d} = ker(pi_{>d} R_{I,d}).
```

The proved predicate `petal_residue_kernel_linear_bound` supplies the only
valid ambient-kernel control currently available: `dim K <= c+1`. The refuted
route `petal_residue_kernel_flatness` shows that literal dimension flatness
cannot be assumed.

The predicate `petal_realizable_extra_uniformity` bounds the exact full-petal
extras realized inside that linearly bounded ambient kernel by a polynomial
whose exponent is independent of `c`.

This is exactly the residue-line budget needed by the mixed-amplification
consumer: the ambient coordinate space may grow linearly, but the realized
extras introduced at each excess layer stay within the uniform polynomial
budget. Hence the residue-line uniformity predicate follows.
