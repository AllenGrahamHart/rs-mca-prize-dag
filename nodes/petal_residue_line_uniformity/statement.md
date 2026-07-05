# petal_residue_line_uniformity

- **status:** CONDITIONAL
- **closure:** proof

## Statement

In the coset-chart residue bridge for the growing-excess petal problem, the
residue-line contribution has uniformly bounded realizable full-petal extras
over the corridor range needed by the list-side proof. The ambient
residue-line kernel

```text
K_{I,d} = ker(pi_{>d} R_{I,d})
```

is controlled by the proved linear Lemma 13 bound `dim K <= c+1`; literal
ambient-kernel flatness is a refuted route, not an input.

## Conditional decomposition

This node is conditional on:

- `petal_realizable_extra_uniformity`.

The proved node `petal_residue_kernel_linear_bound` records the existing
Lemma 13 input `dim K <= c+1`. The refuted node
`petal_residue_kernel_flatness` records why the proof must control exact
realizable extras rather than the full ambient kernel dimension.

## Falsifier

A calibration row or theorem where the exact realizable full-petal extras grow
with `c` beyond the allowed polynomial budget.
