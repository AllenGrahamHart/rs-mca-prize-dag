# F3 h=3 repeat pairwise-coreless compiler

Status: PROVED COMBINATORIAL COMPILER PLUS FINITE GUARDRAILS.

This packet sharpens the `H3-NO-PAIRWISE-CORELESS` target from the
star-obstruction taxonomy.

## Subtype Classification

Let `E` be a family of at most four active 3-edges that is pairwise
intersecting and has empty total intersection.  Then exactly one of the
following occurs.

### Three-Edge Coreless

Some three edges already have empty total intersection:

```text
E_1 cap E_2 cap E_3 = empty.
```

Since the family is pairwise intersecting, these three edges form the basic
pairwise-coreless triangle.

### Tetrahedron

Every three-edge subfamily has a common point, but all four edges together do
not.  In this case the family is forced to be tetrahedral.

Proof: for each edge `E_i`, choose a point `x_i` common to the other three
edges.  Since the total intersection is empty, `x_i notin E_i`.  For
`j != i`, `x_i in E_j`, so each edge `E_j` contains the three points
`{x_i : i != j}`.  The edges are 3-sets, hence

```text
E_j = {x_i : i != j}.
```

Thus the four edges are exactly the four 3-subsets of the four-point set
`{x_1,x_2,x_3,x_4}`.

## Guardrails

The script checks abstract model examples for both subtypes.  The current
boundary witness rows remain stars, and the non-boundary contrast row remains
a disjoint-pair obstruction:

```text
p=337   n=16  kind=star subtype=star
p=2017  n=32  kind=star subtype=star
p=4801  n=64  kind=star subtype=star
p=7937  n=64  kind=star subtype=star
p=65537 n=256 kind=star subtype=star
p=91393 n=256 kind=star subtype=star
p=97    n=32  kind=disjoint_pair subtype=has_disjoint_pair
```

## Role in h=3

The pairwise-coreless half of the star theorem splits into:

```text
H3-NO-THREE-EDGE-CORELESS:
  no three active boundary-style reciprocal edges are pairwise intersecting
  with empty total intersection;

H3-NO-TETRAHEDRON:
  no four active boundary-style reciprocal edges form the tetrahedral
  four-3-subsets pattern.
```

Together these prove `H3-NO-PAIRWISE-CORELESS`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_pairwise_coreless_compiler.py
```

Expected digest:

```text
H3_REPEAT_PAIRWISE_CORELESS_COMPILER_PASS
```
