# F3 h=3 repeat coordinate-hitting ledger

Status: PROVED COMPILER PLUS FINITE CERTIFICATES, NOT A UNIFORM HITTING THEOREM.

This packet sharpens the coordinate-cover ledger.  The full coordinate union
`A_coord` is canonical but can be too large for the elementary forced-fiber
bound.  The right invariant for that bound is the minimum hitting number of
the active coordinate triples.

## Definition

Let the active coordinate hypergraph have one edge `{u,v,w}` for each active
normalized repeat-boundary ordered triple `(u,v,w)`, with duplicate edges
identified.  Define

```text
tau_coord = minimum size of a set A <= H such that A meets every active edge.
```

Any minimum hitter is a forced-coordinate cover in the sense of the
forced-point reduction.  Therefore

```text
B_line <= 3 sum_{a in A} N_a.
```

The elementary forced-fiber degree bound gives `N_a <= 2n`, so

```text
B_line <= 6 tau_coord n.
```

Combining with the repeat-boundary compiler gives

```text
repeat_residue <= 12n B_line + 18n^2
               <= (72 tau_coord + 18)n^2.
```

Thus `tau_coord = o(n)` pays the repeat residue subcubically.  On a concrete
row, this bound is below `n^3` whenever

```text
72 tau_coord + 18 < n.
```

## Boundary Certificates

The replayed boundary rows give:

```text
p=257     n=16   B_line=0  tau_coord=0
p=1153    n=32   B_line=0  tau_coord=0
p=4289    n=64   B_line=0  tau_coord=0
p=17921   n=128  B_line=0  tau_coord=0
p=65537   n=256  B_line=48 tau_coord=1, hitter={2}
p=262657  n=512  B_line=0  tau_coord=0
p=1051649 n=1024 B_line=0  tau_coord=0
```

For the nonzero row, the active hypergraph has eight distinct coordinate
edges, all hit by `{2}`.  The forced-fiber sum is exact:

```text
B_line = 48 = 3N_2.
```

The elementary payment is therefore

```text
(72*1 + 18) * 256^2 = 5,898,240 < 256^3 = 16,777,216.
```

This certifies the nonzero boundary row by the forced-coordinate route.  It
does not prove a uniform small hitting theorem; that remains the structural
target.

## Role in h=3

The forced-cover target can now be stated in its sharp combinatorial form:

```text
H3-COORD-HITTING:
  prove tau_coord <= C n^eta with eta < 1.
```

This is weaker than bounding the full coordinate union `C_coord`, and it is
the invariant actually consumed by the elementary forced-fiber bound.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_coordinate_hitting_ledger.py
```

Expected digest:

```text
H3_REPEAT_COORDINATE_HITTING_LEDGER_PASS
```
