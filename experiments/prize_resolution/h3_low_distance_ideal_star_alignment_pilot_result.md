# H3 low-distance ideal-star alignment pilot

- **status:** EXPERIMENTAL route evidence; no theorem promotion.
- **Modal app:** `ap-InR5xZAak4rOrjhrEUWIIZ`.
- **resources:** two sequential functions, one physical CPU, 1 GiB RAM, and a
  120-second hard timeout each.
- **observed function time:** `0.383` seconds at `n=32` and `14.007` seconds at
  `n=64`.
- **campaign cost cap:** `$0.10`; published-rate requested-resource cost for
  the completed function time is below `$0.001`.
- **result hash:**
  `6e097c0f7f910be76d09ed4a5557de2cd5ee3aeddcdd01935275b8f16a131a6b`.

For each relevant prime from the complete principal-norm census, the screen
fixed one primitive `n`th root modulo `p` and grouped all
squared-norm-at-most-three shifted products by their actual finite-field
value. Galois invariance makes one primitive root complete. A prime survives
exactly when a fiber contains a center with two distance-at-most-six leaves.
This tests prime-ideal alignment without enumerating rooted stars or computing
Smith normal forms.

```text
order   principal primes   aligned ideal-star primes   compression
32      103                18                          5.72x
64      2,127              162                         13.13x
```

The complete screens found maximum ordered product-fiber sizes `10` and `14`,
respectively. Thus neither toy order has a `P>=19` row among the input primes;
`X_18=0` throughout and there are no C36' violations. This is evidence only,
because official H3 starts at `n=8192`.

The contrast with the preceding `103 -> 103` and `2,127 -> 2,127` rational
gcd screen is decisive: the common degree-one prime ideal carries genuine
compression. The selected route is exact prime-ideal alignment coupled to an
algebraic candidate-prime/template generator. A larger raw star fleet is not
selected.

Replay the pinned summary checks with

```text
tools/ramguard tiny -- python3 experiments/prize_resolution/h3_low_distance_ideal_star_alignment_pilot_check.py
```
