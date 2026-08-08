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
 direct 30-cell registry + F02/F04 closes (PROVED)
                         |
                         v
  18 affine reps + projective/negative audits (OPEN)
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
six `F04` representatives, leaving 18. The projective-boundary and
negative-sign literal audits are separate.
