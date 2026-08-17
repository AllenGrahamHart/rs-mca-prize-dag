## Work cycle 399: raw-clipped adjacent-support theorem

### Pins

- starting Codex pin: `b30896e0d`
- canonical Fable prize pin: `28a62b40060c39c8ee35deaac819f33f18824303`
- upstream main pin: `93fba1be3f3299b0ba4708d88715377bbb656e45`
- relevant upstream PR: `#1170` at K'=86 head `7214947e`
- critical snapshot before DAG changes: 27 `TARGET`, 37 `CONDITIONAL`

### Result: PROVED

The new background node
`rate_half_mca_sparse_circuit_raw_clipped_adjacent_support_coupling` proves a
generic refinement of the fixed-union adjacent-support theorem. Independent
raw selected-incidence caps on supports `d` and `d+1` may be imposed inside
the exact fixed-union stratum polytope before the weighted objective is
maximized.

The proof is a fractional-knapsack exchange argument. Fixing total support
`d` fills uncoupled strata first and then uses increasing loss ratios
`b_i/a_i`; fixing support `d+1` gives the reverse dual order `a_i/b_i`.
Both exact rational verifiers reconstruct the K'=87 `(u,g,d)=(34,6,5)`
specialization and cap

```text
14207926136094898913594751174330524101924656533.
```

The theorem explicitly floors selected-incidence caps by their extension
factors and forbids composition on overlapping support pairs.

### Burn-down

- node/workboard item attacked: local `rate_half_band_crossing_location`
- DAG status delta: one new background `PROVED` theorem; critical-folder
  status counts unchanged
- graph replay: 2,571 nodes, 7,667 edges; manifest and full prize-DAG checks
  pass under the 256 MB RAM guard
- upstream terminal delta: none; `K'=86` remains the last exported prefix
- route delta: the first K'=87 support-disjoint witness now has a proved,
  reusable repair rather than a numerical-only observation
- delta-star bracket movement: none
- new assumptions: none
- next route-deciding action: build paired K'=87 adapters using the clipped
  adjacent cap and exhaust offset 1 before launching any full-row wave
