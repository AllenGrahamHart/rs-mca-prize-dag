# list_corridor_widths

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: TARGET]
- **closure:** proof

## Statement

Compute the LIST-side corridor widths per clean rate: the gap in grid steps between the proved list-safe radius (|Lambda| <= eps*|F| above the window) and the proved list-unsafe radius (crossing at the gate), at each rate's official row — the list analogue of W = 2.17/2.00/1.12. Previously unpriced; pure computation from the banked list-safe/unsafe formulas (imgfib-conditional bounds + planted arithmetic).

## Attack surface

the corridor_eaters machinery, list-side formulas; delegable compute

## Falsifier

a rate where the list corridor is already <= 1 grid step (adjacency free)
