# frontier: single_obstruction_valueset

No usable scan result is currently available.

## Existing setup

The Modal script defines:

- a gate validating the generalized forced square-root obstruction against the
  banked h=5/X79 construction and its h in {6,10,21,40} extension;
- a sampled value-distribution scan for `O_{h-1}` over h=21..40 and
  calibration rows `q ~ n^2, n^3`;
- a collision-ratio verdict against the uniform-on-F_p birthday baseline.

The script was syntax-checked in this working copy:

```text
python3 -m py_compile nodes/single_obstruction_valueset/notes/modal_single_obstruction_valueset.py
```

## Modal status

The recorded app `ap-rLAsDplh1N7jQAiy0gmOEE` has only stop messages in the
retrieved logs. It emitted no gate or scan JSON, so it supplies no evidence
for or against the value-set lemma.

## Remaining proof obligations

- `sov_forced_root_correctness`: replay or cite a completed gate proving the forced-root
  obstruction generalization is correct for all h in the intended range.
- `sov_obstruction_equidistribution`: prove value-set equidistribution / small fibers for the map
  `O_{h-1}` on anchored cores at official-shape rows. This is the real
  theorem; a sample scan is only evidence.
- `sov_fiber_budget_translation`: translate the fiber bound into the per-h active-core budget
  used by `midlarge_h20_A`.

The attack surface points to character sums or norm-structure cancellation.
This is closely related in shape to DLI: a low-degree map must have enough
geometric distribution on a structured root-of-unity domain.

## Falsifier

A calibration row where `O_{h-1}` collision rates are far above uniform, or a
structural family of anchored cores on which `O_{h-1}` is constant with fiber
size above the active-core budget.
