# H3 low-distance norm-template pilot

- **status:** EXPERIMENTAL route evidence; no theorem promotion.
- **Modal app:** `ap-J4kT8st6P45yWvWZtc2Xgi`.
- **resources:** two sequential functions, one physical CPU, 1 GiB RAM, and a
  60-second hard timeout each.
- **observed function time:** `0.414` seconds at `n=32` and `6.501` seconds at
  `n=64`, plus image startup.
- **campaign cost cap:** `$0.10`; published-rate requested-resource cost for
  the completed function time is below `$0.001`.
- **result hash:**
  `ec1c79b660a15cad985423b6536e39acf9408e3b349113c5e065d40f43a026bf`.

The complete `n=32` census found

```text
77,656 raw distance-at-most-six edges
5,216 Galois/exchange orbits
227 distinct absolute norms
103 relevant prime divisors (p>=n^2 and p=1 mod n).
```

This is a `22.98x` equality-of-norm compression. It does not persist at the
next sampled order. The complete `n=64` orbit census found `52,494` orbits;
the first `5,000` already produced `2,567` distinct norms, only `1.95x`
compression. Thus exact-norm deduplication by itself is not the algebraic
compression needed by `CR-001`.

This pilot does not estimate the number of distinct norms over all `n=64`
orbits, does not extrapolate a rigorous growth exponent, and does not check an
official row. Its decision value is negative: do not launch more raw norm
shards without a stronger selector or a proved coarser norm template.

Replay the pinned summary checks with

```text
tools/ramguard tiny -- python3 experiments/prize_resolution/h3_low_distance_norm_template_pilot_check.py
```
