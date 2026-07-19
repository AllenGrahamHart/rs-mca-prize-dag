# F3 h=3 repeat coreless-pattern compiler

Status: PROVED COMBINATORIAL COMPILER PLUS FINITE GUARDRAILS.

This packet refines the pairwise-coreless obstruction shapes.

## Three-Edge Patterns

Let `E_1,E_2,E_3` be three 3-edges that are pairwise intersecting but have
empty total intersection.  Then the sorted pair-intersection sizes are exactly
one of

```text
(1,1,1),  (1,1,2).
```

The first is the loose triangle:

```text
|E_1 union E_2 union E_3| = 6.
```

The second is the pinched triangle:

```text
|E_1 union E_2 union E_3| = 5.
```

No other size pattern is possible: if two pair intersections both had size
`2`, the corresponding common point would force a nonempty triple
intersection.

## Four-Edge Pattern

The pairwise-coreless compiler already proves that if no three-edge subfamily
is coreless, then the four-edge obstruction is tetrahedral: the four edges are
the four 3-subsets of a 4-point set.

Thus `H3-NO-PAIRWISE-CORELESS` splits into:

```text
H3-NO-LOOSE-TRIANGLE
H3-NO-PINCHED-TRIANGLE
H3-NO-TETRAHEDRON
```

The later linear-hypergraph compiler proves that active edges cannot repeat a
coordinate pair.  Hence the pinched-triangle and tetrahedron cases are
automatic for active repeat-boundary edges, leaving only the loose-triangle
case.

## Guardrails

The verifier checks abstract models for all three obstruction patterns.  The
current finite witness rows remain stars, and the non-boundary contrast row
remains a disjoint-pair obstruction:

```text
p=337   n=16  kind=star pattern=star
p=2017  n=32  kind=star pattern=star
p=4801  n=64  kind=star pattern=star
p=7937  n=64  kind=star pattern=star
p=65537 n=256 kind=star pattern=star
p=91393 n=256 kind=star pattern=star
p=97    n=32  kind=disjoint_pair pattern=has_disjoint_pair
```

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_coreless_pattern_compiler.py
```

Expected digest:

```text
H3_REPEAT_CORELESS_PATTERN_COMPILER_PASS
```
