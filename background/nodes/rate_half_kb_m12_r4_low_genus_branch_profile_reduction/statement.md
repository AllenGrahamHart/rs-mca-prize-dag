# KoalaBear m12 r4 low-genus branch-profile reduction

- **status:** PROVED
- **scope:** inner-degree-12 transverse type `(r,delta)=(4,12)`
- **dependency:** `rate_half_kb_m12_outer_subdegree_route_cut`
- **consumer:** `rate_half_band_closure`

Let `C` be the geometrically irreducible outer component of bidegree
`(4,4)`, and let `Gamma -> C` be the degree-12 map emitted by the transverse
compiler. The actual component is birational to a bidegree-`(2,4)` curve, so
its normalization has genus at most three. Riemann-Hurwitz therefore forces

```text
genus(C)<=1.                                         (KB4-1)
```

The unique total pole makes the outer degree-five map a tame polynomial.
Its infinity branch cycle is a 5-cycle and its finite branch-cycle indices
sum to four. An exhaustive exact enumeration in `S_5`, with the off-diagonal
ordered-pair genus replayed independently, leaves exactly five profiles:

```text
geometric group   finite branch-cycle types       genus(C)
A5                (3), (2,2)                         0
A5                (3), (3)                           1
S5                (2), (3,2)                         0
S5                (2), (4)                           0
S5                (2), (2), (2,2)                   1
```

Here `(e1,...,es)` denotes disjoint cycle lengths in one finite branch
cycle. The tame affine group `AGL(1,5)` cannot occur. The only other
two-transitive degree-five polynomial profiles have off-diagonal genus two
or three and are impossible by `(KB4-1)`.

This finite classification does not eliminate the five profiles, close
`r=4` or `m=12`, construct an owner, move the ledger, close `u=2`, establish
cap `68`, or close the KoalaBear row.

## Falsifier

A tame degree-five polynomial branch tuple with infinity cycle type `(5)`,
finite index sum four, two-transitive monodromy, off-diagonal genus at most
one, and a profile outside the five printed rows.
