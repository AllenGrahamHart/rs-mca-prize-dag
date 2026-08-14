# Cycle 321: MCA rank-11 rank-9 split-pencil pair-core dichotomy (2026-08-14)

The new PROVED node
`rate_half_mca_rank11_rank9_split_pencil_paircore_dichotomy` strengthens the
fixed-cell ledger after lifting one affine owner plane to the original row.

If two record lines meet at owner point `p`, their size-`m` supports intersect
in at least

```text
2m-n=134944
```

coordinates. The two distinct slope equalities recover both received
columns, so this complete intersection lies in the pair core `C_p`.

Let `J` be the common pair core of the owner plane and let `t_p` record lines
pass through `p`. In the low-common-core branch `|J|<134944`, fixed-owner
exception disjointness and the two-support floor give the exact ordered-pair
petal inequality

```text
t_p(t_p-1) <= 981105*|C_p minus J|.
```

The owner petals are pairwise disjoint. Doubling the block-design identity
therefore yields

```text
g(g-1) <= 981105*(2097152-|J|)
       <= 981105*(2097152-10)
        = 2057516501910,
g <= 1434405.
```

The adjacent integer `1434406` fails by `2636520`. Consequently every fixed
rank-nine owner plane satisfies an exact dichotomy:

```text
at most 1434405 records,
or one pair core of size at least 134944 shared by the whole plane.
```

If the rank-nine lane carries at least one third of the proved 98-percent
record floor, and every such plane stays in the low-core branch, it must use
at least `34541598583` distinct owner planes. This is a forced structural
alternative, not a plane-count contradiction.

Focused verification:

```text
RATE_HALF_MCA_RANK11_RANK9_SPLIT_PENCIL_PAIRCORE_DICHOTOMY_PASS
  intersection=134944 ordered=2057516501910 cap=1434405 controls=8/8
RATE_HALF_MCA_RANK11_RANK9_SPLIT_PENCIL_PAIRCORE_DICHOTOMY_AUDIT_PASS
  core_checks=981104 resource=2057516501910 cap=1434405 controls=5/5
```

The independent audit exhausts every possible official owner-core size in
the hardest low-core case. No Modal computation was used.

```text
start:                   3fb9452e3
DAG delta:               +1 PROVED pair-core dichotomy,
                         +1 requirement edge, +1 evidence edge
critical status delta:   none
rank-nine delta:         low-core plane cap improved from 45567658 to
                         1434405; larger plane forces shared core 134944
delta-star movement:     none
compute:                 981104 constant-memory integer checks locally
next route action:       aggregate the >=134944 shared-core planes or prove
                         a global census for the forced low-core plane atlas
```
