# E1 N=256 E=31 profile/parity/light reduction

- **status:** PROVED
- **closure:** proof plus exact classification

Let a pair-feasible folded-profile `(3,4,0)` collision at `N=256` have
autocorrelation variance `V=62`, or `E=31`. Then its positive-half
autocorrelation L1 norm satisfies `L<=17`.

There are exactly 15 integer magnitude profiles at energy 31 and `L<=17`.
The exact cubic-Hermite cutoff is `M_3=1302`, and light-chord parity leaves
only

```text
(3,7), (2,5,1), (1,3,2).                            (1)
```

Every profile in (1) has exactly one light-light diameter and three odd
non-diameter autocorrelation coefficients. The complete light-support router
has 960 normalized supports and eight affine odd-unit orbits:

```text
{0,t,2t,64}, {0,t,32,64},       t in {1,2,4,8}.      (2)
```

Every support in (2) has non-diameter chord multiplicities `2,1,1,1`; the
repeated edges share a vertex. The complete diameter ledger is

```text
D_64 in {1,5,9,17,21},       C=(D_64-71)/2.         (3)
```

This theorem is a reduction and shared finite router, not an exclusion of
`V=62`.
