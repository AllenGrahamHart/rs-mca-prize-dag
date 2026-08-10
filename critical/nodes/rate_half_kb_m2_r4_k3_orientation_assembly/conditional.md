# Conditional proof

The active bridge assigns every `Z_BC` slope to exactly one actual component
of type `(2,4,2)` or `(2,8,1)`, preserving its owner and accounting
multiplicity. The proved orientation theorem partitions the order-two type
into coordinate, source-line, and source-cover branches. Coordinate parity
is disjoint; the negative branch is empty and the positive premise supplies
`U_positive`. The source-line and source-cover premises give the disjoint
values `U_source_line` and `U_source_cover`. The trivial-stabilizer premise
gives `U_trivial` for the other component type.

The bridge and all payment premises use the same received-line owner and
first-match chronology. Therefore every non-positive active slope is counted
once and

```text
U_geometry = U_source_line + U_source_cover + U_trivial.
```

No slope-to-component or multiplicity assertion is inferred merely from the
component-level trichotomy.
