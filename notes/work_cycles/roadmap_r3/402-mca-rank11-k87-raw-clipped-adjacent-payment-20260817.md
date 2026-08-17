## Work cycle 402: K'=87 raw-clipped adjacent payment

### Pins

- starting Codex pin: `2f3046d85`
- canonical Fable prize pin: `28a62b40060c39c8ee35deaac819f33f18824303`
- upstream main pin: `93fba1be3f3299b0ba4708d88715377bbb656e45`
- relevant upstream PR: `#1170` at K'=86 head `7214947e`
- critical snapshot before DAG changes: 27 `TARGET`, 37 `CONDITIONAL`

### Result: PROVED

Fresh paired ordinary traversals agree on 542,840 source units, 3,799,880
raw rows, 4,385 expanded units, and 2,940,875 geometry rows per
implementation. Modal app `ap-t1IWAsyDidGwq0ZwwYO6yI`; capture SHA-256:
`06a550c1f65be3c2a7c4d96590188f5de6ca792c1f87e638f2fa7d5163b43519`.
The ordinary premium is strictly below the nonordinary leader.

The complete paired clipped wave passes all 43 unsafe offsets, 511,677 unsafe
units, and 77,179,660 carrier profiles per implementation. Its canonical
merged capture SHA-256 is
`6f8064320850e0009c18c967e2b61ec5b4d77c51e1c2afb4bee6fc41921e5cd8`.
Together with the raw-safe population, it proves completion premium

```text
41460899125475443837881046685022762331499044695.
```

Modal app `ap-JAw6W5GHktZA9TXLxcpMUY` reconstructed the exact component
payment; capture SHA-256:
`883f659486162495750adbc80c97d3224cdae6b3bdebf3429492a33189d95312`.
The exact component gap is

```text
77712391681585193939443710876895639001790676368706144901>0.
```

The compact node
`rate_half_mca_rank11_k87_raw_clipped_adjacent_payment` is therefore
`PROVED`, extending the finite rank-nine prefix from `10..86` to `10..87`.

### Burn-down

- node/workboard item attacked: local `rate_half_band_crossing_location`,
  through the first open rank-nine component row `K'=87`
- DAG status delta: one new background `PROVED` node; critical-folder status
  counts unchanged
- upstream terminal delta: none yet; upstream PR `#1170` still ends at K'=86
- route delta: the K'=87 finite row is closed without new assumptions and
  without composing overlapping adjacent-support bounds
- delta-star bracket movement: none
- new assumptions: none
- next route-deciding action: export K'=87 onto upstream PR `#1170`, then
  test `K'=88` with the same raw-threshold-first stopping discipline
