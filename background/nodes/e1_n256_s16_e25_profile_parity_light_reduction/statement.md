# E1 N=256 E=25 profile/parity/light reduction

- **status:** PROVED
- **closure:** exact finite router

Let a pair-feasible folded-profile `(3,4,0)` collision at `N=256` have
autocorrelation variance `V=50`, or `E=25`. Then its positive-half
autocorrelation L1 norm satisfies `L<=15`.

There are exactly 12 integer magnitude profiles at energy 25 and `L<=15`.
The exact cubic-Hermite cutoff is `M_3=13`, and diameter parity leaves only

```text
one odd:  (1,6), (0,4,1), (1,2,0,1), (0,0,1,1), (0,0,0,0,1);
five odd: (5,5), (4,3,1), (3,1,2), (5,1,0,1).                 (1)
```

Every vector in (1) has exactly one light-light diameter. The complete
relevant normalized light-support ledger is

```text
odd classes   supports   affine odd-unit orbits
1                  264                       11
5               14,400                      100.
```

Thus the exact direct-census router has 111 affine templates and a
`111*binom(124,3)*64=2,203,120,896`-vector floor per engine. The complete
diameter ledger is

```text
D_64 in {1,5,9,17,21},       C=(D_64-77)/2.                 (2)
```

This theorem is an exact finite router, not by itself an exclusion of `V=50`.
