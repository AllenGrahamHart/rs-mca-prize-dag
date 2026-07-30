# Source evidence

## Primitive degree-15 catalogue

- GAP PrimGrp commit:
  `5612e113d50ac23a7d10945383936e20440b4e14`
- File: `data/gps1.g`, entry `PRIMGRP[15]` including trailing newline
- Exact extracted size: 894 bytes
- SHA-256:
  `d24658310cb386c9663e95ab9024eab9142d79f849131f499da36eeda82c003e`
- Raw source:
  https://raw.githubusercontent.com/gap-packages/primgrp/5612e113d50ac23a7d10945383936e20440b4e14/data/gps1.g

The entry gives exactly six groups. Four have nontrivial subdegree 14; the
degree-15 `A6,S6` actions have subdegrees 6 and 8.

The primary verifier checks the catalogue and route arithmetic. The
independent verifier reconstructs the `A6,S6` actions on all 15 two-subsets
and the pole-cycle type `5^3`.

Accessed 2026-07-29. The source hash pins the classification input; finite
action claims are replayed locally.
