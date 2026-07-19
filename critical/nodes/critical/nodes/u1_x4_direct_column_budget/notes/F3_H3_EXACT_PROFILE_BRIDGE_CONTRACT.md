# F3 h=3 exact-profile bridge contract

Status: REPLAYED CONTRACT LEDGER, NOT `RC-NV`, NOT THE GEOMETRIC BRIDGE, AND
NOT `H3-ACT`.

This packet records the exact dependency interface for the strongest current
degree-2 h=3 route.  Its purpose is to prevent three separate arithmetic
interfaces from being silently mixed:

- the exact reduced-condition profile `C_exact(A,D)=DA+6D(D-1)`;
- the exact-profile rank-capacity budget `Z_exact`;
- the L2/level-set pair-count target for a chart ledger.

## Contract

For every official row `n=2^s`, `13 <= s <= 41`, the exact-profile route may
be used in the following form:

```text
RC-RED-PROFILE
+ F3-RANK-AVOID-EXACT
+ H3-BRIDGE-RANKCAP-EXACT(Z_exact)
=> H3-ACT(16).
```

Here the replayed official-row constants are:

```text
Z_exact = 33..21421,
total gain over the active non-diagonal Z_budget table = 51451,
one-image degree-space capacity = 1,
constant-ratio collapsed capacity = 0,
minimum allowed rank deficit = 1847.
```

Thus `H3-BRIDGE-RANKCAP-EXACT(Z_exact)` must assign activated non-toral
shape pairs to **distinct rank-effective repaired images**, spending at most
one exact-profile capacity unit per image on the official boxes.  Repeated
base points in the same same-`(e1,e2)` fiber and constant-ratio collapsed cells
do not create extra capacity.

The bounded-deficit variant of the rank gate is:

```text
rank >= (L+1)-Delta with Delta <= 1847
```

on every official exact-profile box.  This is sufficient for the one-image
inequality `rank > C_exact(A,D)`, but it still does not prove the needed
finite-row rank/minor theorem.

## Separation From The L2 Bridge

The L2/level-set bridge target remains the separate chart-count statement

```text
sum_z R_z(R_z-6) <= 1152 n,
```

equivalently `P_total <= 16n`.  The number `Z_exact` is not a replacement for
this L2 target.  A future proof can proceed by the rank-family contract above
or by a direct L2/level-set theorem, but it should not cite `Z_exact` as if it
were itself an L2 pair-count bound.

## What Remains

This packet does not close a red node.  The remaining exact-profile route
obligations are:

- prove the finite-row repaired-image rank/minor nonvanishing theorem, or the
  bounded-deficit version with uniform `Delta <= 1847`;
- prove the geometric bridge assigning activated non-toral shape pairs to the
  required distinct rank-effective repaired images within `Z_exact`;
- or replace that route with a direct L2/level-set chart-count proof.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_exact_profile_bridge_contract.py
```

Expected digest:

```text
H3_EXACT_PROFILE_BRIDGE_CONTRACT_PASS
```
