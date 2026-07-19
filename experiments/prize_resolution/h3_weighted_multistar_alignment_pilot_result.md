# H3 weighted-multistar alignment pilot

- **status:** EXPERIMENTAL route evidence; no theorem promotion.
- **Modal app:** `ap-jU9q1eWAaOiRkg3sqZForL`.
- **resources:** two sequential functions, one physical CPU, 1 GiB RAM, and a
  120-second hard timeout each.
- **observed function time:** `0.289` seconds at `n=32` and `5.825` seconds at
  `n=64`.
- **published-rate requested-resource cost:** below `$0.001`.
- **result hash:**
  `2408b1acef2362143e33c6a61099384600bcdc78624a621c8d387f8e9d0e5c63`.

The proved weighted-multistar theorem strengthens the old two-leaf screen.
Distance-four edges receive weight two and distance-six edges weight one; a
candidate fiber now needs a center of incident weight at least four.

```text
order  principal primes  two-leaf primes  weighted-multistar primes
32     103               18               4
64     2,127             162              67
```

This gives overall compression factors `25.75` and `31.75` from the complete
toy-order principal-prime lists. The strongest observed incident weight was
eight at both orders. The earlier complete screens already proved that these
toy candidate lists contain no `P>=19` row; this pilot measures candidate
compression only.

The result selects weighted degree at least four as the final exact sieve for
CR-001. It does not solve the official-scale algebraic principal-prime
generator, which remains the expensive request's preprocessing gate.

Replay the pinned summary with

```text
tools/ramguard tiny -- python3 experiments/prize_resolution/h3_weighted_multistar_alignment_pilot_check.py
```
