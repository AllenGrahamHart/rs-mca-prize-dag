# Conditional proof

The positive-coordinate premise supplies the exact disjoint value
`U_positive`. The orientation premise proves that the source-line,
coordinate, and source-cover classes are exhaustive and disjoint, and supplies
the exact source-cover value `U_sourcecover`. The source-line and negative
coordinate values are zero by the two proved evidence theorems. Therefore the
complete K3 value is

```text
U_K3 = U_positive + U_sourcecover.
```

The allocation premise prints the same integers in the same active manifest
and proves `U_K3 <= U_K3_allocation`. This establishes the claimed K3 ledger.
