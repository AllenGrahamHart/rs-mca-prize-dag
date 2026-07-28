# E1 N=256 E=26 profile/parity/light reduction

- **status:** PROVED
- **closure:** proof plus exact classification and route cut

Let a pair-feasible folded-profile `(3,4,0)` collision at `N=256` have
autocorrelation variance `V=52`, or `E=26`. Then its positive-half
autocorrelation L1 norm satisfies `L<=16`.

There are exactly 13 integer magnitude profiles at energy 26 and `L<=16`.
The exact cubic-Hermite cutoff is `M_3=228`, and diameter parity leaves only

```text
two odd: (2,6), (1,4,1), (0,2,2), (2,2,0,1), (1,0,1,1), (1,0,0,0,1);
six odd: (6,5), (5,3,1), (4,1,2), (6,1,0,1).                 (1)
```

Every vector in (1) has no light-light diameter. The complete relevant
normalized light-support ledger is

```text
odd classes   supports   affine odd-unit orbits
2                8,168                       87
6              280,720                    1,234.
```

Thus the exact direct-census router has `87+1234=1,321` affine templates and a
floor of

```text
1321*binom(124,3)*64 = 26,219,123,456
```

signed vectors per engine. This theorem authorizes the 87-template two-odd
branch but cuts the undifferentiated direct census of the six-odd branch.
