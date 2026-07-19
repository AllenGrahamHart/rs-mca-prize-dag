# F3 h=3 core-orbit count for Terminal C

Status: MACHINE-VERIFIED SIZING/ORGANIZATION STEP.

The full `n=96` Terminal C census can be organized by the affine/Galois orbit
of one side of the shape pair.  For single 3-subsets of `Z/96Z`, the affine
group

```text
x -> u*x+s,  u in (Z/96Z)^*, s in Z/96Z
```

has exactly:

```text
91
```

orbits.

The consecutive-core census already completed the orbit representative
`(0,1,2)`.  This count gives the remaining exact queue: 90 further core types,
with large stabilizer/orbit-size variation.

## Replay

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_orbit_count.py
```

Expected digest:

```text
H3_CORE_ORBIT_COUNT_PASS
```

