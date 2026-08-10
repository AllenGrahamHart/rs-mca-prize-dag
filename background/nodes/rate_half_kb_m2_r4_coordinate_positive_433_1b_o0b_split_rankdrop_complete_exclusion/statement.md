# Positive 433-1b/O0b split-BC product-rank-drop exclusion

- **status:** PROVED
- **scope:** the complete deployed product-row rank-at-most-four branch in
  the six split-`BC` target lanes

The common split compiler and deployed rational classifier leave exactly
sixteen guarded rank-drop points.  The signed-edge atlas gives six split
outside lanes:

```text
S0  with sigma_o in {-1,+1},
SDE with sigma_o in {-1,+1},
SDF with sigma_o in {-1,+1}.
```

For every point and lane, choose any of the seven outside records at the
missing singleton source label and any of the fifteen perfect matchings of
the other six records.  All

```text
16 points * 6 lanes * 7 records * 15 matchings = 10,080
```

target-guarded necessary ideals are unit ideals over `F_2130706433`.
Therefore no deployed `433-1b -> O0b` split-`BC` packet lies on the
product-rank-drop branch.

## Falsifier

A missing point/lane/label, a nonunit guarded ideal, an incorrect signed
outside record, or an admissible rank-drop packet.
