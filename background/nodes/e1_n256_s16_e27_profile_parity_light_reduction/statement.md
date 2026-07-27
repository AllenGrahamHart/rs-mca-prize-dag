# E1 N=256 E=27 profile/parity/light reduction

- **status:** PROVED
- **closure:** proof plus exact classification

Let a pair-feasible folded-profile `(3,4,0)` collision at `N=256` have
autocorrelation variance `V=54`, or `E=27`. Then its positive-half
autocorrelation L1 norm satisfies `L<=15`.

There are exactly 12 integer magnitude profiles at energy 27 and `L<=15`.
The exact cubic-Hermite cutoff is `M_3=443`, and diameter parity leaves only

```text
(3,6), (2,4,1), (1,2,2),
(3,2,0,1), (0,0,3), (2,0,1,1).                 (1)
```

Every vector in (1) has exactly one light-light diameter and exactly three
odd autocorrelation classes. The complete normalized light-support ledger is

```text
odd classes   supports   affine odd-unit orbits   multiplicity partition
1                  264                       11   (2,2,1)
3                  960                        8   (2,1,1,1)
5               14,400                      100   (1,1,1,1,1).
```

Consequently all six profiles are covered by exactly eight affine light
templates. The complete diameter ledger is

```text
D_64 in {1,5,9,17,21},       C=(D_64-75)/2.       (2)
```

This theorem is an exact finite router, not by itself an exclusion of `V=54`.
