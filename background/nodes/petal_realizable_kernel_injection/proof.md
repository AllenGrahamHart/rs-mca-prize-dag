# proof: petal_realizable_kernel_injection

The proved upstream packet `l1_coset_chart_residue_bridge` supplies the
coset-chart coordinates for full-petal extras. In that chart, a full-petal
extra with touched set `I` and defect `d` has a missed-core divisor `D` and
therefore a squarefree locator polynomial `L_D`.

The banked Lemma 8 full-petal rank certificate, restated in
`petal_fixed_excess/proof.md`, says that non-planted full-petal extras with
the same `(I,d)` inject into

```text
{L_D : D subset C, |D| = d} cap K_{I,d},

K_{I,d} = ker(pi_{>d} R_{I,d}).
```

The condition that the extra is realizable is exactly what gives an actual
missed-core subset `D`, hence a squarefree locator `L_D`. The residue bridge
identifies the high-coefficient constraints for being a full-petal extra with
membership in `K_{I,d}`. Thus every exact realizable full-petal extra maps to
a squarefree locator point in the residue-line kernel.

If two realizable extras have the same locator `L_D`, then they have the same
missed-core subset `D`; the coset-chart bridge recovers the same full-petal
extra data from that locator in the fixed `(I,d)` chart. This is precisely the
injectivity assertion of Lemma 8.

Therefore exact realizable full-petal extras are bounded by the number of
squarefree locator points in the residue-line kernel. The remaining theorem,
`petal_kernel_realizable_sparsity`, is to bound those points uniformly in the
growing-excess corridor.
