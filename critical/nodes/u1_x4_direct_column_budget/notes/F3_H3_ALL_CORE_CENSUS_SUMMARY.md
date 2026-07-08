# F3 h=3 all-core census summary (Terminal C)

Status: MACHINE-VERIFIED AGGREGATE.

## Scope

This aggregates one complete oriented `B`-slice for each of the `91`
affine/Galois orbits of the first h=3 core in `Z/96Z`.

It is the complete core-by-core Terminal C census in the sense banked by
`F3_H3_CORE_ORBIT_COUNT.md`: core representatives `(0,1,k)`,
`2 <= k <= 92`, with all disjoint `B` triples for each core.

This is not a Burnside-deduplicated unordered pair-orbit table.  If the
consumer needs the exact affine/Galois pair-orbit rate, the 720 actual
activation entries in the JSON are the input to that final deduplication
layer.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_all_core_census_summary.py
```

Expected digest:

```text
H3_ALL_CORE_CENSUS_SUMMARY_DONE
```

## Result

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_all_core_census_summary.py
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_all_core_census_summary.json
```

Summary:

```text
TOTAL core_types=91 oriented_shapes=11808706 norm_exceptions=106250 activation_exceptions=720
RATES norm=0.8998% activation=0.0061%
H3_ALL_CORE_CENSUS_SUMMARY_DONE
```

The full activation-exception list is in the JSON.  The highest-activation
core types are:

```text
(0, 1, 24): 67 / 129766
(0, 1, 25): 67 / 129766
(0, 1, 72): 67 / 129766
(0, 1, 73): 67 / 129766
(0, 1, 2):  44 / 129766
(0, 1, 48): 37 / 129766
```

The most common activation primes in the oriented exception list begin:

```text
p=37633: 92
p=18913: 40
p=30817: 40
p=12289: 38
p=10177: 34
```

Interpretation: actual common-root activation is very sparse in the complete
oriented core-slice census: `720 / 11808706 = 0.0061%`.  The rational
norm-exception filter is about `0.8998%`, so the common-root test removes the
overwhelming majority of rational norm coincidences.
