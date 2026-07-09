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

There are now three compiled arithmetic interfaces.  For each official row
`n=2^s`, let `Z_budget(s)` be the improved non-diagonal bridge budget from the
low/mid and high-row budget packets, let `Z_exact(s)` be the exact-profile
degree-2 bridge budget, and let `Z_private(s)` be the retuned private-linear
budget.

The older diagonal bridge-budget table is retained as a legacy lower bound.
The active non-diagonal table is replayed against it in
`F3_H3_BRIDGE_BUDGET_LINEAGE.md` and is the `Z_budget(s)` used below.

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

The exact-profile degree-2 route is the strongest current conditional route.
It uses the proved log-jet condition profile

```text
C_exact(A,D) = DA + 6D(D-1)
```

and needs the sharper finite-row rank theorem

```text
F3-RANK-AVOID-EXACT:
  after the same degeneracy repairs, every repaired h=3 signature-curve image
  family needed by the bridge has rank greater than
  (DA + 6D(D-1)) times its consumed exact-profile capacity, for the printed
  exact-profile witness parameters.

H3-BRIDGE-RANKCAP-EXACT(Z_exact):
  activated non-toral h=3 shape pairs can be assigned to repaired
  signature-curve images with total consumed exact-profile capacity at most
  Z_exact(s).
```

Then:

```text
F3-RANK-AVOID-EXACT + H3-BRIDGE-RANKCAP-EXACT(Z_exact(s))
  => H3-ACT(16) on row s.
```

The exact-profile capacity guard verifies that on these official boxes a
degree-space-full repaired image has capacity exactly `1`, while the
constant-ratio collapsed model has capacity `0`.  Thus `Z_exact` buys more
distinct rank-effective repaired images, not repeated copies of one image.

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
Z_exact(13) = 33
Z_exact(41) = 21421
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

For the exact-profile route, the replay verifies the pinned exact-profile
witnesses, their `Z_exact+1` infeasibility under the analytic `B` cap, total
gain `51451` over the active non-diagonal table, degree-space one-image
capacity `1`, and collapsed constant-ratio capacity `0`.

The conic-chart degree-space guardrail shows that repaired same-fiber conic
charts should not be assumed to have automatic full degree-space rank in every
box.  The exact-profile theorem obligation is therefore intentionally stated
as a finite-row rank/minor nonvanishing inequality above the exact condition
count, not as a blanket degree-space-fullness theorem.

The exact-profile deficit budget records the weaker sufficient form.  If a
future theorem proves

```text
rank >= (L+1) - Delta
```

for every repaired image, then the official exact-profile boxes all pass as
soon as

```text
Delta <= 1847.
```

The tight row is `s=13`; higher rows have more room.

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
