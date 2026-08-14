# Cycle 310: MCA rank-11 global-core rank-drop router (2026-08-14)

The new PROVED node
`rate_half_mca_rank11_global_core_rankdrop_highcomplexity_router` resolves
most of Cycle 309's line-global `(C)` output.

After exact global-core cancellation, the dense minimizing pair descends and
the deviation space keeps its dimension `r`. The shortened row has

```text
(n',K',m')=(R+K',K',d+K'),
(R,d)=(1048576,67472).
```

For `r<=8`, every variable transversality endpoint has a one-turn successive
ratio in `K'`, so its maximum occurs at `K'=r` or the deployed `K`. The
largest result, including the disjoint near charge, is

```text
110390969172308040 < 274980728111395087.
```

For `r=9`, the `T=667` margin/interleaving terms are constant in `K'` except
for the same endpoint-controlled high term. The deployed endpoint is worst:

```text
high  = 5143522968716559
low   = 56727790457914040
near  = 134944
total = 61871313426765543 < B_*.
```

Only `r=10` survives. On the shortened domain, eighteen dense-pair records,
ten deviation-basis records, and three fillers give one fixed 31-anchor deck
with empty maximal intersection. Every target tuple has slope degree
`18..31`. If one is high-complexity it becomes the explicit relative label
`(H_C)`. Otherwise the scalar-locator certificates lift and cohere into one
root-free rational atom `(A)`, or a pure-locator, denominator-root, or
collision/near-sunflower exception `(E)`.

The lift identities are exact:

```text
chi=chi'+2c,
3m'-K'+3+2c=3m-K+3=2299571,
g31'=g31-c.
```

`(H_C)` is not promoted to deployed first-match `(S)`, because its original
supports retain the nonempty line-global factor. This is now the only
rank-eleven-specific common-core obstruction.

Focused verification:

```text
RATE_HALF_MCA_RANK11_GLOBAL_CORE_RANKDROP_HIGHCOMPLEXITY_ROUTER_PASS
  r8=110390969172308040 r9=61871313426765543 core=12345 controls=7/7
RATE_HALF_MCA_RANK11_GLOBAL_CORE_RANKDROP_HIGHCOMPLEXITY_ROUTER_AUDIT_PASS
  g31prime=1071000 routes=4 controls=5/5
```

No Modal computation was used. The canonical Fable tree remained clean at
`659319780`. Upstream's newest relevant open stack remains PRs `#1163` to
`#1168`; none pays or isolates this relative high-complexity branch.

```text
start:                   d6d72ac65
DAG delta:               +1 PROVED rank-drop/high-complexity router,
                         +5 requirement edges, +1 evidence edge
critical status delta:   none
upstream terminal delta: C reduced to paid rank drop or H_C/A/E
delta-star movement:     none
compute:                 exact local endpoint arithmetic only
next route action:       pay or transport H_C without treating it as S;
                         A/E remain shared upstream terminals
```
