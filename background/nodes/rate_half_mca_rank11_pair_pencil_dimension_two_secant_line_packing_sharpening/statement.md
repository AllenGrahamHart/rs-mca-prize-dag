# Dimension-two secant-line packing sharpening

- **status:** PROVED
- **scope:** the scalar-dimension-two quotient pair-pencil branch

The 520 selected scalar points determine at least

```text
1349                                                     (SP1)
```

distinct affine secant lines. For each line choose two selected endpoints
and their complete pair-core intersection `I_L`. Distinct secant lines obey

```text
I_L intersection I_M=J,                                (SP2)
```

where `J` is the received-pair core common to all quotient types. Therefore

```text
|J|>=ceil((1349*134940-2097152)/1348)=133485.          (SP3)
```

After the proved reversible shortening by `J`, the 1349 petals `I_L\J` are
pairwise disjoint. At the minimum core size they each have at least 1455
coordinates and leave only

```text
(2097152-133485)-1349*1455=872                         (SP4)
```

coordinates uncovered.

## Falsifier

Fewer than 1349 affine secant lines; two distinct line intersections sharing
a coordinate outside `J`; a common core below 133485; or incorrect residual
petal size or slack.
