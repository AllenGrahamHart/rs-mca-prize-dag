## Work cycle 386: K'=85 raw-threshold envelope

### Pins

- starting Codex pin: `769fc9994d54909841fd4326be13927fab28c87c`
- preregistered source pin: `2a8728f9e541cb15eeb3cc5854b3d16a4e694ed4`
- canonical Fable prize pin: `28a62b40060c39c8ee35deaac819f33f18824303`
- upstream main pin: `93fba1be3f3299b0ba4708d88715377bbb656e45`
- relevant upstream PR: `#1170` (proved prefix through K'=84)
- critical snapshot before DAG changes: 27 `TARGET`, 37 `CONDITIONAL`

### Result: NARROWED

Two exact implementations classified every pre-geometry unit in all 74
positive support-2/3 offset lanes at K'=85. Modal app
`ap-rTfQtYZuTdgjfk5IWhal5W` passed all 148 jobs in about 27 seconds. Its
capture SHA-256 is
`5832710721306c16477523b02303fb6f45fb293f6ea53c71e26bad2a9babac13`.
The merger certified 16,028,400 source units and 112,198,800 raw rows per
implementation with exact profile and classification-digest agreement.

The exact partition is:

```text
raw-safe units       15,696,867
raw-unsafe units        331,533
unsafe offsets              1..41
fully safe offsets          42..74
```

The global raw-safe leader occurs at offset 11 and branch

```text
s2=56/s3=45/s4=58/s5=37/offset11/c6F/c7F/c8F/c9F
```

with premium
`41412868016209776721228891386909879523306833354` and positive ceiling
margin `1793645398692419426975603430807602228515`.

### Burn-down

- node/workboard item attacked: local `rate_half_band_crossing_location`,
  through the first open rank-nine component row K'=85
- DAG status delta: none; K'=85 remains unproved
- upstream terminal delta: none; K'=84 remains the last exportable prefix
- route delta: the unsampled-offset question is closed exactly; the remaining
  row obligation is a finite 331,533-unit post-carrier domination theorem
- delta-star bracket movement: none
- new assumptions: none
- live compute request: test fixed-union-only domination against the offset-11
  leader before pricing any adjacent-support edge
- next route-deciding action: falsify the fixed-union-only domination on
  offsets 11, 1, 23, and 41; if it survives, extend its exact certificate,
  otherwise retain the first witness and identify the one missing adjacent
  charge
