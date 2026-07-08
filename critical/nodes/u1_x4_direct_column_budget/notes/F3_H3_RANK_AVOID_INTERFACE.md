# F3 h=3 rank-avoidance interface

Status: CONDITIONAL THEOREM INTERFACE, NOT `RC-RANK`, NOT THE GEOMETRIC BRIDGE,
AND NOT `H3-ACT`.

This packet pins the exact h=3 theorem interface after the rank-model,
generic-open, and private-linear guard repairs.  It is intended to prevent the
remaining target from drifting.

## Pre-registration

Question:

```text
What exact theorem pair would let the existing h=3 arithmetic compiler prove
H3-ACT(16) on every official row n=2^13..2^41?
```

Success criterion:

- state the two remaining theorem obligations precisely;
- verify that the current non-diagonal budget table covers every official
  exponent `13 <= s <= 41`;
- keep the result explicitly conditional.

Failure criterion:

- promote a rank-open or finite-field witness to `RC-RANK`;
- forget the geometric batching/rank-capacity theorem;
- use the private-linear rank cap with the current degree-2 compiler.

## Interface

For each official row `n=2^s`, let `Z_budget(s)` be the improved
non-diagonal bridge budget from the low/mid and high-row budget packets.

The two remaining h=3 theorem obligations are:

```text
F3-RANK-AVOID:
  after toral, constant-ratio, and hyperbola-line cells are paid or excluded,
  every repaired h=3 signature-curve image family needed by the bridge lies in
  a rank-good minor open set.  Equivalently, its cleared substitution image has
  rank greater than 13 D(A+D) times its rank-effective capacity, for the
  printed non-diagonal witness parameters.

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

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rank_avoid_interface.py
```

Expected digest:

```text
H3_RANK_AVOID_INTERFACE_PASS
```
