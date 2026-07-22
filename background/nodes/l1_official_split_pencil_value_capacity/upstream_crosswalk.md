# Upstream crosswalk - split-pencil value capacity

This is the direct specialization of the upstream moving-root bound for
one-parameter split pencils to

```text
L_[s:t](Z)=s(Z^p+Q(Z))-t.
```

The fixed domain part is empty because the second generator is `1`. Every
fully split finite member has `p` moving roots, so at most `floor(n/p)` such
parameters occur. Official arithmetic makes this at most 23.

For the local L1 first-checkpoint object this has an additional compiler
meaning: a fixed normalized `Q` supports at most 253 unordered collision
pairs. An upstream `(BC)` or split-pencil handoff should retain the theorem as
a proved preprocessing rung and present donated compute, if any, as a search
over canonical `Q` records. It should not spend an independent axis on the
two fiber values.

The exact compiler computes

```text
G_Q(T)=gcd_Zcoeff((Z^n-alpha) mod (Z^p+Q-T)).
```

This squarefree polynomial is precisely the split-value ledger and has degree
at most `floor(n/p)<=23`. Pair existence forces rank at most `m-1` in the
`p` by `(m+1)` remainder-coefficient matrix. A contributed implementation
should emit that matrix rank, `G_Q`, its roots, and direct divisibility checks
as the compact certificate for every retained `Q`. The theorem pays no part
of the number of `Q` records, and low rank without a nontrivial gcd is not a
positive record.

There is a theorem-level low-complement pruning before any computation. If
`2p>n`, no two `p`-point fibers fit in the domain. If `2p<=n<3p`, the
quadratic `G_Q(P)` divides `Z^n-alpha`; comparing its leading gap with the
degree-`n-2p` complement forces `deg Q>=3p-n`. In first-checkpoint depth
coordinates this deletes every `d>=n-p`. At `(n,p)=(8192,3583)`, contributor
work starts below `d=4609`, not at the ratio-only boundary `d=5599`.
