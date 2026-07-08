# F3 h=3 repeat loose-triangle shadow compiler

Status: PROVED COMBINATORIAL/ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet turns the remaining `H3-NO-LOOSE-TRIANGLE` target into a shadow
graph condition.

## Shadow Graph

For every active coordinate edge `{a,b,c}`, put the three coordinate pairs

```text
{a,b}, {a,c}, {b,c}
```

in the shadow graph.

The linear-hypergraph compiler proves that each shadow pair belongs to at most
one active edge.  Thus every shadow triangle is of exactly one of the following
types:

```text
CONTAINED:
  all three shadow pairs come from one active edge;

LOOSE:
  the three shadow pairs come from three distinct active edges.
```

The contained case is harmless: it is just one active edge.  The loose case is
exactly the remaining pairwise-coreless obstruction:

```text
{a,b,x}, {a,c,y}, {b,c,z}
```

with no common coordinate.

Therefore

```text
H3-NO-LOOSE-TRIANGLE
```

is equivalent to:

```text
every shadow triangle is contained in a single active edge.
```

## Guardrails

The abstract model check verifies:

```text
one active edge -> one contained triangle;
one loose triangle -> three contained triangles plus one loose shadow triangle.
```

Finite row checks:

```text
p=337   n=16  active_edges=1 shadow_edges=3  contained=1  loose=0
p=2017  n=32  active_edges=1 shadow_edges=3  contained=1  loose=0
p=4801  n=64  active_edges=1 shadow_edges=3  contained=1  loose=0
p=7937  n=64  active_edges=2 shadow_edges=6  contained=2  loose=0
p=65537 n=256 active_edges=8 shadow_edges=24 contained=8  loose=0
p=91393 n=256 active_edges=2 shadow_edges=6  contained=2  loose=0
```

The non-boundary contrast row does have loose triangles, so this final
pairwise-coreless target is not vacuous:

```text
p=97 n=32 active_edges=15 shadow_edges=45 contained=15 loose=2
```

## Role in h=3

The star obstruction tree now has this final pairwise-coreless target:

```text
H3-SHADOW-TRIANGLE-FREE:
  every triangle in the active-pair shadow graph is contained in one active
  coordinate edge.
```

Together with `H3-VALUE-INJECTIVE` and `H3-SLOPE-HIT`, this implies
`tau_coord<=1`, hence `repeat_residue <= 90n^2`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_triangle_shadow_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_TRIANGLE_SHADOW_COMPILER_PASS
```
