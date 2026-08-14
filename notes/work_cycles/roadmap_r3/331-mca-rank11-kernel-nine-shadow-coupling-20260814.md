# Cycle 331: MCA rank-11 kernel nine-shadow coupling (2026-08-14)

Two PROVED nodes couple all kernel coranks through one support resource.

For a corank-`d` eleven-set, duality sends spanning nine-subsets to
independent pairs in a coloopless rank-`(d+1)` matroid. Parallel-class
counting gives at least

```text
C(d+2,2)
```

such shadows. A fixed rank-`(10-d)` nine-subset has at most
`C(K'-d-9,2)` same-rank eleven-set extensions, because its closure is the
common-zero set of a `d`-dimensional polynomial space. Thus every record
satisfies the joint inequality

```text
sum_d C(d+2,2) I_d/C(K'-d-9,2) <= C(m',9).
```

Combining this shadow budget with the existing ambient/record individual
caps gives an exact fractional-knapsack LP. Its weights increase with
corank, and an independent dual certificate reproduces the optimum.

Exact replay closes every row through `K'=15445`. At the endpoint the
demand-capacity gap is

```text
178044655461817065880792270525721984196903835342334290540589.
```

At `K'=15446`, capacity exceeds demand by

```text
124087038578417364551353992932097013573495323735890481286577,
```

so the one-shadow method stops honestly. The optimizer fills all of
corank 1, stops inside corank 2, and allocates zero to higher coranks.

Focused verification on Modal:

```text
RATE_HALF_MCA_RANK11_KERNEL_NINE_SHADOW_COUPLING_PASS
  sharp_models=9 coefficient_sum=219 controls=5/5
RATE_HALF_MCA_RANK11_KERNEL_NINE_SHADOW_COUPLING_AUDIT_PASS
  coranks=9 first=3 last=55
RATE_HALF_MCA_RANK11_KERNEL_NINE_SHADOW_CAPACITY_CUT_PASS
  checked=15436 controls=7/7
RATE_HALF_MCA_RANK11_KERNEL_NINE_SHADOW_CAPACITY_CUT_AUDIT_PASS
  checked=15436 frontier=2 wall=15446
```

The four Modal jobs peaked at 54--57 MB each.

```text
DAG delta:             +2 PROVED nine-shadow nodes,
                       +3 requirement edges, +2 evidence edges
critical status delta: none
rank-eleven delta:     kernel lane removed for K'=10..15445
remaining intervals:  K'=10..15445 rank eight only;
                       K'=15446..22525 rank eight plus kernel;
                       K'=22526..37995 dense-owner chronology plus kernel;
                       K'=37996..1048576 kernel only
delta-star movement:   none
compute:               exact 15,436-row primal/dual replay on Modal
next route action:     add the compatible eight-subset shadow, whose
                       diagonal resource begins at corank 2
```
