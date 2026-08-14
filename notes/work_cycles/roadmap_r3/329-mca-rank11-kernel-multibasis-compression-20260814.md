# Cycle 329: MCA rank-11 kernel multi-basis compression (2026-08-14)

Two PROVED nodes recover basis multiplicity discarded by the canonical
kernel assignment.

For a corank-`d` eleven-set `T`, the restricted evaluation matroid has rank
`10-d` and no loops. Fixing one basis and applying fundamental-circuit
exchange to every outside element gives at least

```text
1+(11-(10-d))=d+2
```

distinct bases. Decorating each `(record,T)` incidence by all of its bases
does not change the existing fixed-basis capacity. Dividing the decorated
count by this guaranteed multiplicity improves the corank-`d` term to

```text
floor(C(n',10-d) M_d C(K'-10,d+1)/(d+2)).
```

The factor is sharp under looplessness alone: `9-d` coloops together with
one parallel class of size `d+2` has exactly that many bases.

Exact independent replay of the resulting nine-stratum capacity closes
every row through `K'=11641`. At the endpoint the demand-capacity gap is

```text
17769453550459149385453824948016076737082337523706893862084.
```

At `K'=11642`, capacity exceeds demand by

```text
187031323586740190878769118921060658362307444191332937452616,
```

so the refined method stops honestly.

Focused verification:

```text
RATE_HALF_MCA_RANK11_KERNEL_MULTIBASIS_DECORATION_COMPRESSION_PASS
  strata=9 multiplicities=3..11 controls=4/4
RATE_HALF_MCA_RANK11_KERNEL_MULTIBASIS_DECORATION_COMPRESSION_AUDIT_PASS
  multiplicities=3..11 proof_pins=5/5
RATE_HALF_MCA_RANK11_KERNEL_MULTIBASIS_CAPACITY_CUT_PASS
  checked=11632 controls=6/6
RATE_HALF_MCA_RANK11_KERNEL_MULTIBASIS_CAPACITY_CUT_AUDIT_PASS
  checked=11632 proof_pins=4/4
```

No Modal computation was used; both interval replays are constant-memory
exact integer arithmetic.

```text
DAG delta:             +2 PROVED kernel multi-basis nodes,
                       +3 requirement edges, +2 evidence edges
critical status delta: none
rank-eleven delta:     kernel lane removed for K'=10..11641
remaining intervals:  K'=10..11641 rank eight only;
                       K'=11642..22525 rank eight plus kernel;
                       K'=22526..37995 dense-owner chronology plus kernel;
                       K'=37996..1048576 kernel only
delta-star movement:   none
compute:               exact 11,632-row replay, constant memory
next route action:     classify or couple sharp low-basis kernel flats
                       above K'=11641
```
