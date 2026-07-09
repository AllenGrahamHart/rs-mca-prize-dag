# F3 h=3 conic six-A threshold target

Status: SHARPENED PROOF TARGET + BOUNDED CHECK, NOT `RC-RANK`.

The conic binary-form reduction says that the exact-profile route only needs a
uniform codimension bound `Delta <= 1847`.  This packet records a sharper
possible theorem suggested by the current evidence:

```text
CONIC-6A-FULL:
  on repaired same-fiber conic charts, the cleared h=3 conic binary-form span
  has full rank min(A B^3, L+1) whenever H >= 6A.
```

Here

```text
L = (A-1)+6H(B-1).
```

This packet does not prove `CONIC-6A-FULL`.

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

## Bounded Threshold Check

The same pinned conic chart used by the rank guardrails is full at the exact
toy threshold:

```text
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
binary-form theorem.  It is still only evidence plus official-row arithmetic.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_sixa_threshold_target.py
```

Expected digest:

```text
H3_CONIC_SIXA_THRESHOLD_TARGET_PASS
```
