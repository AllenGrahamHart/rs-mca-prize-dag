# Fixed R02/R20 degree-12 s-zero exclusion

- **status:** PROVED
- **cells:** `{F04,F05,F06,F07} x {R02,R20}`
- **branch:** generic degree-12 resultant factor with `s=0`

In every literal cell, the specialized degree-12 factor and two remaining
q-slice cores generate a two-element dimension-one basis over
`F_2130706433[x,p]`. The complete transported generic localizer reduces to
zero at factor 14. Therefore all eight `s=0` branches are empty.

This closes one leading-drop leaf only; it does not close a degree-12 branch
with `s != 0` or any complete fixed cell.

## Falsifier

A literal cell with a different terminal, nonzero final localizer, missing
generic unit, or a specialization that fails to preserve all three
equations.
