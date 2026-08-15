# Cycle 334: MCA rank-11 two-step nine-shadow hierarchy (2026-08-14)

Two PROVED nodes couple every kernel-corank stratum to the stratum two ranks
above it and move the exact kernel cutoff from `K'=17608` to `K'=18101`.

For one exact support `S`, let `I_d(S)` count rank-`(10-d)` eleven-subsets and
let `J_d(S)` count rank-`(10-d)` nine-subsets.  For every `3<=d<=9`, define

```text
s_d=C(d+2,2),       L_d=C(67472+d,2),
E_d=C(K'-d-9,2),    Q_d=C(11-d,2).
```

The shared nine-shadow theorem gives `s_d I_d<=E_d J_d`.  If `U` is counted
by `J_d`, its closure has size at most `K'-d`, so contraction by `U` leaves at
least `67472+d` outside points.  The next-rank closure cap bounds every
parallel class and forces at least `L_d` pairs that raise rank by two.  A
rank-`(12-d)` target has at most `Q_d` source shadows: the complementary pair
must consist of coloops, and a loopless rank-`(12-d)` matroid on eleven
elements has at most `11-d` coloops.  Hence

```text
(s_d L_d/E_d) I_d <= Q_d I_(d-2),    3<=d<=9.
```

The seven exact rows are

```text
d     s_d       L_d          Q_d
3      10    2276404075       28
4      15    2276471550       21
5      21    2276539026       15
6      28    2276606503       10
7      36    2276673981        6
8      45    2276741460        3
9      55    2276808940        1
```

On every newly checked row `17609<=K'<=18102`, the exact LP has one stable
active set: the corank-one cap, the full-containment resource, and all seven
hierarchy rows bind; every corank variable is positive; the rank-preserving
nine-shadow resource and all other individual caps are slack.  The primary
certificate solves the nine exact dual equations by rational Gaussian
elimination.  The independent audit instead reconstructs the hierarchy
multipliers by backward odd/even recurrences.

At `K'=18101`, demand exceeds floored capacity by

```text
33462159928103132226516704640419847248244116666500998762314.
```

At `K'=18102`, capacity exceeds demand by

```text
275016496133605602641019628236447268989861205055439981187167.
```

Focused verification on Modal:

```text
RATE_HALF_MCA_RANK11_KERNEL_TWO_STEP_NINESHADOW_HIERARCHY_PASS
  rows=7 controls=4/4
RATE_HALF_MCA_RANK11_KERNEL_TWO_STEP_NINESHADOW_HIERARCHY_AUDIT_PASS
  closure_checks=250663 coloop_checks=42
RATE_HALF_MCA_RANK11_KERNEL_TWO_STEP_NINESHADOW_CAPACITY_CUT_PASS
  checked=494 controls=6/6
RATE_HALF_MCA_RANK11_KERNEL_TWO_STEP_NINESHADOW_CAPACITY_CUT_AUDIT_PASS
  checked=494 wall=18102 recurrences=7
```

```text
DAG delta:             +2 PROVED two-step nine-shadow nodes,
                       +4 requirement edges, +2 evidence edges
critical status delta: none
rank-eleven delta:     kernel lane removed for K'=17609..18101
remaining intervals:  K'=10..18101 rank eight only;
                       K'=18102..22525 rank eight plus kernel;
                       K'=22526..37995 dense-owner chronology plus kernel;
                       K'=37996..1048576 kernel only
delta-star movement:   none
compute:               exact 494-row primal/dual replay on Modal
next route action:     attack the stable K'=18102 wall by strengthening the
                       corank-one cap, full-containment coefficient, or one
                       hierarchy row, or by finding an independent resource
```
