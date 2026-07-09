# F3 h=3 conic six-A threshold target

Status: THRESHOLD GUARDRAIL + OFFICIAL-ROW ARITHMETIC, NOT `RC-RANK`.

The conic binary-form reduction says that the exact-profile route only needs a
uniform codimension bound `Delta <= 1847`.  This packet records one tempting
sharpening and repairs it immediately.

```text
CONIC-6A-FULL:
  on repaired same-fiber conic charts, the cleared h=3 conic binary-form span
  has full rank min(A B^3, L+1) whenever H >= 6A.
```

Here

```text
L = (A-1)+6H(B-1).
```

As a universal statement, `CONIC-6A-FULL` is false.

## Why This Target Matters

Every official exact-profile row satisfies

```text
H - 6A >= 20.
```

The tight row is the first one:

```text
s=13, H=8192, A=1362, B=34.
```

Thus `CONIC-6A-FULL` would prove full degree-space rank on every official
exact-profile conic box, which is stronger than the currently sufficient
codimension bound `Delta <= 1847`.

However the condition `H >= 6A` is not enough by itself outside the official
dense-box regime.

## Bounded Threshold Check

The same pinned conic chart used by the rank guardrails is full at the exact
`B=4` toy threshold:

```text
A=2, B=4, H=12=6A: rank=128, target=128, deficit=0
A=3, B=4, H=18=6A: rank=192, target=192, deficit=0
A=4, B=4, H=24=6A: rank=256, target=256, deficit=0
A=5, B=4, H=30=6A:
rank=320, target=320, deficit=0.
```

Together with the previous large-gap pilot

```text
H=20: deficit=27
H=24: deficit=1
H=32: deficit=0
```

this suggests that `H >= 6A` is a plausible clean line for the conic
binary-form theorem in the `B=4` toy slice.

But nearby slices refute the unrestricted version:

```text
A=3, B=5, H=18=6A: rank=346, target=375, deficit=29
A=4, B=5, H=24=6A: rank=468, target=500, deficit=32
A=3, B=6, H=18=6A: rank=459, target=543, deficit=84
```

The repaired theorem target is therefore not "six-A implies full rank" in all
boxes.  The useful target remains:

```text
For the official exact-profile dense boxes, where H-6A >= 20 and B >= 34,
prove conic binary-form codimension <= 1847.
```

The `H>=6A` arithmetic is still useful because every official row satisfies it,
but it is only one part of the needed rank theorem.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_sixa_threshold_target.py
```

Expected digest:

```text
H3_CONIC_SIXA_THRESHOLD_TARGET_PASS
```
