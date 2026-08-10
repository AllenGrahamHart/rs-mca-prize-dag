# Claim contract

## In scope

- Cell 11 of the positive `433-1b` branch.
- The 75 raw labels with `xi <= 4`.
- Exact transport through the universal label-orbit quotient.
- A disjoint and exhaustive ownership partition of all 24 active orbits.

## Out of scope

- The 30 endpoint labels with `xi in {5,6}`.
- Complete cell-11 exclusion.
- Any upstream band or prize closure.

The node is `PROVED` only because every required owner node and the quotient
theorem are themselves `PROVED` and the executable aggregate checks exact
coverage. The endpoint theorem is already proved but remains a separate
dependency of the complete-cell composition.
