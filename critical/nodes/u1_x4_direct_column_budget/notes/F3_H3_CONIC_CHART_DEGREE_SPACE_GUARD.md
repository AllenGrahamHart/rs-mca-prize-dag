# F3 h=3 conic-chart degree-space guardrail

Status: MACHINE-VERIFIED GUARDRAIL, NOT `RC-RANK`.

This packet prevents an overstrong next theorem statement.  The conic-chart
rank-good minor certificate proves one full-rank toy box, but the same
same-fiber conic chart does **not** always have full degree-space rank.

## Test Chart

The replay uses the same actual bridge-family chart:

```text
p=769, a=37, b=706, base=(101,333),
Q=1+t+t^2,
U=(298+66t+101t^2)/Q,
V=(333+530t+298t^2)/Q,
W=(101+136t+333t^2)/Q.
```

For each box it compares the exact rank with the naive fullness target

```text
min(A B^3, L+1),       L=(A-1)+6H(B-1).
```

## Results

```text
A  B   H   rank  min(AB^3,L+1)  deficit
5  4  32    320             320        0
5  4  16    247             293       46
5  4   8    137             149       12
5  4   4     74              77        3
5  6   4    122             125        3
12 5   4    108             108        0
16 4   8    160             160        0
```

Thus degree-space fullness can hold or fail depending on the box.  The
failure is not the constant-ratio collapse; it happens on the same
nondegenerate conic chart that has a full-rank `A=5,B=4,H=32` minor.

## Consequence

The future h=3 rank theorem should not be phrased as automatic full
degree-space rank for all repaired conic charts.  The correct target remains
the exact finite-row inequality actually consumed by the bridge:

```text
rank(S_Z) > (DA + 6D(D-1)) * capacity.
```

Equivalently, prove or exhibit enough row-specific minors for the official
exact-profile boxes.  The official boxes have positive degree-space room above
the exact condition count, but this guardrail shows that the room cannot be
ignored.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_chart_degree_space_guard.py
```

Expected digest:

```text
H3_CONIC_CHART_DEGREE_SPACE_GUARD_PASS
```
