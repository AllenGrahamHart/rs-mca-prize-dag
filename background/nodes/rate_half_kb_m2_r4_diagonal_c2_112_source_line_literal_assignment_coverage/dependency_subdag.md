# Dependency sub-DAG

```text
fixed 24-cell packets + moving 12-cell packets
                         |
                         v
       aligned-positive 36-cell coverage (PROVED)
                         |
                         v
 near-positive literal inversion transport (PROVED)
           108 -> 42 -> 12 + 30
                         |
                         v
 affine direct + 48-cell boundary coverage (PROVED)
                         |
                         v
       aligned/near-negative literal audits (OPEN)
                         |
                         v
          literal-assignment coverage (TARGET)
                         |
                         v
       complete source-line exclusion (CONDITIONAL)
```

The TARGET remains a logical leaf. Its aligned-positive subbranch is complete.
The affine near-positive transport leaves 30 direct representatives. Four
`F02` square orbits close directly and both mixed orbits close on the
forbidden `c=d` collision. Dual complete-chart certificates then close all
six `F04` and all six `F06` representatives. Five `M01` cells are q-slice
empty; the last exact two-point orbit fails the first quotient norm under
literal replay. Five `M03` cells are q-slice empty; the last exact four-point
scheme fails the first quotient norm on all eight literal companions. Thus
the affine direct residual is empty. A direct 48-cell compiler separately
closes the complete positive projective boundary. Only the aligned-negative
and near-negative literal audits remain.
