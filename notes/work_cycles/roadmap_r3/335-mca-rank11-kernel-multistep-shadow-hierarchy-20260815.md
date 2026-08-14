# Cycle 335: MCA rank-11 multi-step shadow hierarchy (2026-08-15)

Two PROVED nodes generalize the two-step pair count to every shadow size and
move the exact kernel cutoff from `K'=18101` to `K'=18158`.

For one exact support, let `I_d` count rank-`(10-d)` eleven-subsets.  For
`3<=d<=9` and `2<=t<=d-1`, define

```text
s_(d,t)=C(d+2,t),               L_(d,t)=C(67472+d,t),
E_(d,t)=C(K'-d-11+t,t),        Q_(d,t)=C(9-d+t,t).
```

The dual of a loopless rank-`(10-d)` eleven-set is coloopless of rank `d+1`.
If `f_j` counts its independent `j`-sets, every independent `j`-set has at
least `d-j+2` extensions; otherwise the elements outside its closure would
be coloops.  Thus

```text
(j+1)f_(j+1)>=(d-j+2)f_j,
f_t>=C(d+2,t).
```

These independent `t`-sets are complementary spanning shadows.  One fixed
shadow has at most `E_(d,t)` same-rank extensions.  Conversely, successive
generalized-MDS closure caps force at least `L_(d,t)` support `t`-sets that
raise rank by `t`.  A rank-`(10-d+t)` target contains at most `Q_(d,t)`
source shadows because their complementary `t`-sets must consist of coloops.
Therefore all 28 inequalities

```text
(s_(d,t)L_(d,t)/E_(d,t)) I_d <= Q_(d,t) I_(d-t)
```

hold support-by-support.  The six new triple rows cut the old `K'=18102`
optimizer; its `d=5,7,9` rows were violated by a factor about `3.083935`.
The higher-step rows are consistency consequences at the new optimum and do
not improve the finite LP beyond `t=2,3`.

The exact finite certificate has two hierarchy components.  The corank-one
cap fixes `{1,3}` through `H_(3,2)`.  A seven-vertex tree rooted at corank two
uses edges

```text
(2,4), (2,6), (2,8), (3,5), (2,7), (2,9),
```

where each pair is `(t,d)`.  Full containment fixes that component.  Exact
Gaussian and independent backward-tree duals agree on all 58 rows
`18102..18159`.

At `K'=18158`, demand exceeds floored capacity by

```text
289110608820324799941118306538399899258195112067661304310498.
```

At `K'=18159`, capacity exceeds demand by

```text
20286290696334777989469267474876769475675508046109372076445.
```

Focused verification on Modal:

```text
RATE_HALF_MCA_RANK11_KERNEL_MULTISTEP_SHADOW_HIERARCHY_PASS
  couplings=28 triples=6 controls=4/4
RATE_HALF_MCA_RANK11_KERNEL_MULTISTEP_SHADOW_HIERARCHY_AUDIT_PASS
  couplings=28 recurrences=35
RATE_HALF_MCA_RANK11_KERNEL_THREE_STEP_SHADOW_CAPACITY_CUT_PASS
  checked=58 controls=6/6
RATE_HALF_MCA_RANK11_KERNEL_THREE_STEP_SHADOW_CAPACITY_CUT_AUDIT_PASS
  checked=58 wall=18159 tree_edges=7
```

The four jobs peaked at 54--56 MB.  A 4,424-row float sweep on Modal was used
only to discover the active tree and crossing; all status-bearing arithmetic
is exact.

```text
DAG delta:             +2 PROVED multi-step shadow nodes,
                       +4 requirement edges, +2 evidence edges
critical status delta: none
rank-eleven delta:     kernel lane removed for K'=18102..18158
remaining intervals:  K'=10..18158 rank eight only;
                       K'=18159..22525 rank eight plus kernel;
                       K'=22526..37995 dense-owner chronology plus kernel;
                       K'=37996..1048576 kernel only
delta-star movement:   none
compute:               exact 58-row primal/dual replay on Modal
next route action:     attack the stable K'=18159 tree wall by strengthening
                       a binding edge, full containment, or the corank-one cap,
                       or by adding a genuinely independent resource
```
