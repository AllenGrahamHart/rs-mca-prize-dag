# E1 N=256 E=29 profile/parity/light reduction

- **status:** PROVED
- **closure:** proof plus exact classification

Let a pair-feasible folded-profile `(3,4,0)` collision at `N=256` have
autocorrelation variance `V=58`, or `E=29`. Then its positive-half
autocorrelation L1 norm satisfies `L<=17`.

There are exactly 17 integer magnitude profiles at energy 29 and `L<=17`.
The exact cubic-Hermite cutoff is `M_3=872`, and diameter parity leaves only

```text
(5,6), (1,7), (4,4,1), (0,5,1),
(3,2,2), (5,2,0,1), (2,0,3), (1,3,0,1).       (1)
```

Every vector in (1) has exactly one light-light diameter. The complete
normalized light-support ledger is

```text
odd classes   supports   affine odd-unit orbits   multiplicity partition
1                  264                       11   (2,2,1)
3                  960                        8   (2,1,1,1)
5               14,400                      100   (1,1,1,1,1).
```

No profile in (1) has three odd classes. Consequently all eight profiles are
covered by exactly `11+100=111` affine light templates. The complete diameter
ledger is

```text
D_64 in {1,5,9,17,21},       C=(D_64-73)/2.       (2)
```

This theorem is an exact finite router, not by itself an exclusion of `V=58`.
