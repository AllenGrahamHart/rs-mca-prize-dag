# petal_excess_induction

- **status:** CONDITIONAL
- **closure:** proof

## Statement

Bridge from petal_fixed_excess (PROVED, c fixed) to growing excess: the mixed-amplification induction on c with poly(n) constants uniform in c. EVIDENCE WALL: the growing-excess petal census — pre-registered scan of full-petal extras at c = 2..8 on calibration rows; interpretation fixed: counts flat in c => the induction's shape is right; growth in c => the amplification route needs a new idea (route_exact_rank is already REFUTED).

## Attack surface

the petal census machinery at growing c; delegable compute

## Falsifier

petal extras growing with c at any calibration row

## Conditional decomposition

This node is conditional on:

- `petal_residue_line_uniformity`;
- `petal_mixed_amplification_step`.

The fixed-excess base remains the separate proved input `petal_fixed_excess`
consumed by `petal_growth`.
