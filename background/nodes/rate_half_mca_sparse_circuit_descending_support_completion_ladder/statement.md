# Descending-support completion ladder

- **status:** PROVED
- **correction dimension:** `10`
- **source order:** `5,4,3,2`

Put `q=K-10>=8`.  For source support `c`, let `M_c` be the maximum
number of circuit completions of an independent `(c-1)`-deletion.  Starting
with `c=5` and descending through `4,3,2`, use the following partition:

```text
M_c=q-s for one 0<=s<=9-c,                         (DL1)
```

or retain the complementary bound

```text
M_c<=q-(10-c)                                      (DL2)
```

and continue to the next support.  This gives `5+6+7+8+1=27` disjoint,
exhaustive leaves.  At a terminal `(c,s)` leaf, every target support `d`
satisfying

```text
c+(s+1)d-s-1<=10                                  (DL3)
```

has the cross-support carrier cap, while the source support has deletion
ceiling `q-s`.  The final leaf has simultaneous deletion ceilings
`q-5,q-6,q-7,q-8` on supports `5,4,3,2`.

## Falsifier

A completion maximum omitted from the 27 leaves; overlapping leaves; a
terminal defect outside `0..9-c`; or use of a carrier cap when `(DL3)`
fails.
