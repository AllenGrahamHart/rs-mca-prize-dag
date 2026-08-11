# Cycle 161: rate-half `A=1` zero heavy row forces full center overlap (2026-08-11)

The Cycle-160 valuation trichotomy applies at any squarefree correction root
outside the center divisor, not only when all center overlap is absent. Thus

```text
G(t,x_*)=0       => S_B|Lambda       => S_B|J and j>=2.
```

At a noncenter correction root, the zero row again forces an `X-x_*`
component. Unsupported slopes contradict exact resultant orders three versus
two; actual-support slopes contradict first-jet transversality; and padding
slopes contradict `gcd(g_*,S_B)=1`.

```text
result:                  PROVED full-overlap localization of zero rows
DAG delta:               +1 PROVED leaf, 4 req edges
critical status delta:   none
compute:                 local combinatorial replay only; no Modal spend
new assumptions:         none beyond the separated squarefree locus
```

All `j=0` and `j=1` configurations now have a nonzero heavy row. Only the
fully correction-centered cases `j=2,3` retain the zero-row possibility.
