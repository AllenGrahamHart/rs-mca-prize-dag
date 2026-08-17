## Work cycle 396: K'=87 joint-456 route wall

### Pins

- starting Codex pin: `a927ea5d9`
- canonical Fable prize pin: `28a62b40060c39c8ee35deaac819f33f18824303`
- upstream main pin: `93fba1be3f3299b0ba4708d88715377bbb656e45`
- relevant upstream PR: `#1170` at K'=86 head `7214947e`
- critical snapshot before DAG changes: 27 `TARGET`, 37 `CONDITIONAL`

### Result: ROUTE WALL

The simultaneous support-`4/5/6` LP probe completed as Modal app
`ap-D2TbRHCVUrcU61tRsOC4we`. Capture SHA-256:
`e7a5bd7c42cf067f377aac6176d75c887f371c1c019b3e33fc9ee4bb2eb6e76f`.
Two exact rational implementations agree on every stratum and on cap
`26934334803635047410267405026838894905450545600`.

The consequence is valid but insufficient. It leaves the obstruction above
the K'=87 leader by
`861283046046284527325636787894941163714537850`, and is weaker here than
the strongest existing adjacent-pair option.

### Burn-down

- node/workboard item attacked: local `rate_half_band_crossing_location`, at
  first open rank-nine component row `K'=87`
- DAG status delta: none; no insufficient inequality was promoted
- upstream terminal delta: none; `K'=86` remains the last exported prefix
- route delta: simple simultaneous use of the two adjacent inequalities is
  proved arithmetically insufficient on the exact wall
- delta-star bracket movement: none
- new assumptions: none
- next route-deciding action: solve the support-`4/5` fixed-union stratum LP
  with the witness's global raw support caps imposed before aggregation; if
  this also fails, return to the nested-carrier flag geometry
