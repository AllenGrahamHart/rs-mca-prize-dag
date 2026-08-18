# Cycle 497: dimension-two secant-line packing sharpening

## Result: PROVED common core `133485`

The 520 scalar points have affine-line occupancy at most 15. Every point
therefore lies on at least `ceil(519/14)=38` secant lines. Combining the
resulting point-line incidence floor 19,760 with the exact ordered-pair count
269,880 and Cauchy forces at least 1,349 distinct affine secant lines.

In scalar dimension two, actual pair-core intersections belonging to two
distinct affine lines overlap exactly in the received-pair core `J` common
to all types, including for parallel lines. Packing one intersection from
each of 1,349 lines gives

```text
|J|>=ceil((1349*134940-2097152)/1348)=133485.
```

At this floor, reversible shortening leaves 1,349 disjoint petals of size at
least 1,455 and only 872 uncovered coordinates.

## Burn-down

```text
starting local pin:       f3310b795
canonical prize pin:      0dd5b3244
upstream frontier pin:    PR #1173 at 2788d5ec3
DAG delta:                +1 PROVED secant-packing node, +3 edges
critical status delta:    none
closed interface:         coarse dimension-two common-core floor
compute spend:            none
next action:              use quotient exceptions/ownership against the 872-slack packing
```

## Nonclaims

- the shortened 1,349-petal packing is not paid;
- scalar dimensions three and four remain open;
- no high-complexity payment, rank-eleven closure, or MCA closure.
