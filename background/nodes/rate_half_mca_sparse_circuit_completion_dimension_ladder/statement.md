# Sparse-circuit completion ladder

- **status:** PROVED
- **correction dimension:** `10`
- **component subset size:** `11`
- **official specializations:** `14<=K'<=21`

Let `K>=13`, put `q=K-10`, and let `V<=P_K=F[X]_<K` have dimension ten
and no common zero on a set `S` of `m` distinct field points.  Every
eleven-set `T` on which `V` has evaluation rank ten selects one quotient
label and its minimal circuit support `C_T`.

For circuits with `2<=c=|C_T|<=5`, exactly one of the following alternatives
holds.

1. Every such circuit lies in one carrier `U` with `|U|<=q+4`.
2. Every independent `(c-1)`-set has at most `q-1` circuit completions, for
   every `2<=c<=5`.

Consequently the number `I_c` of rank-ten eleven-sets selecting a
support-`c` circuit is at most the larger of

```text
S_c=C(q+4,c) C(m-c,11-c),

U_c=floor(C(m,c-1)/c
          * max_(0<=b<=q-1) b C(m-c+1-b,11-c)).
```

On every official row `14<=K'<=21`, the maximum in `U_c` occurs at
`b=q-1`.

## Falsifier

More than `q` completions of one independent deletion; `q` completions
whose labels do not span the quotient; a sparse circuit outside the
resulting carrier; a rank-ten eleven-set retaining two completion labels;
or failure of either printed count.
