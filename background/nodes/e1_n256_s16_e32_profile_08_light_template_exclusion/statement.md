# E1 N=256 E=32 profile-(0,8) light-template exclusion

- **status:** PROVED
- **closure:** proof plus two exact censuses

At `N=256`, folded coefficient profile `(3,4,0)`, and autocorrelation
variance `V=64`, autocorrelation magnitude profile `(0,8)` is impossible.

Its zero-odd parity condition forces the four light coefficient positions to
be two antipodal pairs. Up to translation and odd cyclotomic automorphism,
the complete light-support list is

```text
{0,64,t,64+t},       t in {1,2,4,8,16,32}.            (1)
```

Two independent exact engines each exhaust

```text
6 * binom(124,3) * 64 = 119,087,616
```

normalized signed coefficient vectors and retain zero vectors with
autocorrelation profile `(0,8)`.
