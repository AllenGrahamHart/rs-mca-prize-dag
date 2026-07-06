# list_corridor_widths

- **status:** TARGET
- **closure:** proof

## Statement

Compute the LIST-side corridor widths per clean rate: the gap in grid steps between the proved list-safe radius (|Lambda| <= eps*|F| above the window) and the proved list-unsafe radius (crossing at the gate), at each rate's official row — the list analogue of W = 2.17/2.00/1.12. Previously unpriced; pure computation from the banked list-safe/unsafe formulas (imgfib-conditional bounds + planted arithmetic).

## Attack surface

the corridor_eaters machinery, list-side formulas; delegable compute

## Falsifier

a rate where the list corridor is already <= 1 grid step (adjacency free)
