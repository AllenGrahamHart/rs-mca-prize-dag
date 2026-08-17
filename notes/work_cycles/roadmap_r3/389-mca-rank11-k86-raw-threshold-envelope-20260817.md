## Work cycle 389: K'=86 raw-threshold envelope

### Pins

- starting Codex pin: `56cce936a0cdc8bc49cfda03f3e10e026613f1d2`
- canonical Fable prize pin: `28a62b40060c39c8ee35deaac819f33f18824303`
- upstream main pin: `93fba1be3f3299b0ba4708d88715377bbb656e45`
- relevant upstream PR: `#1170` at K'=85 head `7356a104`
- critical snapshot before DAG changes: 27 `TARGET`, 37 `CONDITIONAL`

### Result: NARROWED

The initial full-geometry pilot was formally incomplete: nine jobs finished,
but the independent offset-23 job exceeded its 645-second wall. Four paired
lanes agreed and were safe. Rather than fund a longer redundant geometry
run, the route switched to the cheaper complete raw-threshold classification.

Modal app `ap-kjz4PvurdW9cunGO3pse1N` passed all 150 raw jobs. Its capture
SHA-256 is
`7aa3c934e610aa717ba25b8b7acf424c0f59ad068ec294eac5b448d9abb81612`.
Primary and independent traversals agree on 16,897,650 source units and
118,283,550 raw rows per implementation.

```text
raw-safe units       16,482,237
raw-unsafe units        415,413
unsafe offsets              1..42
fully safe offsets          43..75
```

The global raw-safe leader occurs at offset 32 and branch

```text
s2=73/s3=41/s4=39/s5=57/offset32/c6F/c7F/c8F/c9F
```

with premium
`41436891148468120556440841127823744176664445997` and positive ceiling
margin `2429142732593969226237923721701123878841`.

### Burn-down

- node/workboard item attacked: local `rate_half_band_crossing_location`,
  through the first open rank-nine component row `K'=86`
- DAG status delta: none; `K'=86` remains unproved
- upstream terminal delta: none; `K'=85` remains the last exportable prefix
- route delta: all unsampled-offset uncertainty is removed; the remaining
  row obligation is a finite 415,413-unit post-carrier domination theorem
- delta-star bracket movement: none
- new assumptions: none
- next route-deciding action: adapt the K'=85 best-single residual scanner
  to offsets `1..42`, first stress the likely leaders, and launch a complete
  paired residual wave only if the statement survives
