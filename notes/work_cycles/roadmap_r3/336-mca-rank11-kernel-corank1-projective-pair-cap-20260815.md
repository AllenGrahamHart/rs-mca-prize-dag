# Cycle 336: MCA rank-11 corank-one projective-pair cap (2026-08-15)

Two PROVED nodes replace the generic corank-one transversality payment by a
sharp projective-pair incidence count and move the exact kernel cutoff from
`K'=18158` to `K'=377673`.

After canonical rank-nine basis cancellation, the corank-one chart is the
complete shortened row

```text
(n,K,m,s)=(1048577,1,67473,1).
```

The agreement normals lie in `F^2`.  The common-zero cap gives `z<=K-s=0`,
while same-support pair noncontainment forces the `m` incident normals of
each selected record to span `F^2`.  If their nonempty projective-class
sizes are `a_1,...,a_c`, then `c>=2` and the number of ordered independent
pairs is

```text
m^2-sum_i a_i^2 >= m^2-((m-1)^2+1)=2(m-1)=134944.
```

An independent coordinate pair determines at most one parameter point.
Double counting the `n(n-1)` ordered coordinate pairs therefore gives

```text
M_1 <= floor(n(n-1)/(2(m-1)))=8147918,
```

with remainder `29760`.  This lowers the previous generic cap `16295594`
by `8147676` records.

With this cap, the exact kernel LP has two active roots, `d=1` and `d=2`.
All remaining coranks are positive tree multiples of `d=1` along

```text
(2,3), (3,4), (2,5), (2,6), (2,7), (2,8), (2,9),
```

where each pair is `(t,d)`.  Both shared resources are slack; all nonroot
individual caps are slack; 22 of 28 hierarchy rows are exact equalities.
Positive backward-tree dual prices prove the allocation optimal.

A 64-worker exact Modal replay checked every row
`18159<=K'<=377674`, including all caps, both shared resources, all 28
hierarchy rows, primal-dual equality, and an independent direct-path optimum.
All `359516` rows completed under the 60-second/256-MB worker policy, with
57 MB observed peak memory.

At `K'=377673`, demand exceeds floored capacity by

```text
608290099077401798561583762592584078050381528604243813748500153228.
```

At `K'=377674`, capacity exceeds demand by

```text
1089804128361045148874283346879615159892995682385275039289561845323.
```

Focused verification:

```text
RATE_HALF_MCA_RANK11_KERNEL_CORANK1_PROJECTIVE_PAIR_CAP_PASS
  cap=8147918 pairs=134944 improvement=8147676 controls=6/6
RATE_HALF_MCA_RANK11_KERNEL_CORANK1_PROJECTIVE_PAIR_CAP_AUDIT_PASS
  classes_checked=67472 cap=8147918 remainder=29760
RATE_HALF_MCA_RANK11_KERNEL_PROJECTIVE_PAIR_CAPACITY_CUT_PASS
  checked=359516 controls=6/6
RATE_HALF_MCA_RANK11_KERNEL_PROJECTIVE_PAIR_CAPACITY_CUT_AUDIT_PASS
  checked=359516 endpoints=3 chunks=64
```

```text
DAG delta:             +2 PROVED projective-pair nodes,
                       +5 requirement edges, +2 evidence edges
critical status delta: none
rank-eleven delta:     kernel lane removed for K'=18159..377673
remaining intervals:  K'=10..22525 rank eight only;
                       K'=22526..37995 dense-owner chronology only;
                       K'=37996..377673 no rank-eleven component target;
                       K'=377674..1048576 kernel only
delta-star movement:   none
compute:               exact 359,516-row replay on 64 bounded Modal workers
next route action:     seek a projective-incidence strengthening of the
                       active corank-two cap, while separately harvesting
                       the rank-eight and chronology-only lower intervals
```
