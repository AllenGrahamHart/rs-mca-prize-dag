# Positive 433-1b/O0b residual owner partition

- **status:** PROVED
- **scope:** exact post-closure principal workload, in raw outside labels

The residual route is the disjoint union

```text
block                         common rows       raw labels
split BC, product rank five   6*15*4 = 360      360*105 = 37,800
repeated BC, cells 1/2        16                16*105  =  1,680
repeated BC, cells 11/14      32                32*105  =  3,360
total                         408                         42,840
```

The split product-rank-drop branch is empty.  In the repeated branch, all
common-unit rows and every cells-3/6 outside system for both `BC` signs are
already empty.  No other common row or outside label survives the certified
partition.

This is an ownership theorem only.  It does not assert that any of the
42,840 labels has a point or that the route is empty.

## Falsifier

An omitted stratum, overlap between blocks, an incorrect formal-to-raw
factor of 105, or a survivor in a branch declared closed.
