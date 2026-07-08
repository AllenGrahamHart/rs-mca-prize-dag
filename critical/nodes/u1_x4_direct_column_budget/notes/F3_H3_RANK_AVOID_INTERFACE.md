# F3 h=3 rank-avoidance interface

Status: CONDITIONAL THEOREM INTERFACE, NOT `RC-RANK`, NOT THE GEOMETRIC BRIDGE,
AND NOT `H3-ACT`.

This packet pins the exact h=3 theorem interface after the rank-model,
generic-open, and private-linear guard repairs.  It is intended to prevent the
remaining target from drifting.

## Pre-registration

Question:

```text
What exact theorem pairs would let the h=3 arithmetic compilers prove
H3-ACT(16) on every official row n=2^13..2^41?
```

Success criterion:

- state the two remaining theorem obligations precisely;
- verify that the current non-diagonal budget table covers every official
  exponent `13 <= s <= 41`;
- verify that the private-linear budget table also covers every official
  exponent `13 <= s <= 41`;
- keep the result explicitly conditional.

Failure criterion:

- promote a rank-open or finite-field witness to `RC-RANK`;
- forget the geometric batching/rank-capacity theorem;
- mix the private-linear rank cap with the degree-2 compiler.

## Interface

There are now two separately compiled arithmetic routes.  For each official
row `n=2^s`, let `Z_budget(s)` be the improved non-diagonal bridge budget from
the low/mid and high-row budget packets, and let `Z_private(s)` be the retuned
private-linear budget.

The degree-2 non-diagonal route needs:

```text
F3-RANK-AVOID:
  after toral, constant-ratio, and hyperbola-line cells are paid or excluded,
  every repaired h=3 signature-curve image family needed by the bridge lies in
  a rank-good minor open set over the actual row field.  Equivalently, at the
  row prime `p`, its cleared substitution image has rank greater than
  13 D(A+D) times its rank-effective capacity, for the printed non-diagonal
  witness parameters.

H3-BRIDGE-RANKCAP(Z_budget):
  activated non-toral h=3 shape pairs can be assigned to repaired
  signature-curve images with total consumed rank capacity at most
  Z_budget(s).
```

Then the already-banked arithmetic compiler gives:

```text
F3-RANK-AVOID + H3-BRIDGE-RANKCAP(Z_budget(s))
  => H3-ACT(16) on row s.
```

The private-linear route is separate.  It may be used only with the
private-linear degree cap `L_private=(A-1)+3n(B-1)` and the retuned
`Z_private(s)` table:

```text
F3-PRIVATE-LINEAR-RANK-AVOID:
  after the same toral, constant-ratio, and hyperbola-line cells are paid or
  excluded, every repaired private-linear signature-curve image family needed
  by the bridge has rank greater than 13 D(A+D) times its rank-effective
  capacity over the actual row field, for the printed private-linear witness
  parameters.

H3-BRIDGE-PRIVATE-RANKCAP(Z_private):
  activated non-toral h=3 shape pairs can be assigned to repaired
  private-linear signature-curve images with total consumed rank capacity at
  most Z_private(s).
```

Then the retuned private-linear arithmetic compiler gives:

```text
F3-PRIVATE-LINEAR-RANK-AVOID
  + H3-BRIDGE-PRIVATE-RANKCAP(Z_private(s))
  => H3-ACT(16) on row s.
```

Together with `F3_H3_PER_ROW_ACCIDENT_STEPANOV_POSE.md`, `H3-ACT(16)` gives
the h=3 contribution bound needed for the F3 floor for all official rows.

## Budget Coverage

The replay verifies all official exponents:

```text
s = 13,14,...,41.
```

The minimum and maximum printed rank-capacity budgets are:

```text
Z_budget(13) = 16
Z_budget(41) = 10795
Z_private(13) = 23
Z_private(41) = 15267
```

For every row, the verifier checks the pinned non-diagonal witness
`(A,B,D,Z)` satisfies:

```text
13 D(A+D) Z < A B^3,
13 D(A+D) Z < Z(L+1),       L = (A-1)+6n(B-1),
ceil(Z L / D) <= 16n,
```

and that the already-banked `Z+1` row fails the `16n` target.  This packet does
not rescan parameter space; the exhaustive scans remain in the low/high budget
packets.

For the private-linear table it checks the pinned `Z_private` witnesses with

```text
L_private = (A-1)+3n(B-1),
ceil(Z_private L_private / D) <= 16n,
```

and verifies the stored `Z_private+1` bound is already above `16n`.  The
maximality scans remain in `F3_H3_PRIVATE_LINEAR_LOWROW_BUDGET.md`.

The finite-field qualifier is essential.  `F3_H3_PRIVATE_LINEAR_BAD_PRIME_GUARDRAIL.md`
exhibits an integer private-linear coefficient matrix with full degree-space
rank over Q but a rank drop modulo `p=1009`.  Therefore a proof of the
rank-avoidance theorem must leave a rank-good minor nonzero modulo the actual
row prime; characteristic-zero fullness alone is not enough.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rank_avoid_interface.py
```

Expected digest:

```text
H3_RANK_AVOID_INTERFACE_PASS
```
