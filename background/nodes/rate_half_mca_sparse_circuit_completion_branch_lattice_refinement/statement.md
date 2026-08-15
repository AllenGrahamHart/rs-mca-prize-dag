# Completion-branch lattice refinement

- **status:** PROVED
- **correction dimension:** `10`

Let an existing sparse-circuit branch retain any collection of valid support
caps.  Put `q=K-10>=8`, choose another source support `2<=c<=9`, and let
`M_c` be its maximum deletion-completion count.  The branch may be replaced
by the disjoint exhaustive leaves

```text
M_c=q-s,                 0<=s<=9-c,                (BL1)
M_c<=q-(10-c).                                      (BL2)
```

On a terminal leaf, intersect the inherited caps with source ceiling `q-s`
and every cross-support carrier satisfying

```text
c+(s+1)d-s-1<=10.                                  (BL3)
```

On the fallback leaf, intersect with source ceiling `q-(10-c)`.  Thus one
branch is replaced by exactly `11-c` valid leaves.  Refinements may be
repeated on selected leaves, producing a finite branch lattice without
discarding inherited constraints.

## Falsifier

A completion maximum omitted from `(BL1)`--`(BL2)`; overlapping leaves;
loss of an inherited cap; or use of a cross-support carrier when `(BL3)`
fails.
