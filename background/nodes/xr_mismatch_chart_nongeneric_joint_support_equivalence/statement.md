# Mismatch-chart nongenericity equals a second joint support

- **status:** PROVED
- **consumer:** `xr_tangent_support_mismatch_bridge`

Fix a canonical full-external-zero mismatch chart with discrepancy support
`T`, external zero set `Z`, `d=|Z|`, locator `P_Z`, and scaled endpoints

```text
b_i=e_i/P_Z on T,       i=0,1.
```

Put `K'=K-d`, `A'=A-d`, and `r'=|T|-A'`. The chart is nongeneric at radius
`r'` -- that is, there are degree-below-`K'` polynomials `g_0,g_1` jointly
agreeing with `(b_0,b_1)` on at least `A'` points of `T` -- if and only if
there is a codeword pair

```text
c_i'=c_i+P_Z g_i in RS[D,K]
```

jointly explaining `(u,v)` on `Z union R` for some `R subseteq T`,
`|R|>=A-d`. This is an agreement support of size at least `A` containing
the full external zero set.

Moreover, supports belonging to distinct joint codeword-pair explanations
of the same received pair intersect in at most `K-1` coordinates. Thus every
recursive nongeneric chart lands in a genuine low-core family. The remaining
open issue is the slope-to-explanation fiber and its cross-chart aggregate.
