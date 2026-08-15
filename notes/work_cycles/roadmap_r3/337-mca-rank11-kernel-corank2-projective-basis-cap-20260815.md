# Cycle 337: MCA rank-11 corank-two projective-basis cap (2026-08-15)

Two PROVED nodes sharpen the corank-two record cap by a projective-basis
count and move the exact kernel cutoff from `K'=377673` to `K'=568338`.

In the complete shortened explanation-dimension-two chart,

```text
(n,K,m,s)=(1048578,2,67474,2).
```

Support-local transversality leaves no zero normals.  Its one-span MDS step
puts at least `67473=m-1` incident normals outside every projective class,
so all `m` incident projective points are distinct.  Pair noncontainment
makes the incident normal span three-dimensional, hence the projective set
is noncollinear.

For a line containing `q>=2` of these points and `r=m-q>=1` points off it,
the number of collinear triples is at most

```text
C(q,3)+C(r,3)+C(r,2)=C(q,3)+C(r+1,3)<=C(m-1,3).
```

Thus every record owns at least

```text
m(m-1)(m-2)-6C(m-1,3)=3(m-1)(m-2)=13657614768
```

ordered independent coordinate triples.  Double counting gives

```text
M_2<=floor(n(n-1)(n-2)/(3(m-1)(m-2)))=84416263,
```

with remainder `2935655472`.  The prior generic cap `253241283` falls by
`168825020` records.

With `M_1=8147918` and this new `M_2`, the exact kernel optimizer has cap
roots `d=1,2` and tree

```text
(2,3), (2,4), (2,6), (2,8), (3,5), (2,7), (2,9).
```

All remaining coranks are positive tree multiples.  Both shared resources
and all nonroot individual caps are strict; 17 hierarchy rows are tight.
Positive backward-tree dual prices certify exact optimality.

A 64-worker exact Modal replay checked every row
`377674<=K'<=568339`.  All `190666` rows completed under the
60-second/256-MB worker policy, with 57 MB observed peak memory and 112.10
aggregate worker-seconds.

At `K'=568338`, demand exceeds floored capacity by

```text
38432453444617070485037263551626410396462586389410416394578520596038.
```

At `K'=568339`, capacity exceeds demand by

```text
36180877960369511460476382880286784896208001102094988739728829832800.
```

Focused verification:

```text
RATE_HALF_MCA_RANK11_KERNEL_CORANK2_PROJECTIVE_BASIS_CAP_PASS
  cap=84416263 bases=13657614768 improvement=168825020 controls=7/7
RATE_HALF_MCA_RANK11_KERNEL_CORANK2_PROJECTIVE_BASIS_CAP_AUDIT_PASS
  splits_checked=67472 cap=84416263 remainder=2935655472
RATE_HALF_MCA_RANK11_KERNEL_CORANK2_PROJECTIVE_CAPACITY_CUT_PASS
  checked=190666 wall=568339 controls=6/6
RATE_HALF_MCA_RANK11_KERNEL_CORANK2_PROJECTIVE_CAPACITY_CUT_AUDIT_PASS
  checked=190666 endpoints=3 chunks=64
```

```text
DAG delta:             +2 PROVED projective-basis nodes,
                       +5 requirement edges, +2 evidence edges
critical status delta: none
rank-eleven delta:     kernel lane removed for K'=377674..568338
remaining intervals:  K'=10..22525 rank eight only;
                       K'=22526..37995 dense-owner chronology only;
                       K'=37996..568338 no rank-eleven component target;
                       K'=568339..1048576 kernel only
delta-star movement:   none
compute:               exact 190,666-row replay on 64 bounded Modal workers
next route action:     seek a projective-frame strengthening in corank three
                       or a binding hierarchy-edge improvement; separately
                       harvest rank eight and chronology-only lower intervals
```
