# Cycle 478: multi-anchor pencil synchronization

## Result: PROVED per-type synchronization

Re-base the triple-owner packet at any pair type with at least 29 records.
The four-dimensional component span still needs at most four secondary types,
so the anchor packet size is one of 29, 26, 23, or 20. Fixed supports and a
one-swap star then give the exact dichotomy:

```text
one packet has chi>=2299571,
or all records of that pair type lie in one rational exception pencil.
```

This is per-type synchronization; different pair types may retain different
pencils.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +3 edges
critical status delta: none
route delta: fixed-pencil caps become summable over first-owned pair types
new assumptions: none
next action: exact class ledger
```
