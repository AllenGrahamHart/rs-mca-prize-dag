# Cycle 325: MCA rank-11 rank-nine weighted target elimination (2026-08-14)

Three PROVED nodes retain the component extension weight that cycle 322
discarded when it selected `2578110` distinct records.

First,
`rate_half_mca_rank11_component_ninesubset_weighted_concentrator` marks all
55 nine-subsets of every typed component eleven-subset and averages before
deduplication. One fixed `B` carries

```text
W_B >=ceil((495405467/10^9) N_min
           *C(m',9)*C(m'-9,2)/C(n',9)).
```

Even at `K'=10`, this is `5868470021012020` marked `(record,T)`
incidences. Dividing by `C(m'-9,2)` recovers the old `2578110` record
floor, but the new route keeps the numerator.

Second, `rate_half_mca_rank11_rank9_weighted_component_cap` charges every
rank-ten extension of a fixed rank-nine `B` to its unique owner point.
At least one of the two added coordinates lies in that point's petal. A
point owns at most `981105` records, its core has size below `m'`, and the
plane petals are disjoint. Hence

```text
W_B <=981105*(m'-10)*n'.
```

Finally,
`rate_half_mca_rank11_rank9_weighted_target_elimination` closes the complete
rank-nine alternative. Its `2578110` records already force a common plane
core of size at least `134944`. For `K'<=67472`, this contradicts strict
owner-core size below `m'`. For `K'>=67473`, the weighted comparison at the
boundary is

```text
6849288576200976639 > 147748596828055575,
gap = 6701539979372921064.
```

After cancelling `C(m'-9,2)`, the demand-to-cap ratio is a constant times
`C(m',9)/C(n',9)*(m'-9)/n'`; every factor increases with `K'`. Thus the
boundary contradiction is uniform through `K'=1048576`.

The cycle also rejected a candidate `134931` two-terminal overlap node: the
calculation was weaker than direct inclusion-exclusion and its first draft
overstated the selected-support/core relation. It was not registered.

Focused verification:

```text
RATE_HALF_MCA_RANK11_COMPONENT_NINESUBSET_WEIGHTED_CONCENTRATOR_PASS
  marked=5868470021012020 distinct=2578110 controls=6/6
RATE_HALF_MCA_RANK11_RANK9_WEIGHTED_COMPONENT_CAP_PASS
  owner=981105 boundary_cap=147748596828055575 controls=6/6
RATE_HALF_MCA_RANK11_RANK9_WEIGHTED_TARGET_ELIMINATION_PASS
  demand=6849288576200976639 cap=147748596828055575
  gap=6701539979372921064 controls=8/8
```

No Modal computation was used.

```text
DAG delta:             +3 PROVED weighted rank-eleven nodes,
                       +5 requirement edges, +3 evidence edges
critical status delta: none
rank-eleven delta:     fixed rank-nine component target eliminated
remaining target:     fixed kernel chart or rank-eight owner flat
delta-star movement:   none
compute:               constant-memory exact integer arithmetic only
next route action:     retain extension weight in the fixed-kernel and
                       rank-eight branches
```
