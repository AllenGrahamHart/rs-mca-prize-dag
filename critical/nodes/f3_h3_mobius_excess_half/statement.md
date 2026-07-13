# C36' cutoff-18 weighted excess

- **status:** see `dag.json` (single source of truth)
- **legacy id:** `f3_h3_mobius_excess_half`

For every official row, define

```text
P(t)=#{(a,b) in A^2: ab=t},
R(t)=#{(c,d) in A^2: d/c=t},
X_18=sum_(t!=1) max(P(t)-18,0) R(t).
```

Then

```text
17 X_18 <= 300 n^2.                              (WX18)
```

This is the exact remaining premise after the identity fiber and the first
`18` units of every nonidentity quotient fiber are paid. It is weaker than the
former cutoff-35 statement `X_35<=n^2/2`, which implies `(WX18)` by the proved
cutoff comparison.

The proved `f3_h3_rich_fiber_norm_cutoff` theorem gives `X_18=0` whenever
`p>6^(n/4)`. Thus the universal statement remains open only for
`n^2<=p<=6^(n/4)`.
