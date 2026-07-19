# F3 h=3 conic-chart rank minor certificate

Status: MACHINE-VERIFIED FINITE-FIELD MINOR CERTIFICATE, NOT `RC-RANK`.

This packet strengthens the same-fiber conic-chart rank witness from
`F3_H3_RICH_CURVE_RANK_SAMPLE.md`.  Instead of only recording that the toy
substitution matrix has rank `320`, it exhibits a concrete nonzero
`320 x 320` minor.

## Certificate

Use the same toy row and conic chart:

```text
p=769, H=32, A=5, B=4, D=1,
a=37, b=706, base=(101,333),
Q=1+t+t^2.
```

The conic chart is

```text
U=(298+66t+101t^2)/Q,
V=(333+530t+298t^2)/Q,
W=(101+136t+333t^2)/Q.
```

The coefficient matrix has `581` degree rows and `320=A B^3` monomial columns.
The certificate takes:

```text
rows:    261..580
columns: all monomial columns X^a U^(Hb1) V^(Hb2) W^(Hb3) Q^(H(3(B-1)-b1-b2-b3))
         with 0<=a<5 and 0<=b_i<4.
```

The replay verifies:

```text
determinant mod 769 = 514 != 0.
```

The row/column certificate digest is:

```text
c8ed933836ad696533f73b13a86e71eabce164927a50fc2f8bfd5ce207f92060
```

Therefore this concrete minor proves full coefficient rank for this actual
same-fiber conic-chart point over `F_769`.

## Role

This proves that the rank-good open set is nonempty on the same-fiber conic
chart family in the toy row.  It does not prove the required official-row
avoidance theorem.  The real `RC-RANK` task is still to produce finite-row
minor nonvanishing for the repaired F3 conic-chart images used by the bridge.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_chart_rank_minor_certificate.py
```

Expected digest:

```text
H3_CONIC_CHART_RANK_MINOR_CERTIFICATE_PASS
```
