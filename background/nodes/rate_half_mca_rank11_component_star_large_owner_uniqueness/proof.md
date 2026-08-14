# Proof

Let two owner pairs `p=(a,b)` and `q=(a',b')` own the same record of slope
`gamma`, and let their within-support pair cores be

```text
A_p=S intersect {r_0=a,r_1=b},
A_q=S intersect {r_0=a',r_1=b'}.
```

Assume both deficiencies are at most `Delta=22320`. Inclusion-exclusion
inside `S` gives

```text
|A_p intersect A_q|
 >=2(m'-Delta)-m'
 =m'-2Delta
 =K'+22832.                                          (1)
```

If `p!=q`, at least one of `a-a'` and `b-b'` is a nonzero RS polynomial of
degree below `K'`. Every coordinate in `A_p intersect A_q` is a root of both
differences, and hence of that nonzero component. The RS root bound gives

```text
|A_p intersect A_q|<=K'-1,                           (2)
```

contradicting (1). Thus `p=q`.

The component-star router supplies an owner with deficiency at most `22320`
in its full-evaluation-rank branch. Applying the uniqueness just proved
shows that every choice of star ten-subset yielding such an owner gives the
same pair. The argument is uniform because `m'-K'=67472` is unchanged by
shortening.
