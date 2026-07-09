# F3 h=3 repeat LP4 exception ledger

Status: PROVED EXCEPTION LEDGER FOR THE LP4 LINE-PENCIL GATE.

This packet records the finite/degenerate line parameters that should not be
included in the generic four-affine-form LP4 rank gate.

## Coefficient Collisions

The first three line-pencil coefficients are

```text
1, r, -r/(r+1).
```

In characteristic not `2` or `3`, they collide exactly for

```text
r in {0, -1, 1, -1/2, -2}.
```

Here `r=0` and `r=-1` are invalid parameters.  The remaining values force
duplicate boundary coordinates:

```text
r=1       gives u=v,
r=-1/2    gives v=w,
r=-2      gives u=w.
```

Thus none of these values contributes to the distinct-boundary LP4 target.

## Triple-Repeat Cell

The fourth coefficient vanishes on

```text
q0(r)=r^2+r+1=0.
```

This is the triple-repeat cell `lambda=1`, already paid by the q0 cell packet:

```text
B_q0 <= 132 n^(2/3),
12 n B_q0 <= 1584 n^(5/3).
```

The replay checks that this contribution is below `n^3` for every official row
`n=2^13..2^41`.

## Role in h=3

The generic LP4 rank/nonvanishing gate may be stated after excluding:

```text
r in {0, -1, 1, -1/2, -2},
q0(r)=0.
```

The first set is inadmissible for distinct triples, and the second set is
already paid.  This packet does not prove the remaining LP4 rank gate.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lp4_exception_ledger.py
```

Expected digest:

```text
H3_REPEAT_LP4_EXCEPTION_LEDGER_PASS
```
