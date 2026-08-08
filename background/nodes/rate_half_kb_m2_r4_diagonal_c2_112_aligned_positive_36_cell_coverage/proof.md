# Proof

The seven disjoint supplier packets cover the registry as follows:

| supplier | cells | count |
|---|---:|---:|
| fixed companion inversion | `F00,F01 x R02,R11,R20` | 6 |
| `F02/F03` exact import | `F02,F03 x R02,R11,R20` | 6 |
| fixed balanced exclusion | `F04,F05,F06,F07 x R11` | 4 |
| fixed remaining `R02` exclusion | `F04,F05,F06,F07 x R02` | 4 |
| fixed `R20` exclusion | `F04,F05,F06,F07 x R20` | 4 |
| moving ten-cell import | all moving cells except `M01/M02-R11` | 10 |
| moving balanced-pair certificate | `M01,M02 x R11` | 2 |

Their counts sum to 36. The machine audit expands every row into literal
cell identifiers, checks that the union has size 36 with no overlap, and
checks that it equals the complete Cartesian registry. Every supplier is
PROVED and each concludes emptiness of the complete declared cell system.
Therefore all 36 aligned-positive cells are empty. QED.
