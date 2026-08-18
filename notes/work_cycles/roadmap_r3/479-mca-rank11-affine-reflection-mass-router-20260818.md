# Cycle 479: affine-reflection mass router

## Result: PROVED owner-safe route cut

The triple-owner family has 322,359,637 records on at most 58,361 pair
types. Charge every small or synchronized nonzero-affine type by the uniform
cap 1,154:

```text
58361*1154=67348594,
322359637-67348594=255011043.
```

Thus either one packet has `chi>=2299571`, or 255,011,043 records lie on
other synchronized rational pencil classes. Since

```text
255011043=4369*58361+31834,
```

one fixed surviving pencil owns at least 4,370 disjoint fibers.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +4 edges
critical status delta: none
route delta: nonzero affine class capped; 255011043-record residual isolated
new assumptions: none
next action: dihedral/fractional/primitive class split or high-complexity payment
```

## Nonclaims

- no surviving pencil class is paid;
- no high-complexity payment;
- no rank-eleven or MCA closure.
