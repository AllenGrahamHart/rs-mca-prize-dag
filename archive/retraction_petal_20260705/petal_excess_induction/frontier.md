# frontier: petal_excess_induction

No growing-excess census result is currently available.

## Existing inputs

- `petal_fixed_excess` supplies the fixed-excess base.
- `l1_coset_chart_residue_bridge` is PROVED and is already wired as a
  requirement of this node.
- `route_exact_rank` is refuted, so the induction must use the residue-line /
  coset-chart bridge, not the old exact-rank formula.

## Modal status

The recorded Modal run `ap-zd7RoOmGJ1hyL4MooOBOqg` failed before producing a
scan verdict:

```text
AssertionError at subgroup_coset_petals: assert (p - 1) % ell == 0
```

This means the calibration-prime selection could choose a row with no
order-`ell` subgroup, aborting before any flat-vs-growth evidence was emitted.

The script has been patched so invalid rows return `None` and the prime
selector explicitly enforces `p == 1 mod ell`. The patch was syntax-checked
with:

```text
python3 -m py_compile nodes/petal_excess_induction/notes/modal_petal_excess_induction.py
```

The scan was not relaunched locally.

## Remaining proof obligations

- `petal_residue_line_uniformity`: show the residue-line kernel dimension and
  realizable extra count remain bounded uniformly as excess `c` grows in the
  corridor range.
- `petal_mixed_amplification_step`: assuming the full-petal bound at excess
  `c`, prove the excess `c+1` bound with no blow-up in the polynomial constant.

The fixed-excess base plus `PETAL-RLU` plus `PETAL-STEP` would close this node.
If the repaired scan shows growth in `dim K` or exact extras, that growth is
the obstruction and the induction route must be replaced.
