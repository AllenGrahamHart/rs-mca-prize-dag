# F3 h=3 repeat coordinate-cover ledger

Status: PROVED COMPILER PLUS FINITE EVIDENCE, NOT A COVER-SIZE THEOREM.

This packet introduces the canonical forced-coordinate cover of the
repeat-boundary support.

## Definition

For a row, let `C_coord` be the number of subgroup elements that occur as one
of the first three coordinates in at least one active normalized repeat-boundary
triple `(u,v,w)`.

Equivalently, the cover set is

```text
A_coord = union_{active triples (u,v,w)} {u,v,w}.
```

This set trivially covers every active triple, so the forced-fiber degree bound
applies with `F=C_coord`:

```text
B_line <= 6 C_coord n,
repeat_residue <= (72 C_coord + 18)n^2.
```

Thus the repeat residue is subcubic whenever

```text
C_coord = o(n),
```

and it is below `n^3` on a concrete row whenever

```text
72 C_coord + 18 < n.
```

This is not yet a theorem because `C_coord` itself is not bounded uniformly.
It is the most direct measurable object for the forced-coordinate route.

## Boundary Evidence

The focused boundary rows currently give:

```text
p=257     n=16   C_coord=0
p=1153    n=32   C_coord=0
p=4289    n=64   C_coord=0
p=17921   n=128  C_coord=0
p=65537   n=256  B_line=48, support=48, C_coord=17
p=262657  n=512  C_coord=0
p=1051649 n=1024 C_coord=0
```

The nonzero row has `C_coord=17`, so the coordinate-cover residue bound is

```text
(72*17+18) * 256^2 = 81,395,712,
```

which is larger than `256^3`.  Thus the canonical cover is structurally useful
but not yet strong enough, by this crude bound, to certify the `n=256` row.  The
smaller common forced cover `{2}` gives the sharper row explanation.  This is
formalized by the coordinate-hitting ledger, where the same row has
`tau_coord=1`.

## Role in h=3

The forced-cover target can now be stated without existential language:

```text
H3-COORD-COVER:
  prove C_coord <= C n^eta with eta < 1
```

or prove that a smaller hitting subcover exists.  The coordinate-hitting ledger
records the sharper target consumed by the degree bound.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_coordinate_cover_ledger.py
```

Expected digest:

```text
H3_REPEAT_COORDINATE_COVER_LEDGER_PASS
```
