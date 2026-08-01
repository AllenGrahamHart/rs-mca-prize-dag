# KoalaBear m2 r4 coordinate negative one-loop 442 nonloop-singleton opposite-pair exclusion

- **status:** PROVED
- **scope:** the one-loop `(4,4,2)` common-`K` matching orbit in which an
  `AC` record is the singleton, the two `AB` records form one antipodal
  source pair, and the loop is paired with the other `AC` record
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate` and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_product_q_weld`
- **consumer:** `rate_half_band_closure`

Normalize one cell by

```text
(x_L,x_AB+,x_AB-,x_AC+,x_AC-)=(1,r,epsilon_2*i*r,t,epsilon_1*i),
i^2=-1,                  epsilon_1,epsilon_2 in {+1,-1}. (KB41O-1)
```

Its labels and products are

```text
(1,r^2,-r^2,t^2,-1),       (-b^2,b,-b,c,-c).     (KB41O-2)
```

For every one of the four relative root-sign choices, the product equations
and one of the two one-loop q welds contradict the label and target guards.
Hence this entire matching orbit is empty.  Changing the sign of target
representative `C` exchanges the two cells, so this deletes atlas cells
`11` and `14` and every root-sign class.

This theorem does not classify the other three nonloop-singleton matching
orbits, impose outside products, handle one-loop 433 or zero-loop, close the
coordinate orientation, close a row, or prove either Prize result.

## Falsifier

An admissible common-`K` solution of `(KB41O-1)--(KB41O-2)` for any of the
four sign choices, or a sign class not covered by the displayed
normalization and the `C` representative swap.
