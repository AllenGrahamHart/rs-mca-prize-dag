# E1 N=256 square-mass-16 E=32 profile/parity/diameter reduction

- **status:** PROVED
- **closure:** proof plus exact arithmetic

Let a pair-feasible folded-profile `(3,4,0)` collision at `N=256` have
autocorrelation variance `V=64`, or `E=V/2=32`. Then its positive-half
autocorrelation L1 norm satisfies

```text
L<=18.
```

Among the 18 integer magnitude profiles with energy 32 and `L<=18`, the
exact cubic-Hermite norm certificate excludes every profile except

```text
(4,7), (0,8), (3,5,1).                               (1)
```

Their respective `(L, number of odd coefficients)` pairs are

```text
(18,4), (16,0), (16,4).                              (2)
```

The number `d_1` of light-light diameter edges is either zero or two. The
complete diameter and signed-cross ledgers are

```text
D_64 in {0,2,4,8,12,16,18,20},
C=(D_64-70)/2.                                       (3)
```

If `d_1=2`, either four-odd profile in (1) has its four remaining light-light
chords in distinct non-diameter distance classes. If `d_1=0`, those profiles
have exactly four odd light-chord distance classes among six chords. For the
zero-odd profile `(0,8)`, every non-diameter light-chord class has even
multiplicity. The theorem is a reduction, not an exclusion of `V=64`.
