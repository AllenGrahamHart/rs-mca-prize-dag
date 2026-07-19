# F3 h=3 conic-chart official-ratio deficit pilot

Status: SMALL MACHINE-VERIFIED ROUTE PILOT, NOT `RC-RANK`.

This packet checks a few small boxes whose ratio `A/H` is closer to the first
official exact-profile row than the earlier toy full-rank certificate.  It is
not a broad sweep and it does not prove a theorem.

## Result

Using the same same-fiber conic chart over `F_769`,

```text
a=37, b=706, base=(101,333),
```

the replay checks:

```text
A  B   H   rank  min(AB^3,L+1)  deficit
2  4   8    118             128       10
2  6   8    214             242       28
2  8   8    310             338       28
3  4  16    192             192        0
3  6  16    414             483       69
4  4  24    256             256        0
```

The point is qualitative: degree-space deficits are visible even in
official-ratio toy boxes, so the exact-profile `RC-RANK` route should be
attacked as a genuine finite-row minor/lower-bound theorem.  The bounded
deficit allowance `Delta <= 1847` remains useful, but it is not automatic from
dimension counting or from the single full-rank toy minor.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_chart_official_ratio_deficit_pilot.py
```

Expected digest:

```text
H3_CONIC_CHART_OFFICIAL_RATIO_DEFICIT_PILOT_PASS
```
