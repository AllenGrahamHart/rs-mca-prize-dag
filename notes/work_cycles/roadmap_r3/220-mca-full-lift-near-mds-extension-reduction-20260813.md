# Cycle 220: MCA full-lift near-MDS extension reduction (2026-08-13)

Cycle 219 isolated the top explanation-rank branch with lifted/error rank
`K+1`.  This cycle identifies its exact code-theoretic object.

Put

```text
W=C+span{r_1},       e=min_(b in C) wt(r_1-b).
```

Pair noncontainment gives `r_1 notin C`, so `W` has dimension `K+1`.
Interpolation proves `e<=N-K`.  The complete generalized-weight hierarchy is

```text
d_1(W)=e,
d_j(W)=N-K+j-1       for 2<=j<=K+1.
```

For `j>=2`, every `j`-space not contained in `C` meets `C` in dimension
`j-1`; the RS MDS hierarchy gives the generalized Singleton lower bound,
which is therefore exact.  Thus the extension is near-MDS with exactly one
defective generalized weight.

The full-lift selected errors form a full-affine-rank weight-`<=N-m` list in
one affine coset of `W`.  Error-to-slope projection has fiber one, and
same-support pair noncontainment is equivalent to injectivity of restriction
`W->F^S` on every selected maximal zero set.

Substituting the hierarchy into the corrected compiler recovers its top-rank
bound.  Even at the best endpoint `e=N-K`, where `W` is MDS, the exact values
remain over budget:

```text
KoalaBear:   743896698428332665 > 274980728111395087;
Mersenne-31:          219426634 >          16777215.
```

The primary verifier checks rank-one-defect and MDS extensions over `GF(7)`,
both official ceilings, and three mutations.  An independent `GF(5)` audit
exhausts all 31 codimension-one extensions of `RS[GF(5),5,2]`; every one has
weights `(e,4,5)`, with distance profile `[(1,5),(2,25),(3,1)]`.

```text
start:                   878571558
canonical prize:         c8d48cd4b (no newer Fable commit)
upstream main:           93fba1be
open frontier PRs:       #1163, #1164, #1165; no newer MCA frontier PR
upstream export head:    #1165 @ f966e38c
result:                  NARROWED + EXPORTED; one PROVED near-MDS reduction
DAG delta:               +1 PROVED node, +3 edges
critical status delta:   none; replacement target remains TARGET
upstream terminal delta: near-MDS theorem, exhaustive 31-extension audit,
                         and compiler-ceiling route fence added to #1165;
                         all-LineRay consequence posted to #1164
delta-star movement:     none
compute:                 exact bounded local arithmetic under RAMguard
next route action:       seek a row-sharp sparse-list theorem using the
                         codimension-one RS extension beyond its weight
                         hierarchy, or a chronology-correct S/A/E route
```
