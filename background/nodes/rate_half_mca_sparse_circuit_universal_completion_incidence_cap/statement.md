# Universal sparse-circuit completion incidence cap

- **status:** PROVED
- **correction dimension:** `10`
- **component subset size:** `11`
- **supported circuit sizes:** `2<=c<=9`

Let `V<=P_K=F[X]_<K` have dimension ten, put `q=K-10`, and let `S`
be a set of `m` distinct field points.  Suppose an eleven-set selected by a
record has evaluation rank ten on `V`, hence one circuit label in the
`q`-dimensional annihilator.

For an independent `(c-1)`-set `A`, let `b_A` be its number of support-`c`
circuit completions.  Then

```text
b_A<=q.                                                   (UC1)
```

If `I_c` counts selected rank-ten eleven-sets whose unique circuit has
support `c`, then

```text
I_c <=floor(C(m,c-1)/c
             * max_(0<=b<=q) b C(m-c+1-b,11-c)).          (UC2)
```

The statement is recordwise and requires no saturation/carrier branch.

## Falsifier

More than `q` completions of one independent deletion; an eleven-set
retaining two completion labels; a selected support-`c` incidence omitted
from all `c` deletion charges; or an incidence count above `(UC2)`.
