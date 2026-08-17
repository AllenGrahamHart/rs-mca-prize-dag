## Work cycle 398: K'=87 clipped-56 witness repair

### Pins

- starting Codex pin: `7317391d9`
- canonical Fable prize pin: `28a62b40060c39c8ee35deaac819f33f18824303`
- upstream main pin: `93fba1be3f3299b0ba4708d88715377bbb656e45`
- relevant upstream PR: `#1170` at K'=86 head `7214947e`
- critical snapshot before DAG changes: 27 `TARGET`, 37 `CONDITIONAL`

### Result: NARROWED

Modal app `ap-0M46E2HegLDfuwCNvdJTUm` solved the `(34,6)` support-5/6
fixed-union LP after imposing the witness's raw support caps before
aggregation. Capture SHA-256:
`3f5c2073ae746ba1c546fbc49afa09941280438c94989b9f614bf812a8f42eab`.
The two exact allocation orders agree.

The resulting cap repairs the support-disjoint counterexample with positive
margin `1929093338019885320682606421709317172772593344`. The raw support-5
cap is active, proving that the refinement supplies new arithmetic strength.

### Burn-down

- node/workboard item attacked: local `rate_half_band_crossing_location`, at
  first open rank-nine component row `K'=87`
- DAG status delta: none; one witness is repaired, not the full lane
- upstream terminal delta: none; `K'=86` remains the last exported prefix
- route delta: a generic-looking pre-aggregation refinement now has positive
  witness margin after four exact route cuts
- delta-star bracket movement: none
- new assumptions: none
- next route-deciding action: prove and package the generic raw-clipped
  adjacent-support theorem, then exhaust offset 1 with paired implementations
