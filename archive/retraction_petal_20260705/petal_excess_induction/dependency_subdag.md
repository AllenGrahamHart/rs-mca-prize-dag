# dependency sub-DAG: petal_excess_induction

Promoted subclaims.

```text
l1_coset_chart_residue_bridge [PROVED]
    -> petal_residue_kernel_linear_bound [PROVED]
    -> petal_residue_line_uniformity
    -> petal_mixed_amplification_step
    -> petal_excess_induction
    -> petal_growth

petal_residue_kernel_linear_bound [PROVED]
    -> petal_residue_kernel_flatness [REFUTED route]

l1_coset_chart_residue_bridge [PROVED]
    -> petal_realizable_extra_uniformity
    -> petal_residue_line_uniformity
    -> petal_mixed_amplification_step

petal_fixed_excess [PROVED]
    -> petal_growth
```

## petal_residue_line_uniformity

Statement: in the coset-chart residue bridge, the kernel
`K_{I,d} = ker(pi_{>d} R_{I,d})` has dimension and realizable-extra count
bounded uniformly in the excess `c = d - ell` over the corridor range needed
by the list-side proof.

Status: conditional on `petal_residue_kernel_linear_bound` and
`petal_realizable_extra_uniformity`. The proved linear bound records Lemma 13,
`dim K <= c+1`. The attempted stronger route
`petal_residue_kernel_flatness` is refuted by tiny coset rows, so the remaining
work is exact realizable-extra uniformity.

Falsifier: residue-line dimension or exact realizable extras growing with `c`
in a calibration row.

## petal_mixed_amplification_step

Statement: the fixed-excess full-petal bound amplifies from excess `c` to
excess `c+1` with polynomial constants controlled uniformly in `c`.

Status: conditional on `petal_residue_line_uniformity`. The step uses
residue-line data, not the refuted exact-rank formula.

Falsifier: any necessary induction coefficient growing super-polynomially in
the corridor parameters.
