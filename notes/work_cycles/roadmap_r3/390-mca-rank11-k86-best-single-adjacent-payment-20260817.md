## Work cycle 390: K'=86 best-single adjacent payment

### Pins

- starting Codex pin: `236ef2bcb`
- canonical Fable prize pin: `28a62b40060c39c8ee35deaac819f33f18824303`
- upstream main pin: `93fba1be3f3299b0ba4708d88715377bbb656e45`
- relevant upstream PR: `#1170` at K'=85 head `7356a104`
- critical snapshot before DAG changes: 27 `TARGET`, 37 `CONDITIONAL`

### Result: PROVED

The K'=86 raw envelope left exactly 415,413 unsafe units on offsets 1..42.
An eight-job adversarial stress wave survived offsets 1, 23, 32, and 42 with
4,954,135 carrier profiles per implementation. The complete paired wave then
passed all 84 jobs as Modal app `ap-HSdSkI0KYmWfnz0jL0Bron`. Capture SHA-256:
`bc67b9fa9ffa6b386d5d5f9e053e2d5a99a8451f2e9ae8d03c0095cc6f867349`.

```text
source units per implementation       13,571,481
raw-unsafe units per implementation      415,413
carrier profiles per implementation   62,159,220
completion premium
  41436891148468120556440841127823744176664445997
safe-ceiling margin
  2429142732593969226237923721701123878841
```

The broader route pilot had been incomplete in an unrelated offset-23 audit
job. A dedicated checker now verifies the two completed ordinary jobs inside
that pinned capture: 504,660 source units, 3,532,620 raw rows, and equal
2,718,499-row geometry traversals, all below the global leader.

Modal app `ap-3mwC5dZ9yYxOTcOJx9JygE` independently reconstructed the exact
component payment. Capture SHA-256:
`252d9dfa3f4c6e819a706a54e437aae1337907473e3dd3113bff460764007f3e`.
The exact component gap is

```text
12144862496270285686198005257330878943217549361781518735>0.
```

The compact node
`rate_half_mca_rank11_k86_best_single_adjacent_payment` is therefore
`PROVED`, extending the finite rank-nine prefix from `10..85` to `10..86`.

### Burn-down

- node/workboard item attacked: local `rate_half_band_crossing_location`,
  through the first open rank-nine component row `K'=86`
- DAG status delta: one new background `PROVED` node; critical-folder status
  counts unchanged
- upstream terminal delta: none yet; `K'=85` remains the last exported prefix
- route delta: the K'=86 finite row is closed without new assumptions
- delta-star bracket movement: none
- next route-deciding action: export K'=86 onto upstream PR `#1170`, then
  probe `K'=87` with the same raw-threshold-first stopping discipline
