# E1 N=256 E=21 profile/parity/light reduction

- **status:** PROVED
- **closure:** exact finite router

Let a pair-feasible folded-profile `(3,4,0)` collision at `N=256` have
autocorrelation variance `V=42`, or energy `E=21`. Then its positive-half
autocorrelation L1 norm satisfies `L<=13`.

There are exactly eight integer magnitude profiles at energy 21 and `L<=13`.
Diameter parity excludes the nine-odd profile `(8,1,1)` and leaves

```text
one odd:  (1,5), (0,3,1), (1,1,0,1);
five odd: (5,4), (4,2,1), (3,0,2), (5,0,0,1).       (1)
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
D_64 in {1,5,9,17,21},       C=(D_64-81)/2.          (2)
```

No cubic-Hermite cutoff is invoked.
