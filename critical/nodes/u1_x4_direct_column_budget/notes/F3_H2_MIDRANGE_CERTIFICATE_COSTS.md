# F3 h=2 finite-midrange certificate-cost table

Status: PROVED ARITHMETIC COST TABLE, NOT A CERTIFICATE.

This is a T3 constant-campaign packet from
`notes/codex_briefs/F3_FLIP_20260708.md`.  After the optimized in-house h=2
chain, the only official power-of-two rows not covered by the in-house theorem
alone are `2^13` through `2^22`.  This packet quantifies the exact ordered-pair
work for direct h=2 energy certificates on those rows.

## Pre-registration

Question:

```text
Which official power-of-two h=2 rows remain below the optimized in-house
crossover, and which are plausibly certificate-feasible under a fixed
ordered-pair shard model?
```

Success criterion:

- compute the optimized in-house crossover exactly;
- list every official power-of-two row below it;
- estimate exact ordered-difference census cost using an explicit shard unit;
- separate feasible rows from residual rows without claiming an unrun
  certificate.

Failure criterion:

- the table misses any official power in `[2^13, 2^41]`;
- the shard model is implicit or confused with a measured runtime certificate.

## Inputs

From `F3_H2_RICH_COSET_OPTIMIZED.md`, the optimized in-house chain gives

```text
T_2 < h^3    for integer h >= 7,639,006.
```

Thus official powers `2^23` through `2^41` are theorem-covered, while
`2^13` through `2^22` are the finite in-house midrange.

For a direct h=2 exact energy census, the simple ordered-difference pass has

```text
h(h-1)
```

nonzero ordered differences.  This table uses the explicit planning shard

```text
S = 2^26 ordered differences
```

which is exactly the work size of the first official row `h = 2^13` up to the
minus-one factor.  This is a work-unit model, not a Modal timing claim.

## Result

Under the policy threshold `< 2000` shards:

```text
feasible exact-census rows: 2^13, 2^14, 2^15, 2^16, 2^17, 2^18
residual midrange rows:     2^19, 2^20, 2^21, 2^22
theorem-covered rows:       2^23 through 2^41
```

The external Cochrane--Pinner import still closes all h=2 rows.  This table is
only the in-house finite-midrange accounting requested by T3.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_midrange_certificate_costs.py
```

Expected digest:

```text
H2_MIDRANGE_CERTIFICATE_COSTS_PASS
```
