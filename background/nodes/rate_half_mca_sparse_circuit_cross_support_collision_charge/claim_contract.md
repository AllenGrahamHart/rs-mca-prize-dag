# Claim contract

- Source supports: `c=2,3,4,5`.
- Target supports: `2<=d<=9`, subject to `c+d<=11`.
- Exact nonempty source defects: `0<=s<q`.
- Source carrier size: `q+c-1-s`.
- Positive intersection: `12-c-d`.
- Target outside budget: `s+d-1`.
- Outside target-circuit stratum: divide by the exact number `j` of
  external deletion exposures.
- Incidence multiplier: `C(m-d,11-d)`.
- No target cap is inferred from the empty source stratum `s=q`.
