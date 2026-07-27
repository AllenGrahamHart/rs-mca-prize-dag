# E1 N=256 E=28 profile/parity/light reduction

- **status:** PROVED
- **closure:** proof plus exact classification

Let a pair-feasible folded-profile `(3,4,0)` collision at `N=256` have
autocorrelation variance `V=56`, or `E=28`. Then its positive-half
autocorrelation L1 norm satisfies `L<=16`.

There are exactly 14 integer magnitude profiles at energy 28 and `L<=16`.
The exact cubic-Hermite cutoff is `M_3=658`, and diameter parity leaves only

```text
(4,6), (0,7), (3,4,1), (2,2,2),
(4,2,0,1), (1,0,3), (0,3,0,1), (3,0,1,1).       (1)
```

The profiles `(0,7)` and `(0,3,0,1)` have zero odd classes and exactly two
light-light diameters; their 63 normalized antipodal-pair supports form six
affine odd-unit orbits. The other six profiles have four odd classes, no light
diameter, and lie in the proved atlas of 28,800 normalized supports in 148
affine orbits. Thus all eight profiles are covered by exactly
`6+148=154` affine light templates.

The complete branchwise diameter ledger is

```text
d_1=0: D_64 in {0,4,8,12,16,20}, C=(D_64-74)/2;
d_1=2: D_64 in {2,18},             C=(D_64-74)/2.       (2)
```

This theorem is an exact finite router, not by itself an exclusion of `V=56`.
