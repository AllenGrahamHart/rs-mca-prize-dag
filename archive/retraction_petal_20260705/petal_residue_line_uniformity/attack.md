# ATTACK - petal_residue_line_uniformity

Use light local computation only.

This node now assembles the proved linear kernel accounting with the remaining
exact-extra predicate:

- `petal_residue_kernel_linear_bound`;
- `petal_realizable_extra_uniformity`.

The repaired Modal helper can be relaunched off-laptop, but do not run broad
growing-excess scans locally. The literal ambient-kernel flatness route is
recorded as refuted in `petal_residue_kernel_flatness`, so the only viable
local route is to show that the growing kernel directions do not produce too
many exact realizable full-petal extras.
