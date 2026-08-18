# Proof

At the selected row, the proved full-span terminal partitions every
nontransverse slope first by its represented row space `U_e`; no slope is
owned twice. For a class `C_alpha` satisfying `(SC1)`, both coordinate
corrections of every assigned pair lie in the one direction space
`V_alpha`.

The ordinary affine-span theorem bounds the corresponding ordinary list by

```text
M_(d_alpha)
 = floor(C(n-K+d_alpha,d_alpha)/C(A-K+d_alpha,d_alpha)).
```

For every `d_alpha<=9`, `M_(d_alpha)^2<q`. The proved sub-square
interleaving collapse therefore leaves at most `M_(d_alpha)` ordered pair
types. Fixed-pair first-match ownership contributes at most `n-A` slopes per
type, so class `C_alpha` costs at most

```text
R_(d_alpha)=(n-A)M_(d_alpha).
```

The classes partition the represented row spaces and inherit their disjoint
slope ownership. Summing the class bounds proves `(SC2)`.

The complete transverse ledger is

```text
E_transverse=209812758437679617,
```

while `B_*=274980728111395087`. Hence `(SC2)<=L` implies a total at most
`B_*`, so an unsafe family must satisfy `(SC3)`.

At `n=2097152`, `K=1048576`, `A=1114369`, and `n-A=982783`, exact integer
evaluation gives

```text
d   M_d          R_d                 floor(L/R_d)+1
1   15           14741745            4420641497
2   253          248644099           262093370
3   4047         3977322801          16384884
4   64508        63397365764         1027929
5   1028035      1010335321405       64502
6   16382924     16100859197492      4048
7   261076837    256581877097371     254
8   4160438212   4088807947303996    16
9   66298487937  65157026870188671   2
```

These are the displayed uniform-cover thresholds. Two five-spaces cost
`2020670642810<L`. In a `2 x 5` presentation, every used factor slice `gB`
is one five-dimensional cover space, so at most `64501` such slices are paid.
QED.
