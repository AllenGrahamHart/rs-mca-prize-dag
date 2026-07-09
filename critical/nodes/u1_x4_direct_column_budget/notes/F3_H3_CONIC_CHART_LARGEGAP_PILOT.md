# F3 h=3 conic-chart large-gap pilot

Status: BOUNDED EXACT-RANK PILOT, NOT `RC-RANK`.

This packet refines the h=3 exact-profile rank target after the conic-chart
degree-space guardrail.  It does not prove a rank theorem.  It records that the
known same-fiber conic chart behaves much better once the `H/A` gap approaches
the official exact-profile range.

## Setup

The replay uses the same actual same-fiber conic chart as
`F3_H3_CONIC_CHART_DEGREE_SPACE_GUARD.md`:

```text
p=769, a=37, b=706, base=(101,333).
```

It checks three nearby boxes:

```text
A=5, B=4, H in {20,24,32}.
```

This is deliberately small so the replay stays below the local 60-second
policy.

## Replayed Rows

```text
A=5 B=4 H=20: rank=293 target=320 deficit=27  H/A=4
A=5 B=4 H=24: rank=319 target=320 deficit=1   H/A=24/5
A=5 B=4 H=32: rank=320 target=320 deficit=0   H/A=32/5
```

The official exact-profile boxes have a larger gap:

```text
min official H/A = 8192/1362 = 4096/681, at s=13.
```

The exact-profile route can tolerate any uniform bounded deficit

```text
Delta <= 1847.
```

Thus the known toy conic-chart large-gap deficits are far inside the official
bounded-deficit budget.  This supports the current theorem target:

```text
prove finite-row conic-chart rank >= (L+1)-Delta
with Delta <= 1847 on the official exact-profile boxes.
```

It does not prove that target.  It only sharpens why the bounded-deficit route
is plausible and why automatic degree-space fullness is stronger than needed.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_chart_largegap_pilot.py
```

Expected digest:

```text
H3_CONIC_CHART_LARGEGAP_PILOT_PASS
```
