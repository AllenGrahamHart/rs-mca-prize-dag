# F3 h=3 repeat linear-hypergraph compiler

Status: PROVED ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet proves that the active coordinate hypergraph is linear: two
distinct active edges cannot share two coordinates.

## Pair Uniqueness

In shifted coordinates

```text
x = a-1,  y = b-1,  z = c-1,
```

an active edge satisfies

```text
xy+xz+yz = 0.
```

For any active pair `a,b`, the shifted coordinates are nonzero.  Also
`x+y != 0`, because otherwise the reciprocal equation would give `xy=0`.
Thus the third coordinate is forced:

```text
z = -xy/(x+y),
c = 1 - (a-1)(b-1)/(a+b-2).
```

Therefore any unordered coordinate pair lies in at most one active edge.

## Consequences

The active coordinate hypergraph is a linear 3-uniform hypergraph:

```text
distinct active edges intersect in at most one coordinate.
```

This kills two previously named pairwise-coreless patterns:

```text
H3-NO-PINCHED-TRIANGLE   is automatic;
H3-NO-TETRAHEDRON        is automatic.
```

Both patterns repeat a coordinate pair across two distinct edges, which
linearity forbids.

So the pairwise-coreless branch collapses to a single target:

```text
H3-NO-LOOSE-TRIANGLE.
```

## Guardrails

The replay checks exact pair uniqueness on the boundary witness rows and the
non-boundary contrast row:

```text
p=337   n=16  active_edges=1 repeated_pairs=0
p=2017  n=32  active_edges=1 repeated_pairs=0
p=4801  n=64  active_edges=1 repeated_pairs=0
p=7937  n=64  active_edges=2 repeated_pairs=0
p=65537 n=256 active_edges=8 repeated_pairs=0
p=91393 n=256 active_edges=2 repeated_pairs=0
p=97    n=32  active_edges=15 repeated_pairs=0
```

The abstract model guardrail checks that loose triangles are linear, while
pinched triangles and tetrahedra repeat coordinate pairs.

## Role in h=3

The star obstruction tree now has three surviving subtargets:

```text
H3-VALUE-INJECTIVE
H3-SLOPE-HIT
H3-NO-LOOSE-TRIANGLE
```

Together these imply `tau_coord<=1`, hence `repeat_residue <= 90n^2`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_linear_hypergraph_compiler.py
```

Expected digest:

```text
H3_REPEAT_LINEAR_HYPERGRAPH_COMPILER_PASS
```
