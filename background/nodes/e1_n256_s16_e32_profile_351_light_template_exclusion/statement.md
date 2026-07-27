# E1 N=256 E=32 profile-(3,5,1) light-template exclusion

- **status:** PROVED
- **closure:** proof plus two exact censuses

At `N=256`, folded coefficient profile `(3,4,0)`, and autocorrelation
variance `V=64`, autocorrelation magnitude profile `(3,5,1)` is impossible.

The proved four-odd router reduces the light support to 148 affine odd-unit
orbits. Two independent exact engines each exhaust

```text
148 * binom(124,3) * 64 = 2,937,494,528
```

representative normalized signed vectors. They agree on

```text
profile-(3,5,1) vectors                 29,238;
full-conductor profile vectors          15,440;
unrestricted maximum M_3                 1,392;
full-conductor maximum M_3                1,392.       (1)
```

Since `1392<1517`, the exact cubic norm certificate from the `V=64` profile
reduction puts every such collision norm strictly below `2^250`.
