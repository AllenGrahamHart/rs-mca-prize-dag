# Repeated-BC duplicate-role cells 11-14 transport

- **status:** PROVED
- **scope:** all source signs, BC signs, outside-cycle signs, and outside
  labels in the repeated-BC `[11,14]` block

Swapping the duplicate common roles `BC1` and `BC2` maps cell 11 to cell 14.
Because these roles have identical target products and sums, the map is an
exact common-row permutation and fixes the entire outside packet and all 105
outside labels. It bijects 1,680 raw systems in each direction.

## Falsifier

A nonidentical duplicate target row, changed sign parameter, changed outside
label, or an uncovered cell-14 system.
