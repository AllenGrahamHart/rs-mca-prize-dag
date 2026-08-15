# Cycle 325: MCA rank-11 rank-nine weighted target route (scope repaired 2026-08-15)

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

The original cycle then claimed complete rank-nine elimination. That claim
mixed an original-row common-core floor with the residual support size after
reverse shortening. The lift inserts `1048576-K'` deleted coordinates into
every owner core, so an original-row core of size `134944` gives no such
residual-core floor. That low-row argument is retracted.

The weighted comparison itself is valid and has the earlier exact crossing

```text
K'=20617: 92386821615379573 < 92394042904582935,
K'=20618: 92397581841774591 > 92395178310909600.
```

After cancelling `C(m'-9,2)`, the demand-to-cap ratio is a constant times
`C(m',9)/C(n',9)*(m'-9)/n'`; every factor increases with `K'`. Thus rank
nine is closed on `20618<=K'<=1048576` and open here on `10<=K'<=20617`.

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
  last_gap=7221289203362 first_gap=2403530864991
  reopened=10..20617 controls=8/8
```

No Modal computation was used.

```text
DAG delta:             +3 PROVED weighted rank-eleven nodes,
                       +5 requirement edges, +3 evidence edges
critical status delta: none
rank-eleven delta:     rank nine eliminated only for K'>=20618
remaining target:     low-row rank-nine chart; rank-eight owner flat
delta-star movement:   none
compute:               constant-memory exact integer arithmetic only
next route action:     residual-unit owner-plane coupling below K'=20618;
                       retain extension weight in rank eight
```
