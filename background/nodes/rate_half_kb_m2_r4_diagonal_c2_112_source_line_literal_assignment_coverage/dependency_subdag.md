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
  30 affine reps + projective/negative audits (OPEN)
                         |
                         v
          literal-assignment coverage (TARGET)
                         |
                         v
       complete source-line exclusion (CONDITIONAL)
```

The TARGET remains a logical leaf. Its aligned-positive subbranch is complete.
The affine near-positive transport is exact but leaves 30 representatives;
projective-boundary and negative-sign literal audits are separate.
