# Cycle 332: MCA rank-11 full nine-shadow containment (2026-08-14)

Two PROVED nodes price the nonspanning nine-subsets omitted by Cycle 331.

For one record, let `J_1` count rank-nine nine-subsets. A rank-nine shadow
extends to a kernel eleven-set in at most

```text
E_1=C(K'-10,2)
```

ways, while every lower-rank shadow has the unrestricted support-pair cap

```text
E_0=C(m'-9,2).
```

Counting all 55 nine-subsets in every kernel eleven-set and using the
three-spanning-shadow minimum for corank one eliminates `J_1` and gives

```text
[52+3E_0/E_1] I_1 + 55 sum_(d>=2) I_d
  <= E_0 C(m',9).
```

Combining this with the rank-preserving nine-shadow resource produces a
two-constraint exact LP. At its boundary, coranks 1 and 2 are both
fractional, both shadow resources bind, and all higher coranks vanish.
The independent replay uses the nonnegative dual multipliers rather than
the primal piecewise optimizer.

Exact replay closes every row through `K'=15670`. At the endpoint the
demand-capacity gap is

```text
60244744187647715538325354175068999745872308513185869854532.
```

At `K'=15671`, capacity exceeds demand by

```text
291105561463347587484268984669020036510369238771859813045635,
```

so the method stops honestly.

Focused verification on Modal:

```text
RATE_HALF_MCA_RANK11_KERNEL_NINE_SHADOW_CONTAINMENT_COUPLING_PASS
  rows=5 shadows=55 controls=6/6
RATE_HALF_MCA_RANK11_KERNEL_NINE_SHADOW_CONTAINMENT_COUPLING_AUDIT_PASS
  rows=6 coefficient_base=52 lower_coefficient=55
RATE_HALF_MCA_RANK11_KERNEL_NINE_SHADOW_CONTAINMENT_CAPACITY_CUT_PASS
  checked=15661 controls=8/8
RATE_HALF_MCA_RANK11_KERNEL_NINE_SHADOW_CONTAINMENT_CAPACITY_CUT_AUDIT_PASS
  checked=15661 active=1,2 wall=15671
```

The four Modal jobs peaked at 55--57 MB each.

```text
DAG delta:             +2 PROVED containment-shadow nodes,
                       +3 requirement edges, +2 evidence edges
critical status delta: none
rank-eleven delta:     kernel lane removed for K'=10..15670
remaining intervals:  K'=10..15670 rank eight only;
                       K'=15671..22525 rank eight plus kernel;
                       K'=22526..37995 dense-owner chronology plus kernel;
                       K'=37996..1048576 kernel only
delta-star movement:   none
compute:               exact 15,661-row primal/dual replay on Modal
next route action:     couple the rank-nine and rank-eight flat families;
                       standalone ten/eight shadows are nonbinding here
```
