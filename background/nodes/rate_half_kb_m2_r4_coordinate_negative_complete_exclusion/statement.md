# KoalaBear m2 r4 negative coordinate orientation complete exclusion

- **status:** PROVED
- **scope:** every negative-parity coordinate-order-two component in the
  residual `(m,r,delta)=(2,4,2)` row
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_442_h6_complete_product_exclusion`,
  `rate_half_kb_m2_r4_coordinate_negative_two_loop_433_constrained_complete_product_exclusion`,
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_complete_exclusion`,
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_433_complete_exclusion`,
  and
  `rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_complete_exclusion`
- **consumer:** `rate_half_band_closure`

No negative-parity coordinate-order-two packet exists over the deployed
KoalaBear field.

Indeed, the exact loop-budget gate partitions every such packet into the
five skeletons

```text
profile   loops       multiplicities
(4,4,2)   (0,1,0)     (2,2,0)
(4,4,2)   (1,1,0)     (1,1,1)
(4,3,3)   (0,0,0)     (2,2,1)
(4,3,3)   (1,0,0)     (1,1,2)
(4,3,3)   (1,0,1)     (2,0,1).                  (KBNX-1)
```

The terminal exclusions delete these rows respectively as

```text
one-loop 442, two-loop 442,
zero-loop 433, one-loop 433, two-loop 433.        (KBNX-2)
```

The rows in `(KBNX-1)` are disjoint and exhaustive, so `(KBNX-2)` closes
the whole negative coordinate orientation.

This theorem does not exclude positive coordinate parity, diagonal or
trivial stabilizer orientations, close `(m,r,delta)=(2,4,2)`, move an
owner/payment, close a Prize row, or prove either Prize result.

## Falsifier

A negative coordinate packet outside `(KBNX-1)`, or a complete packet in
one of the five rows despite its terminal exclusion.
