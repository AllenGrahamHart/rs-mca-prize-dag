# F3 h=3 repeat star-obstruction taxonomy

Status: PROVED COMBINATORIAL TAXONOMY PLUS FINITE GUARDRAILS.

This packet splits the star-obstruction target into two concrete cases.

## Taxonomy

Let `E` be a set of active coordinate edges.  If `E` is not a star, then its
total intersection is empty.  There are exactly two obstruction modes:

```text
DISJOINT-PAIR:
  two active edges are disjoint;

PAIRWISE-CORELESS:
  every pair of active edges intersects, but the total intersection is empty.
```

Combining this with the star-obstruction compiler, `tau_coord>1` in the active
coordinate hypergraph implies one of:

```text
1. two disjoint active repeat-boundary coordinate edges; or
2. at most four pairwise-intersecting active edges with empty total
   intersection.
```

Thus proving singleton hitting can be split into two algebraic exclusions.

## Guardrails

The finite witness rows from the hitting scan are all stars:

```text
p=337   n=16  active_edges=1 kind=star
p=2017  n=32  active_edges=1 kind=star
p=4801  n=64  active_edges=1 kind=star
p=7937  n=64  active_edges=2 kind=star
p=65537 n=256 active_edges=8 kind=star
p=91393 n=256 active_edges=2 kind=star
```

The non-boundary contrast row has a genuine disjoint-pair obstruction:

```text
p=97 n=32 active_edges=15 kind=disjoint_pair
```

The script also checks abstract model examples for the `star`,
`disjoint_pair`, and `pairwise_coreless` classes.

## Role in h=3

The star theorem can now be attacked by two named exclusions:

```text
H3-NO-DISJOINT-EDGES:
  no two active reciprocal edges are disjoint in the boundary-style regime;

H3-NO-PAIRWISE-CORELESS:
  no at-most-four active reciprocal edges are pairwise intersecting with
  empty total intersection in the boundary-style regime.
```

Together these imply `tau_coord<=1`, hence `repeat_residue <= 90n^2`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_star_obstruction_taxonomy.py
```

Expected digest:

```text
H3_REPEAT_STAR_OBSTRUCTION_TAXONOMY_PASS
```
