# Dependency sub-DAG

```text
fixed 24-cell packets + moving 12-cell packets
                         |
                         v
       aligned-positive 36-cell coverage (PROVED)
                         |
                         v
   aligned-negative + near-aligned audits (OPEN)
                         |
                         v
          literal-assignment coverage (TARGET)
                         |
                         v
       complete source-line exclusion (CONDITIONAL)
```

The TARGET remains a logical leaf. Its aligned-positive subbranch is complete;
the residual is exactly the literal aligned-negative and near-aligned audit.
