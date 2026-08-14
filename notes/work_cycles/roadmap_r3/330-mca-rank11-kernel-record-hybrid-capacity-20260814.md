# Cycle 330: MCA rank-11 kernel record/ambient hybrid capacity (2026-08-14)

Two PROVED nodes add a second summation order to the rank-deficient lane.

For one record with exact `m'`-support, all-bases decoration gives the
corank-`d` capacity

```text
P_d=floor(C(m',10-d) C(K'-10,d+1)/(d+2)).
```

This needs no multi-record cap `M_d`: a basis lies in the actual support,
and its remaining `d+1` tuple coordinates use the same `K'-10`
common-zero resource.

If `R_actual>=N_min` is the unknown actual residual record count, then each
stratum satisfies both `I_d<=A_d` from the ambient all-bases theorem and
`I_d<=R_actual P_d`. After division by `R_actual`, the minimum is
nonincreasing in the record count. It is therefore enough to evaluate

```text
sum_d min(A_d,N_min P_d)
```

against demand at `N_min`.

Exact replay closes every row through `K'=11772`. At the endpoint, the gap
is

```text
76504076505592948633027913576880724493595282142849410185084.
```

At `K'=11773`, capacity exceeds demand by

```text
139343682529231472322825521514042608524569163680782450618944.
```

The boundary takes the ambient branch for `d=1,2` and the record-support
branch for `d=3,...,9`. Both separate estimates have sharp abstract-matroid
models, so the next route must constrain simultaneous cross-stratum
saturation in one residual correction space.

Focused verification:

```text
RATE_HALF_MCA_RANK11_KERNEL_RECORD_SUPPORT_CAPACITY_PASS
  strata=9 multiplicities=3..11 controls=4/4
RATE_HALF_MCA_RANK11_KERNEL_RECORD_SUPPORT_CAPACITY_AUDIT_PASS
  strata=9 proof_pins=4/4
RATE_HALF_MCA_RANK11_KERNEL_HYBRID_CAPACITY_CUT_PASS
  checked=11763 controls=6/6
RATE_HALF_MCA_RANK11_KERNEL_HYBRID_CAPACITY_CUT_AUDIT_PASS
  checked=11763 branches=AARRRRRRR proof_pins=4/4
```

No Modal computation was used; both replays are constant-memory exact
integer arithmetic.

```text
DAG delta:             +2 PROVED kernel hybrid-capacity nodes,
                       +3 requirement edges, +2 evidence edges
critical status delta: none
rank-eleven delta:     kernel lane removed for K'=10..11772
remaining intervals:  K'=10..11772 rank eight only;
                       K'=11773..22525 rank eight plus kernel;
                       K'=22526..37995 dense-owner chronology plus kernel;
                       K'=37996..1048576 kernel only
delta-star movement:   none
compute:               exact 11,763-row replay, constant memory
next route action:     couple the d=1,2 ambient flats to the d>=3
                       record-support flat profile
```
