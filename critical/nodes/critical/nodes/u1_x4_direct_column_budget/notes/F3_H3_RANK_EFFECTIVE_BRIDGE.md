# F3 h=3 rank-effective bridge interface

Status: PROVED ARITHMETIC INTERFACE REPAIR, NOT `RC-RANK` AND NOT THE
GEOMETRIC BATCHING THEOREM.

This packet tightens the h=3 bridge contract after the rank-stress warning.
The earlier bridge wording bounded a raw family size `|Z|`.  That is not quite
the invariant consumed by `RC-RANK`, because repeating the same curve image does
not increase substitution rank.  The bridge must bound rank-effective capacity
units, not raw multiplicity.

## Pre-registration

Question:

```text
Given a pinned substitution rank r for one repaired curve image, how many
activated curve copies can that image pay in the RC-RANK inequality?
```

Success criterion:

- derive the exact capacity rule from `rank > 13 D (A + D) |Z|`;
- verify it on the ranks pinned by the rank sample and rank stress packets;
- restate the bridge contract so future h=3 work does not silently count raw
  duplicate curves.

Failure criterion:

- treat this as a proof of the rank theorem;
- allow unlimited multiplicity for an individually passing curve;
- change the official `Z_budget` arithmetic without changing what the bridge
  theorem is required to bound.

## Capacity Rule

In the toy row used by the rank sample/stress packets,

```text
p=769, h=32, A=5, B=4, D=1,
conditions per curve = 13 D (A + D) = 78.
```

If a repaired curve image has substitution rank `r`, then the largest raw
multiplicity `m` that this image can pay by itself is

```text
cap(r) = floor((r - 1) / 78),
```

because `RC-RANK` needs the strict inequality

```text
r > 78 m.
```

The verifier checks the pinned ranks:

```text
constant-ratio collapsed: rank 50  -> capacity 0
private-divisor rational: rank 293 -> capacity 3
shifted polynomial:       rank 247 -> capacity 3
shared denominator:       rank 247 -> capacity 3
repaired random full-rank: rank 320 -> capacity 4
```

This exactly explains the duplicate warning:

```text
private curve repeated twice:      293 > 2*78  passes
private curve repeated four times: 293 < 4*78  fails
```

## Bridge Contract Repair

The h=3 bridge should now be read as:

```text
H3-BRIDGE-RANKCAP(Z):
  After toral, constant-ratio, and hyperbola-line degeneracies are paid or
  excluded, activated non-toral h=3 shape pairs are assigned to repaired
  signature-curve images with total consumed rank capacity at most Z.
```

Then the compiled conditional chain is:

```text
RC-RED(13) + RC-RANK + H3-BRIDGE-RANKCAP(Z_budget(n)) => H3-ACT(16).
```

This does not change the `Z_budget` table.  It changes what the future
geometric theorem must prove: not a raw bound on a list with duplicates, but a
bound on rank-effective curve-image capacity.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rank_effective_bridge.py
```

Expected digest:

```text
H3_RANK_EFFECTIVE_BRIDGE_PASS
```
