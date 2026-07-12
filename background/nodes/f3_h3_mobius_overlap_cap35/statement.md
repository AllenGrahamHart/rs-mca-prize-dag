# f3_h3_mobius_overlap_cap35

- **status:** see `dag.json` (single source of truth)
- **role:** stronger background sufficient route; not the critical premise

For every official row, let `A=(1-H)\{0}` and define

```text
P(t)=#{(a,b) in A^2: ab=t},
R(t)=#{(c,d) in A^2: d/c=t}.
```

Then

```text
max {P(t): t != 1 and R(t)>0} <= 35.              (M35)
```

Writing `a=1-x` and `b=1-y`, `P(t)` is the number of points of
`H^2` on the Mobius involution

```text
y=(x+t-1)/(x-1).
```

The support restriction `R(t)>0`, equivalently `t in A/A`, is part of the
claim and should be retained in any proof attempt.
