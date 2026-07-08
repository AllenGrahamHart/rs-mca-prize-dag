# F3 h=3 repeat frontier ledger

Status: REPLAYED FRONTIER LEDGER, NOT A NEW THEOREM.

This packet records the current branch-level frontier for the h=3
repeat-boundary star route by importing the existing compilers and asserting
their degree/rank/payment values agree.

## Strict Branch Frontier

The strict route has seven branch-level gates:

```text
H3-VALUE-GEN-INJECTIVE:
  generic same-lambda ratio collision, S_total=14, off-orbit total=10;

H3-VALUE-SCALE-INJECTIVE:
  lambda=1 primitive-cube scale collision, S_total=6, off-orbit degree=3;

H3-SLOPE-GG-HIT:
  generic-generic lambda-distinct slope hit, S_total=14,
  hit-product total <= 41;

H3-SLOPE-MIXED-HIT:
  generic/scale lambda-distinct slope hit, S_total=10,
  hit-product total <= 27;

LOOSE-GEN-RANK/NV:
  generic two-parameter loose nine-slope target, S_total=15;

LOOSE-A-RANK/NV:
  clean branch-A one-parameter loose eight-slope target, S_total=22;

LOOSE-B-RANK/NV:
  clean branch-B one-parameter loose eight-slope target, S_total=24.
```

## Count Route Frontier

The scale same-lambda branch has a separate count payment:

```text
H3-VALUE-SCALE-INJECTIVE
  replaced by scale collision pairs <= binom(floor((n-1)/3),2).
```

Therefore the count route has six still-open strict gates:

```text
H3-VALUE-GEN-INJECTIVE,
H3-SLOPE-GG-HIT,
H3-SLOPE-MIXED-HIT,
LOOSE-GEN-RANK/NV,
LOOSE-A-RANK/NV,
LOOSE-B-RANK/NV.
```

This does not prove `H3-VALUE-INJECTIVE`; it records the alternate payment
route for arguments that can tolerate the quadratic scale branch.

## Loose Rank-Minor Sample Box

For the sample box

```text
P=16, C=512, B=4, D=2, |Z|=1, n=32,
```

the imported rank-minor compiler gives:

```text
generic:  rank target 1061, entry degree 1470, minor degree <= 1559670;
branch A: rank target 1057, entry degree 2127, minor degree <= 2248239;
branch B: rank target 1057, entry degree 2319, minor degree <= 2451183.
```

## Paid Ledgers

At the first official row `n=2^13`, the paid ledgers are:

```text
scale orbits <= 2730,
scale collision pairs <= 3725085,
loose secondary points <= 434176.
```

Both paid point/pair ledgers are below `n^2` throughout the official range.

## Role in h=3

This packet is a consistency checkpoint for the current frontier.  It should
be updated whenever a branch gate is proved, weakened, paid, or replaced.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_frontier_ledger.py
```

Expected digest:

```text
H3_REPEAT_FRONTIER_LEDGER_PASS
```
