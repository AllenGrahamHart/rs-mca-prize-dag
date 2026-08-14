# Cycle 322: MCA rank-11 component nine-subset concentration (2026-08-14)

Three focused PROVED nodes replace the recordwise component target by one
fixed populated chart.

First,
`rate_half_mca_rank11_component_ninesubset_lane_concentrator` chooses the
heavier of the full-rank affine-owner and rank-deficient kernel lanes. That
lane carries at least `495405467` parts per billion of all
record/eleven-subset incidences. Marking every nine-subset of each
eleven-subset and dividing by the exact maximum extension multiplicity gives

```text
C(11,9)*C(m',11)=C(m',9)*C(m'-9,2),
fixed-B records
 >=ceil((495405467/10^9)*274980728111260126
        *C(m',9)/C(n',9)).
```

The product ratio increases with `K'`, so its uniform endpoint is `K'=10`:

```text
fixed-B records >=2578110.
```

Second, `rate_half_mca_rank11_rank9_ninecell_paircore_extension` checks the
scope needed by this selector. With only nine fixed common coordinates, the
low-core ordered-pair resource becomes

```text
981105*(2097152-9)=2057517483015.
```

The adjacent quadratic bracket is unchanged:

```text
1434405*1434404 <=2057517483015
                 <1434406*1434405.
```

Thus a rank-nine nine-cell plane still has at most `1434405` records unless
it shares at least `134944` received coordinate pairs.

Finally, `rate_half_mca_rank11_component_ninesubset_target_router`
classifies the fixed population. In the kernel lane it gives one fixed
nonzero ambient evaluation kernel. In the affine-owner lane, restriction of
a rank-ten eleven-set to nine coordinates has rank eight or nine. Rank nine
exceeds the plane cap by

```text
2578110-1434405=1143705
```

and therefore forces the shared pair core. At rank eight, all selected
owners lie in one affine `U^2` flat with `dim U=2`; after anchoring one
slope, all selected error differences lie in `span(U,r_1-B_*)`, so their
affine error rank is at most three.

Focused verification:

```text
RATE_HALF_MCA_RANK11_COMPONENT_NINESUBSET_LANE_CONCENTRATOR_PASS
  lane_ppb=495405467 endpoint=2578110 controls=6/6
RATE_HALF_MCA_RANK11_COMPONENT_NINESUBSET_LANE_CONCENTRATOR_AUDIT_PASS
  endpoint=2578110 factors=9
RATE_HALF_MCA_RANK11_RANK9_NINECELL_PAIRCORE_EXTENSION_PASS
  ordered=2057517483015 cap=1434405 controls=6/6
RATE_HALF_MCA_RANK11_RANK9_NINECELL_PAIRCORE_EXTENSION_AUDIT_PASS
  core_checks=981104 resource=2057517483015 cap=1434405
RATE_HALF_MCA_RANK11_COMPONENT_NINESUBSET_TARGET_ROUTER_PASS
  population=2578110 excess=1143705 rank8_toy=3 controls=6/6
RATE_HALF_MCA_RANK11_COMPONENT_NINESUBSET_TARGET_ROUTER_AUDIT_PASS
  routes=3 population=2578110 excess=1143705
```

No Modal computation was used. The arithmetic and exhaustive owner-core
audit run in constant memory.

```text
start:                   0e547404a
DAG delta:               +3 PROVED target-concentration nodes,
                         +4 requirement edges, +1 evidence edge
critical status delta:   none
rank-eleven delta:       one typed fixed chart now carries >=2578110
                         records; rank-nine affine chart forces shared core
delta-star movement:     none
compute:                 exact local arithmetic only; no Modal spend
upstream delta:          PR #1170 first extended through pair-core plane
                         theorem at head 92e378a6a
next route action:       pay or recursively compress the fixed kernel chart,
                         shared-core plane, or rank-eight owner flat
```
