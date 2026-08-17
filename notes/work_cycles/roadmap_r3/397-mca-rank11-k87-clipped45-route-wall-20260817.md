## Work cycle 397: K'=87 clipped-45 route wall

### Pins

- starting Codex pin: `c45067434`
- canonical Fable prize pin: `28a62b40060c39c8ee35deaac819f33f18824303`
- upstream main pin: `93fba1be3f3299b0ba4708d88715377bbb656e45`
- relevant upstream PR: `#1170` at K'=86 head `7214947e`
- critical snapshot before DAG changes: 27 `TARGET`, 37 `CONDITIONAL`

### Result: ROUTE WALL

Modal app `ap-cCC7w2ZcDACsgqKNJS19Ij` solved the `(36,5)` support-4/5
fixed-union LP with the witness's raw global support caps imposed before
aggregation. Capture SHA-256:
`4f3bef9931e692f12b85432719730f433fcb0603cf894982c06a5e9458895120`.
The two exact allocation orders agree, but the resulting repaired premium
still exceeds the K'=87 leader by
`527046372060980182985446452501713227668364930`.

### Burn-down

- node/workboard item attacked: local `rate_half_band_crossing_location`, at
  first open rank-nine component row `K'=87`
- DAG status delta: none; an insufficient valid refinement was not promoted
- upstream terminal delta: none; `K'=86` remains the last exported prefix
- route delta: pre-aggregation raw clipping strengthens support 4/5 but not
  enough; the best extant witness payment is the support-5/6 edge
- delta-star bracket movement: none
- new assumptions: none
- next route-deciding action: apply the exact clipped-stratum optimization to
  support 5/6 on the witness's `(34,6)` carrier
