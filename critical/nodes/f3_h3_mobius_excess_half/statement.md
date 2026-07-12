# f3_h3_mobius_excess_half

- **status:** see `dag.json` (single source of truth)

For every official row, define

```text
P(t)=#{(a,b) in A^2: ab=t},
R(t)=#{(c,d) in A^2: d/c=t},
X_35=sum_(t!=1) max(P(t)-35,0) R(t).
```

Then

```text
X_35 <= n^2/2.                                    (WX35)
```

Unlike the background pointwise cap, `(WX35)` permits fibers larger than
`35` and prices only their actual quotient-weighted excess.
