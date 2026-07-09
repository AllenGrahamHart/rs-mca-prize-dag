# F3 h=3 repeat-support boundary evidence

Status: MACHINE-VERIFIED FINITE EVIDENCE AND ZERO-SUPPORT FALSIFIER.

This packet tests the repeat-boundary line support on boundary-style rows
`p >= n^2` using the efficient `u,v in H` formulation.  It is not a support
theorem.  Its main value is guardrail information: support emptiness is false,
so the remaining target must be a support bound.

## Pre-registration

Question:

```text
Does the repeat-boundary line support vanish on boundary-style rows p >= n^2?
```

Success criterion:

- use the `O(n^2)` subgroup-pair scan, not a field-size slope scan;
- verify several boundary-style rows exactly;
- record any nonzero support row as a falsifier for zero-support shortcuts.

Failure criterion:

- promote finite zero rows to a theorem;
- run a field-size search that scales with `p`;
- ignore a nonzero row.

## Efficient Scanner

Instead of looping over every field slope `r`, loop over

```text
u,v in H \ {1}
```

and compute

```text
w = 1 - (u-1)(v-1)/(u+v-2),
lambda = u+v+w-2.
```

If `w,lambda in H` and `u,v,w` are distinct, then this contributes to
`B_line` and the active slope is

```text
r = (u-1)/(v-1).
```

This is exactly the same line compiler, but costs `O(n^2)` rather than
`O(p^2)`.

## Replay Output

The current boundary-style ledger is:

```text
p=257     n=16   B_line=0
p=1153    n=32   B_line=0
p=4289    n=64   B_line=0
p=17921   n=128  B_line=0
p=65537   n=256  B_line=48, support=48, R_orb=8, max_fiber=1
p=262657  n=512  B_line=0
p=1051649 n=1024 B_line=0
```

Thus a tempting theorem

```text
B_line = 0 for all boundary-style official rows
```

is false.  The `n=256, p=65537` row has nonzero genuine support, although it is
still tiny compared with `n`.

## Role in h=3

This supports the current target:

```text
R_orb <= C n^beta
```

rather than an emptiness target.  It also suggests that boundary-style rows may
have a much smaller support constant than dense toy rows, but that remains
finite evidence only.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_support_boundary_evidence.py
```

Expected digest:

```text
H3_REPEAT_SUPPORT_BOUNDARY_EVIDENCE_PASS
```
