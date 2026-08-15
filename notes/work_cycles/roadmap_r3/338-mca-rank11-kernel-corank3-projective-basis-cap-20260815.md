# Cycle 338: MCA rank-11 corank-three projective-basis cap (2026-08-15)

Two PROVED nodes sharpen the corank-three record cap by a projective-basis
count and move the exact kernel cutoff from `K'=568338` to `K'=796598`.

In the complete shortened explanation-dimension-three chart,

```text
(n,K,m,s)=(1048579,3,67475,3).
```

Support-local transversality leaves no zero normals.  Its one-span MDS step
makes all `m` projective normals distinct, and its two-span step permits at
most two points on any projective line.  Pair noncontainment supplies full
normal rank, so this no-three-collinear point set spans `PG(3)`.

Choose a plane containing `q>=3` support points and put `r=m-q>=1`.  The
number of coplanar quadruples is at most

```text
B(q,r)=C(q,4)+floor(q/2)C(r,2)+2C(r,3)+C(r,4).
```

The two-middle split requires care: for a fixed outside pair, its line meets
the chosen plane outside the point set, and secants through that intersection
use disjoint point pairs.  Vandermonde expansion gives

```text
C(m-1,4)-B(q,r)
  =(q-3)C(r,3)
   +(C(q-1,2)-floor(q/2))C(r,2)
   +(r-1)C(q-1,3) >= 0.
```

Thus every record owns at least

```text
(m)_fall_4-24C(m-1,4)
  =4(m-1)(m-2)(m-3)
  =1228711865141376
```

ordered independent coordinate quadruples.  Double counting gives

```text
M_3<=floor((n)_fall_4/(4(m-1)(m-2)(m-3)))=983902549,
```

with remainder `1056607358217600`.  The prior generic cap `3935435218`
falls by `2951532669` records.

With `M_1=8147918`, `M_2=84416263`, and this new `M_3`, the exact kernel
optimizer has cap roots `d=1,2,3` and forest

```text
(2,4), (2,5), (3,6), (4,7), (5,8), (6,9).
```

All remaining coranks are positive forest multiples.  Both shared resources
and all nonroot individual caps are strict; 12 hierarchy rows are tight.
Positive backward-forest dual prices certify exact optimality.

A 64-worker exact Modal replay checked every row
`568339<=K'<=796599`.  All `228261` rows completed under the
60-second/256-MB worker policy, with 59 MB observed peak memory and 144.68
aggregate worker-seconds.

At `K'=796598`, demand exceeds floored capacity by

```text
1063274038253455766288412818872693782800681544679740581002823089126086.
```

At `K'=796599`, capacity exceeds demand by

```text
670721678337441589385303494237372283642375643589068751593971045368244.
```

Focused verification:

```text
RATE_HALF_MCA_RANK11_KERNEL_CORANK3_PROJECTIVE_BASIS_CAP_PASS
  cap=983902549 bases=1228711865141376 improvement=2951532669 controls=8/8
RATE_HALF_MCA_RANK11_KERNEL_CORANK3_PROJECTIVE_BASIS_CAP_AUDIT_PASS
  splits_checked=67472 cap=983902549 remainder=1056607358217600
RATE_HALF_MCA_RANK11_KERNEL_CORANK3_PROJECTIVE_CAPACITY_CUT_PASS
  checked=228261 wall=796599 controls=8/8
RATE_HALF_MCA_RANK11_KERNEL_CORANK3_PROJECTIVE_CAPACITY_CUT_AUDIT_PASS
  checked=228261 endpoints=3 chunks=64
```

```text
DAG delta:             +2 PROVED projective-basis nodes,
                       +5 requirement edges, +2 evidence edges
critical status delta: none
rank-eleven delta:     kernel lane removed for K'=568339..796598
remaining intervals:  K'=10..22525 rank eight only;
                       K'=22526..37995 dense-owner chronology only;
                       K'=37996..796598 no rank-eleven component target;
                       K'=796599..1048576 kernel only
delta-star movement:   none
compute:               exact 228,261-row replay on 64 bounded Modal workers
next route action:     seek a projective-frame strengthening in corank four
                       or a binding hierarchy-edge improvement; separately
                       harvest rank eight and chronology-only lower intervals
```
