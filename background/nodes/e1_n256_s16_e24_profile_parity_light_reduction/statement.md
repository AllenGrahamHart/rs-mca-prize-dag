# E1 N=256 E=24 profile/parity/light reduction

- **status:** PROVED
- **closure:** proof plus exact finite classification

Let a pair-feasible folded-profile `(3,4,0)` collision at `N=256` have
autocorrelation variance `V=48`, or energy `E=24`.  Then its positive-half
autocorrelation L1 norm satisfies `L<=14`.

Exactly nine integer magnitude profiles have energy 24 and `L<=14`.  Diameter
parity excludes the three eight-odd profiles and leaves exactly

```text
zero odd: (0,6), (0,2,0,1);
four odd: (4,5), (3,3,1), (2,1,2), (4,1,0,1).             (1)
```

The zero-odd branch has two light-light diameters and uses 63 normalized light
supports in 6 affine odd-unit orbits.  The four-odd branch has no light-light
diameter and uses 28,800 normalized supports in 148 affine orbits.  Therefore
the exact direct router has 154 templates and

```text
154*binom(124,3)*64 = 3,056,582,144
```

signed vectors per engine.  No cubic-Hermite cutoff is invoked.
