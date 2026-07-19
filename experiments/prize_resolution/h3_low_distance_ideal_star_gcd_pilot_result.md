# H3 low-distance ideal-star gcd pilot

- **status:** EXPERIMENTAL route evidence; no theorem promotion.
- **Modal app:** `ap-yiFl4ymMCORN2txyqtXONi`.
- **resources:** two sequential functions, one physical CPU, 1 GiB RAM, and a
  120-second hard timeout each.
- **observed function time:** `0.321` seconds at `n=32` and `6.899` seconds at
  `n=64`, plus image startup.
- **campaign cost cap:** `$0.10`; published-rate requested-resource cost for
  the completed function time is below `$0.001`.
- **result hash:**
  `17f47ce015e1d70327fb78a126c3f8afe0366074af6d83367866f57b0e353ab8`.

The complete screen used one representative of every Galois orbit of
squared-norm-at-most-three centers. It found

```text
order   centers/orbits   low edges   rooted stars    relevant primes
32      435/40           72,849      24,407,583      103 -> 103
64      1,891/87         1,558,905   2,569,691,591   2,127 -> 2,127
```

The arrow compares primes dividing at least one normalized low-distance
principal norm with primes dividing two such norms incident to one center.
Every relevant prime survived at both orders. Thus rational gcd screening
alone gives no candidate-prime compression, and raw rooted-star enumeration
is already scaling too quickly.

This does not test the exact two-generator ideal norm. Two principal norms can
share a rational prime through different prime ideals above it. The selected
next bounded test is therefore prime-ideal alignment: fix one primitive
`n`th root modulo each relevant prime and ask whether one shifted-product
fiber contains an actual low-distance rooted star.

Replay the pinned summary checks with

```text
tools/ramguard tiny -- python3 experiments/prize_resolution/h3_low_distance_ideal_star_gcd_pilot_check.py
```
