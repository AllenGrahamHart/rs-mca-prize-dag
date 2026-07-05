# single_obstruction_valueset

- **status:** CONDITIONAL
- **closure:** proof

## Statement

THE LEMMA UNDER midlarge_h20_A: for h > 20 at official-shape rows, the first obstruction O_{h-1}, restricted to anchored cores, takes >= C(n,h)/budget distinct values in F_p (equivalently: its fibers are small). EVIDENCE WALL: the value-distribution scan — sample anchored cores at h = 21..40, calibration rows, measure O-value collision rates; pre-registered: collision rate consistent with uniform => the lemma's shape is right; heavy collisions => route dead, fall back to per-h certificates.

## Attack surface

sampling scan, delegable; then the proof via character sums or the norm structure

## Falsifier

O-value collision rates far above uniform at any calibration row

## Conditional decomposition

This node is conditional on:

- `sov_forced_root_correctness`;
- `sov_obstruction_equidistribution`;
- `sov_fiber_budget_translation`.
