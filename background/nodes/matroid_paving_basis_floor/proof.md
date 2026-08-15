# Proof

Prove the slightly stronger induction that also permits `r=1`.  In rank
one there is at least one nonloop, hence at least one basis, which is
`C(m-1,0)`.  If `r>=2` and `m=r`, the whole ground set is the unique basis
and the bound is equality.

Suppose first that `M` has a coloop `e`.  The deletion `M minus e` has rank
`r-1`.  Every one of its `(r-1)`-subsets is independent by hypothesis and
is therefore a basis.  Adjoining `e` gives exactly

```text
C(m-1,r-1)
```

bases of `M`.

Otherwise choose any element `e`; it is not a coloop.  The deletion
`M minus e` has rank `r` and retains the independence hypothesis.  The
contraction `M/e` has rank `r-1`.  If a set `A` of at most `r-2` elements
were dependent in `M/e`, then `A union {e}`, of size at most `r-1`, would
be dependent in `M`, a contradiction.  Thus induction applies to both
minors.  Deletion-contraction for bases and Pascal's identity give

```text
b(M) = b(M minus e)+b(M/e)
     >= C(m-2,r-1)+C(m-2,r-2)
      = C(m-1,r-1).
```

The coloop construction in the statement attains the floor.
