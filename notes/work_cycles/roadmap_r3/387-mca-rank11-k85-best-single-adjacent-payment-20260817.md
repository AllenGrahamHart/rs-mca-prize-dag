## Work cycle 387: K'=85 best-single adjacent payment

### Pins

- starting Codex pin: `197c7d3e98d477568c784a62289365d9b4a3a326`
- canonical Fable prize pin: `28a62b40060c39c8ee35deaac819f33f18824303`
- upstream main pin: `93fba1be3f3299b0ba4708d88715377bbb656e45`
- relevant upstream PR: `#1170` (proved prefix through K'=84)
- critical snapshot before DAG changes: 27 `TARGET`, 37 `CONDITIONAL`

### Result: PROVED

Four progressively weaker candidate payments were attacked before the full
wave. Fixed-union-only and edge-4-only domination were falsified by exact
witnesses; witness replay identified adjacent edges 4 and 6 as real but
case-dependent charges. This led to the honest statement: each residual
profile may use its best individually valid single adjacent edge, without
composing overlapping edges.

The paired exhaustive wave completed as Modal app
`ap-avKuaBEl3bNsvVug235bXS`. Its capture SHA-256 is
`a2a47722b66ff40ed83b44c47dc725b341700ffc2c9653a61e63f7dff1fedfa8`.
Primary and independent traversals agree on all 41 residual offsets,
12,788,064 source units, 331,533 raw-unsafe units, and 49,090,656
deduplicated carrier profiles per implementation. Every profile is at most
the exact offset-11 leader

```text
P_85=41412868016209776721228891386909879523306833354.
```

Together with the paired ordinary lane and complete raw-threshold envelope,
this certifies the whole `K'=85` carrier frontier. Modal app
`ap-9R6TUWXTLwS11AiqMsAem5` then gave exact safe-ceiling margin
`1793645398692419426975603430807602228515` and positive component gap

```text
8967598503742781003071510733325918643075973211834024001.
```

The compact node
`rate_half_mca_rank11_k85_best_single_adjacent_payment` is therefore
`PROVED`, extending the finite rank-nine closed prefix to `K'=10..85`.

### Burn-down

- node/workboard item attacked: local `rate_half_band_crossing_location`,
  through the first open rank-nine component row `K'=85`
- DAG status delta: one new proved background certificate; critical status
  labels unchanged
- finite-row delta: closed prefix advanced from `10..84` to `10..85`
- upstream terminal delta: none until PR `#1170` is extended and accepted
- route delta: raw safety alone is insufficient, but one individually valid
  adjacent edge pays every residual profile at `K'=85`
- delta-star bracket movement: none
- new assumptions: none
- first open finite row: `K'=86`
- next route-deciding action: export the compact K'=85 packet upstream, then
  test whether `K'=86` admits the same best-single theorem or exposes the
  predicted adjacent-support crossing
