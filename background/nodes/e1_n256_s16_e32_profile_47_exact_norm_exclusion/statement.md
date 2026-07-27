# E1 N=256 E=32 profile-(4,7) exact-norm exclusion

- **status:** PROVED
- **closure:** proof plus two exact norm censuses

At `N=256`, folded coefficient profile `(3,4,0)`, and autocorrelation
variance `V=64`, autocorrelation magnitude profile `(4,7)` is impossible.

The proved four-odd router gives 148 affine odd-unit light-support orbits, and
the proved proper-conductor theorem removes every proper-subfield vector. Two
independent engines each enumerate all

```text
148 * binom(124,3) * 64 = 2,937,494,528
```

representative normalized signed vectors, retain exactly 60,148
full-conductor profile-`(4,7)` vectors, and compute their exact cyclotomic
norms. FLINT and PARI/GP agree on the maximum

```text
N_max = 119477984433218714943829098200259691143739376720677525742811917286342611458,
15*N_max < 2^250.                                      (1)
```

Thus no retained norm is divisible by a pair-feasible prime `p>=2^250`.
