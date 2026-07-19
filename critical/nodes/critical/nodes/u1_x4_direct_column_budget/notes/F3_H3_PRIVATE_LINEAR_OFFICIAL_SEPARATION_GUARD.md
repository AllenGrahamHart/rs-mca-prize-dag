# F3 h=3 private-linear official separation guard

Status: PROVED ARITHMETIC GUARDRAIL, NOT THE PRIVATE-LINEAR RANK THEOREM.

This packet records a simple but important fact about the retuned official
private-linear compiler: every official box lies deep in the separated
parameter regime

```text
max(A, D, B-1) < H,
```

where `H=n=2^s` is the row subgroup order.

## Checks

The replay checks every row `s=13..41` in
`f3_h3_private_linear_lowrow_budget.py`, both for the passing `Z_private`
witness and for the stored `Z_private+1` next-failure witness.

The exact minimum margins are:

```text
passing witnesses:      H - max(A,D,B-1) >= 7904
next-failure witnesses: H - max(A,D,B-1) >= 7911
next B-cap scans:       H - (B_cap-1)    >= 8099
```

The largest `B` values in the table are:

```text
passing B:      41284
next-failure B: 41284
next B cap:     61931
```

while the smallest official `H` is `8192`; the worst margins occur at the
first official row.

## Role

This guard does not prove rank.  It gives the future private-linear theorem a
clean official hypothesis: the boxes needed by the compiler are not in a
small-`H` overlap regime.  Combined with the resultant-degree guard, it
separates the known toy obstruction from the official private-linear route.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_official_separation_guard.py
```

Expected digest:

```text
H3_PRIVATE_LINEAR_OFFICIAL_SEPARATION_GUARD_PASS
```
