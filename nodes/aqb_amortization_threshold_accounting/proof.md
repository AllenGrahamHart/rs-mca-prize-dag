# proof: aqb_amortization_threshold_accounting

The proved node `aqb_deficit_arithmetic` certifies the worst finite deficit at
`Q=256`:

```text
B_I(256) =
d*256 - 40 - log2 C(2^40, 2^39+d)
```

with

```text
B_I(256) < 429,645,547 bits.
```

More precisely, the Robbins-interval verifier gives

```text
429,645,547 - B_I(256) > 0.2265 bits.
```

The deficit is affine increasing in `Q`, so this is the worst admissible case.
Therefore any averaged family whose net shared entropy gain is certified to be
at least

```text
429,645,547 bits
```

clears the finite deficit in every admissible case covered by the AQB-I
statement. This is exactly the threshold-accounting implication used by
`aqb_box_charge_amortization`.
