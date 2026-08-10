### 2026-08-10 FPC5 shifted-Johnson first-layout payment

The fixed-cell shifted-Johnson cap was compiled through the proved canonical
first-layout theorem. For any exact `(M,t,d)` cell, every later source-layout
member is one of the first layout's planted anchors, so the complete global
class is bounded by

```text
binom(M,t) W L_m(q)+M.
```

This removes the source-layout multiplier and pays the touched-set and
background-choice multipliers exactly. On the smallest official row, the
unique shifted cell at the first live scale of rates `1/2`, `1/4`, and `1/8`
is globally paid for `q>=2^228,2^233,2^220`, respectively. At rate `1/16`,
`M=61`, defects `248` and `292` are jointly paid for `q>=2^254`.

The aggregate audit is also route-deciding negatively: each of defects
`286,...,291` exceeds the prize budget after the exact `binom(61,3)` factor,
even at `q=2^256-1`. Four of these looked affordable at fixed-cell level, so
the outer replay prevents a false promotion.

Burn-down: result `NARROWED`; one PROVED compiler node added, selected
thin-strip cells receive complete source/touched aggregation, no critical
status changed, no assumptions added, and no Modal spend. The remaining
large-source work is now cleanly split between lower-field versions of the
same cells, six rate-`1/16` cells that need a stronger local bound, and the
dominant region `a^2<=N(K-1)` where Haboeck cannot apply at all.
