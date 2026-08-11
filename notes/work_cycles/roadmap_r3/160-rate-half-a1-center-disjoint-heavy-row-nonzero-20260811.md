# Cycle 160: rate-half `A=1` center-disjoint heavy row is nonzero (2026-08-11)

On the separated double-root locus with

```text
gcd(Lambda,g_*S_B^2)=1,
```

the Cycle-157 scalar cannot vanish. If `G(t,x_*)=0`, then `X-x_*` divides
`G`. At a root of `S_B`, the row `Q(t,x_*)` has order three.

- If the correction slope is unsupported, this contradicts the exact
  resultant order two from `E_4=S_B^2`.
- If `x_*` is an actual-support root, local intersection order at least
  three contradicts first-jet transversality.
- If `x_*` is padding, the slope belongs to `g_*`, contradicting
  `gcd(g_*,S_B)=1`.

Therefore

```text
G(t,x_*)=c g_*S_B^2,       c!=0.
```

```text
result:                  PROVED nonzero center-disjoint heavy row
DAG delta:               +1 PROVED leaf, 4 req edges
critical status delta:   none
compute:                 local valuation replay only; no Modal spend
new assumptions:         none beyond center-disjoint separated locus
```

The center-disjoint augmented gate now targets one exact projective row;
the zero row is removed. Center/correction overlap cases remain indexed by
`1<=j<=3`.
