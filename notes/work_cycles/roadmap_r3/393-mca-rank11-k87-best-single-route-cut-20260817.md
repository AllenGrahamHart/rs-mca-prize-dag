## Work cycle 393: K'=87 best-single route cut

### Pins

- starting Codex pin: `c1a3c5123`
- canonical Fable prize pin: `28a62b40060c39c8ee35deaac819f33f18824303`
- upstream main pin: `93fba1be3f3299b0ba4708d88715377bbb656e45`
- relevant upstream PR: `#1170` at K'=86 head `7214947e`
- critical snapshot before DAG changes: 27 `TARGET`, 37 `CONDITIONAL`

### Result: ROUTE CUT

The paired best-single stress wave completed all eight jobs as Modal app
`ap-LHOZ5HAjGEZi9RzlEHSHZH`. Capture SHA-256:
`28384df190292e49aeb22ded3194f83037700654293fe5ba4518ffd2680a5501`.
Primary and independent traversals agree exactly. Offsets 9, 23, and 43
survive; offset 1 is falsified at

```text
m2=27, m3=28, s2=50, s3=49, s4=48, s5=47
case=F23__N4_t2__N5_t0
charges=(32,7),(36,5), high=c6F/c7F/c8F/c9F
```

The best single adjacent edge leaves premium
`41535717484613459403166619514559682376379208865`, exceeding the exact
K'=87 raw-safe leader by
`74818359138015565285572829536920044880164170`. This is the first finite row
where the proved K'=85/K'=86 best-single continuation fails.

### Burn-down

- node/workboard item attacked: local `rate_half_band_crossing_location`, at
  first open rank-nine component row `K'=87`
- DAG status delta: none; no false statement was promoted
- upstream terminal delta: none; `K'=86` remains the last exported prefix
- route delta: a complete best-single wave is blocked by a paired exact
  witness; three route-deciding lanes nevertheless survive
- delta-star bracket movement: none
- new assumptions: none
- next route-deciding action: compute the exact support-disjoint option table
  on the witness, testing the non-overlapping edge set `4+6` before designing
  any broader residual scanner
