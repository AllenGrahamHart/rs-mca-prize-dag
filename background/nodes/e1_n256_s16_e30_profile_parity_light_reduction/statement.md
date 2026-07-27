# E1 N=256 E=30 profile/parity/light reduction

- **status:** PROVED
- **closure:** proof plus exact classification

Let a pair-feasible folded-profile `(3,4,0)` collision at `N=256` have
autocorrelation variance `V=60`, or `E=30`. Then its positive-half
autocorrelation L1 norm satisfies `L<=18`.

There are exactly 18 integer magnitude profiles at energy 30 and `L<=18`.
The exact cubic-Hermite cutoff is `M_3=1087`, and light-chord parity leaves
only

```text
(6,6), (2,7), (5,4,1), (1,5,1),
(4,2,2), (0,3,2), (6,2,0,1), (3,0,3).       (1)
```

Every profile in (1) has zero light-light diameters and either two or six odd
non-diameter autocorrelation classes. The exact light-support ledger is

```text
two odd classes:  8,168 normalized supports in 87 affine odd-unit orbits;
six odd classes: 280,720 normalized supports, all six light chords distinct.
```

The two-odd multiplicity partitions are `2,2,1,1` and `3,2,1`, occurring in
82 and 5 affine orbits. Since a normalized affine orbit has size at most 256,
the six-odd branch has at least 1,097 orbits. A direct representative census
would therefore inspect at least 21,773,185,792 signed vectors.

The complete diameter ledger is

```text
D_64 in {0,4,8,12,16,20},       C=(D_64-72)/2.       (2)
```

This theorem is a reduction and route fence, not an exclusion of `V=60`.
