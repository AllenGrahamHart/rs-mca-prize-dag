## Work cycle 392: K'=87 raw-threshold envelope

### Pins

- starting Codex pin: `fdc4a2718`
- canonical Fable prize pin: `28a62b40060c39c8ee35deaac819f33f18824303`
- upstream main pin: `93fba1be3f3299b0ba4708d88715377bbb656e45`
- relevant upstream PR: `#1170` at K'=86 head `7214947e`
- critical snapshot before DAG changes: 27 `TARGET`, 37 `CONDITIONAL`

### Result: NARROWED

The preregistered complete raw-threshold wave passed all 152 jobs as Modal
app `ap-xwOdMdTBRKtC2aIHtpRSw0`. Capture SHA-256:
`2722d7811cf29e425bd67fd49a46f586efe2f21c0dda698e369dcfe4fd48b449`.
Primary and independent traversals agree on all 76 offsets, all
17,801,784 source units, and all 124,612,488 raw rows per implementation.

```text
raw-safe units       17,290,107
raw-unsafe units        511,677
unsafe offsets              1..43
fully safe offsets          44..76
```

The global raw-safe leader occurs at offset 9 and branch

```text
s2=55/s3=46/s4=37/s5=30/offset9/c6F/c7F/c8F/c9F
```

with premium
`41460899125475443837881046685022762331499044695`. The exact safe ceiling is
`41460914669043067085305042221812436226076443389`, leaving positive margin
`15543567623247423995536789673894577398694`.

### Burn-down

- node/workboard item attacked: local `rate_half_band_crossing_location`,
  through the first open rank-nine component row `K'=87`
- DAG status delta: none; `K'=87` remains unproved
- upstream terminal delta: none; `K'=86` remains the last exported prefix
- route delta: all raw-offset uncertainty is removed; the row is reduced to
  a finite 511,677-unit post-carrier domination theorem
- delta-star bracket movement: none
- new assumptions: none
- next route-deciding action: adapt the K'=86 best-single theorem to offsets
  `1..43`, stress offsets `1`, `23`, `9`, and `43`, and run the complete
  paired residual wave only if all four survive
