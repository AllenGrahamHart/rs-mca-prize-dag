# Cycle 231: M31 boundary-anchor case split (2026-08-13)

The first unpaid Mersenne support was only `638658` above budget under the
mean-Gram/global-line profile. Exact decomposition showed that its final
boundary-layer increment alone costs `928560`.

Put `q=e-K-3 floor((e-K)/3)`. When `q>=1`, split on the size of the
already-synchronized top-third union `A`. If `|A|<=1`, charge the complete
prefix through `H` and one tail explanation. If `|A|>=2`, use two members of
`A` as anchors: every exact-`H` explanation has a mixed triple intersection
of size at least `K+q-1>=K`, so the whole boundary layer joins the same
affine line. This proves

```text
|Z| <= max(P_H+1,P_(H-1)+(N-m+1)).
```

At Mersenne `e=98230`, the two cases are `16434745` and `16487313`.
The latter is below budget by `289902`. At `e=98231`, the same legal theorem
gives `17492173`, over budget by `714958`; this is not unsafe.

```text
start:                   83fc2dd3a
canonical prize:         c8d48cd4b (no newer Fable commit)
upstream frontier:       #1163-#1166; #1166 @ af0e7c63b
result:                  NARROWED; one PROVED boundary compiler
DAG delta:               +1 PROVED node, +4 edges
critical status delta:   none; replacement target remains TARGET
full-lift residuals:     KoalaBear 96151<=e<=1044238;
                         Mersenne 98231<=e<=1044241
delta-star movement:     none
compute:                 two exact 65k-cap endpoint replays under RAMguard;
                         no Modal
next route action:       attack the support-local rank-10 exception-12
                         terminal, while screening whether a second M31
                         boundary layer admits a stronger small-tail split
export target:           extend existing przchojecki/rs-mca PR #1165
```
