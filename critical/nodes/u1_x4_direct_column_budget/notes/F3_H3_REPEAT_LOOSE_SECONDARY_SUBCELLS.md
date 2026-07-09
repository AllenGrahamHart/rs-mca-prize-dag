# F3 h=3 repeat loose secondary subcells

Status: PROVED ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet classifies the lower-dimensional secondary collision subcells
inside the two one-parameter loose collision branches.

## Setup

The loose case split has two one-parameter collision branches:

```text
branch A: b = a(a+1)/(a^2+a+1),
branch B: b = -(2a^2+2a+1)/(a^2+a+1).
```

Each branch is defined by one lambda-coordinate collision divisor.  A
secondary subcell is a parameter value on that branch where an additional
lambda-coordinate collision divisor also vanishes, so the eight-slope branch
has fewer than eight distinct slopes.

After pulling back the other collision divisors to the branch parameter `a`,
the compiler strips only structural non-pole factors

```text
a, a+1, a^2+a+1.
```

## Residual Degrees

For branch A, the residual secondary product has degree

```text
24.
```

For branch B, the residual secondary product has degree

```text
29.
```

Thus, outside at most `24` branch-A parameter values and at most `29`
branch-B parameter values over a row field, the one-parameter branch target
has exactly eight distinct slopes after the primary duplicate is removed.

## Guardrails

The finite guardrail checks the branch formulas over

```text
p = 5, 7, 11, 13, 17, 97.
```

On valid branch parameters, residual product nonzero is equivalent to the
clean eight-slope condition in the checked rows; residual product zero always
creates an additional slope collision.

## Role in h=3

The branch A/B Stepanov targets can now be stated cleanly as:

```text
main branch:
  one-parameter eight-slope target outside a finite secondary set;

secondary subcells:
  at most 24 branch-A and 29 branch-B parameter values before row-specific
  validity filtering.
```

This does not prove `LOOSE-A-RANK/NV` or `LOOSE-B-RANK/NV`; it isolates the
finite lower-dimensional exceptions that a future proof or payment can handle
separately.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_secondary_subcells.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_SECONDARY_SUBCELLS_PASS
```
