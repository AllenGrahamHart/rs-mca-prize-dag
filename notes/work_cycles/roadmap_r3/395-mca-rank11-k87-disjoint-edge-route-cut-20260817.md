## Work cycle 395: K'=87 disjoint-edge route cut

### Pins

- starting Codex pin: `75c4e2e90`
- canonical Fable prize pin: `28a62b40060c39c8ee35deaac819f33f18824303`
- upstream main pin: `93fba1be3f3299b0ba4708d88715377bbb656e45`
- relevant upstream PR: `#1170` at K'=86 head `7214947e`
- critical snapshot before DAG changes: 27 `TARGET`, 37 `CONDITIONAL`

### Result: ROUTE CUT

The paired offset-1 support-disjoint falsifier completed as Modal app
`ap-cJPrOXXEvVBCRydRzokVWK`. Capture SHA-256:
`dcc663d48ea02daa4267f9a13b4af6889f66d8af9738e35af96df4e42c400e23`.
Primary and independent traversals agree exactly on the first obstruction:

```text
m2=28, m3=29, s2=49, s3=48, s4=48, s5=47
case=F23__N4_t0__N5_t0
charges=(34,6),(36,5), high=c6F/c7F/c8F/c9F
```

The only available adjacent edges are 4 and 5. They overlap at support 5,
so the proved disjoint optimizer can use at most one. Its best price exceeds
the K'=87 leader by
`28875175078457354958072343663520239143833856`.

### Burn-down

- node/workboard item attacked: local `rate_half_band_crossing_location`, at
  first open rank-nine component row `K'=87`
- DAG status delta: none; no overlapping charge was assumed
- upstream terminal delta: none; `K'=86` remains the last exported prefix
- route delta: both best-single and support-disjoint continuations are now
  cut by paired exact witnesses
- delta-star bracket movement: none
- new assumptions: none
- next route-deciding action: derive and test a simultaneous support-`4/5/6`
  fixed-union inequality, or strengthen one of the two adjacent-pair caps,
  before any additional row-wide wave
