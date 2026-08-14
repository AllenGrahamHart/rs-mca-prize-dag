# Cycle 326: MCA rank-11 kernel canonical-basis capacity (2026-08-14)

Two PROVED nodes replace componentwise kernel payments by one summable
rank-stratified interface.

The structural node
`rate_half_mca_rank11_kernel_canonical_basis_globalizer` chooses one
canonical rank basis `B` for every rank-deficient eleven-subset. If
`r=rank(ev_T)` and `d=10-r`, all records assigned to the same `B` share one
quotient solution. After one affine translation and exact cancellation of
`B`, they form a single rank-`d` explanation family.

The remaining `d+1` coordinates of `T` are common zeros of the kernel
space. Generalized MDS leaves exactly the uniform resource

```text
at most K'-10 extra common zeros,
at most C(K'-10,d+1) extensions per record.
```

Thus one fixed basis carries at most
`M_d C(K'-10,d+1)` incidences. This is an aggregate chart cap, not a sum of
unrelated irreducible-component payments.

The capacity node
`rate_half_mca_rank11_kernel_rankstratified_capacity_cut` sums these caps
over the `C(n',10-d)` possible bases and all `d=1,...,9`. Exact replay of
all 4,589 residual dimensions proves that this total is below the dominant
kernel-lane demand for every

```text
10 <= K' <= 4598.
```

At the last closed row, the exact incidence gap is

```text
219272330501201744129177266158988707697316238048878827197685.
```

At `K'=4599` the capacity exceeds demand by

```text
95457494746881463288875361950515757435711627164872173764503,
```

so the method stops honestly. No extrapolation is made.

Focused verification:

```text
RATE_HALF_MCA_RANK11_KERNEL_CANONICAL_BASIS_GLOBALIZER_PASS
  ranks=9 rank9_cap=61871313426630599 controls=6/6
RATE_HALF_MCA_RANK11_KERNEL_CANONICAL_BASIS_GLOBALIZER_AUDIT_PASS
  pairs=9 proof_pins=4/4
RATE_HALF_MCA_RANK11_KERNEL_RANKSTRATIFIED_CAPACITY_CUT_PASS
  checked=4589 controls=6/6
RATE_HALF_MCA_RANK11_KERNEL_RANKSTRATIFIED_CAPACITY_CUT_AUDIT_PASS
  checked=4589 proof_pins=4/4
```

No Modal computation was used; both replays are constant-memory exact
integer arithmetic.

```text
DAG delta:             +2 PROVED kernel-capacity nodes,
                       +4 requirement edges, +2 evidence edges
critical status delta: none
rank-eleven delta:     kernel lane removed for K'=10..4598
remaining kernel wall: K'=4599..1048576
remaining target:     rank-eight owner flat at all K', plus kernel above wall
delta-star movement:   none
compute:               exact 4,589-row replay, constant memory
next route action:     build the rank-eight weighted owner-pair cap and
                       seek cross-basis compression above K'=4598
```
