# F3 h=3 repeat hitting exception scan

Status: FINITE FALSIFICATION OF THE PURE `2`-COVER TARGET; POSITIVE
EVIDENCE FOR SMALL HITTING.

The forced-coordinate-2 normal form explains the row `(p,n)=(65537,256)`, but
the stronger global target

```text
all active repeat-boundary coordinate edges are hit by 2
```

is false even on boundary-style rows with `p >= n^2`.

## Witness Rows

A bounded local scan found the following finite witnesses:

```text
p=337   n=16  B_line=6  active_edges=1 non_two_edges=1 tau_coord=1
p=2017  n=32  B_line=6  active_edges=1 non_two_edges=1 tau_coord=1
p=4801  n=64  B_line=6  active_edges=1 non_two_edges=1 tau_coord=1
p=7937  n=64  B_line=12 active_edges=2 non_two_edges=2 tau_coord=1
p=91393 n=256 B_line=12 active_edges=2 non_two_edges=2 tau_coord=1
```

For comparison, the special row remains:

```text
p=65537 n=256 B_line=48 active_edges=8 non_two_edges=0 tau_coord=1
```

Thus `H3-FORCED-TWO-COVER` should not be pursued as a theorem.  The right
target is the weaker hitting statement.

## Exception-Hitting Form

Let `tau_non_two` be the minimum size of a set hitting the active coordinate
edges not already hit by `2`.  Then

```text
tau_coord <= 1 + tau_non_two
```

whenever there is a nonempty `2`-hit cell, and `tau_coord <= tau_non_two` if
there is not.  Combining with the coordinate-hitting compiler gives

```text
repeat_residue <= (72 tau_coord + 18)n^2.
```

The witness rows above all still have `tau_coord=1`; the non-`2` edges are
not a failure of the hitting route, only of the overly rigid fixed-`2` route.

## Role in h=3

The surviving structural target is:

```text
H3-COORD-HITTING:
  prove tau_coord <= C n^eta with eta < 1,
```

or prove this through a small collection of forced-coordinate cells, one of
which is the explicit inverse-pair `2`-cell.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_hitting_exception_scan.py
```

Expected digest:

```text
H3_REPEAT_HITTING_EXCEPTION_SCAN_PASS
```
