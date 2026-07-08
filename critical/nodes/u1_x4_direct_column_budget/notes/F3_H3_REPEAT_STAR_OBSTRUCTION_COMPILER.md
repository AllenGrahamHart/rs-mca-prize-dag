# F3 h=3 repeat star-obstruction compiler

Status: PROVED COMBINATORIAL COMPILER PLUS FINITE ROW CHECKS.

This packet turns the singleton-hitting target into a finite-pattern
obstruction problem.

## Compiler

Let `E` be the active coordinate hypergraph whose edges are the three-element
sets `{u,v,w}` coming from active repeat-boundary triples.

Then

```text
tau_coord <= 1
```

is equivalent to saying that all active edges have a common coordinate.  If
this fails, a small obstruction exists:

```text
there are at most four active edges with empty total intersection.
```

Proof: choose one active edge `E0={a,b,c}`.  If no coordinate is common to all
active edges, then for each `x in E0` there is an active edge `E_x` not
containing `x`.  The four edges

```text
E0, E_a, E_b, E_c
```

have empty intersection.  The converse is immediate.

Thus the star target is equivalent to excluding these four-edge
empty-intersection configurations in the repeat-boundary incidence variety.

## Finite Checks

The compiler script checks the abstract combinatorial equivalence and then
verifies that the current finite witness rows have no obstruction:

```text
p=337   n=16  active_edges=1 tau_coord=1 obstruction_edges=0
p=2017  n=32  active_edges=1 tau_coord=1 obstruction_edges=0
p=4801  n=64  active_edges=1 tau_coord=1 obstruction_edges=0
p=7937  n=64  active_edges=2 tau_coord=1 obstruction_edges=0
p=65537 n=256 active_edges=8 tau_coord=1 obstruction_edges=0
p=91393 n=256 active_edges=2 tau_coord=1 obstruction_edges=0
```

These checks are not evidence beyond the rows already scanned; their role is
to verify that the obstruction extractor matches `tau_coord`.

## Role in h=3

The next proof target can now be phrased without searching over arbitrary
hitting sets:

```text
H3-STAR-OBSTRUCTION:
  rule out four active repeat-boundary coordinate edges with empty
  intersection in the boundary-style regime.
```

If this is proved, then `tau_coord<=1`, and the coordinate-hitting compiler
gives

```text
repeat_residue <= 90n^2.
```

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_star_obstruction_compiler.py
```

Expected digest:

```text
H3_REPEAT_STAR_OBSTRUCTION_COMPILER_PASS
```
