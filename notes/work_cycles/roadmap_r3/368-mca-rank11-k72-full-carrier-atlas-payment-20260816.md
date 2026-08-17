# Cycle 368: MCA K'=72 full carrier atlas payment (2026-08-16)

The split-section coupling from Cycle 367 extends to every fixed carrier
union of dimension at least five.  Combined with an exact pairwise carrier
atlas, this closes the complete `K'=72` row without requiring the bespoke
three-carrier flag as a live dependency.

## Cycle pins

```text
our start:       9e16311b8
our end:         cycle commit containing this record
canonical prize: 28a62b400
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   #1170..#1173; #1170 at 1ca90d4c570e3630b62c4cca084549282f1d7418
```

## Pairwise carrier atlas

For an attaining carrier `B_c`, the support-two projective point is
transverse, lies in a proper deletion span, or is in full-completion
position.  The first two positions give the conservative fixed unions

```text
T_c: (b_2+|B_c|,10-c),
A_c: (b_2+|B_c|-1,11-c).
```

If supports three and `d in {4,5}` are both full, put

```text
r_3=M_3-M_2+1,  r_d=M_d-M_2+d-2.
```

Minimality of `A_d union {p}` for `p in B_2` forces at least `d-2`
anchors outside the support-three rank-two flat.  Hence the residual overlap
has the exact range

```text
0<=t<=min(r_3,M_d-M_2).
```

The union size is `b_2+r_3+r_d-t`; its fixed vanishing dimension is `10-d`
at `t=0` and `11-d` at positive overlap.  The support-four and support-five
alternatives combine by Cartesian product, with no conjectural relation
between their residuals.

## Fixed-union coupled charge

Let a `g>=5` dimensional correction subspace vanish on `u` fixed points.
Put

```text
R=K-u-g,  B=R+3,  N=m-u.
```

For an independent triple or four-set in the original evaluation matroid
outside the union, intersection with the vanishing subspace leaves `g-3` or
`g-4` residual polynomials.  Their gcd-degree bound certifies rank-three
flat size at most `B` and rank-four flat size at most `B+1`.  It is the
original outside matroid to which flat-circuit coupling applies; no circuit
is transferred to the subspace matroid.

After adding exact lower inside/outside strata, the joint selected-incidence
cap is

```text
21 (L_4+X_4) C(m-4,7)+15 (L_5+X_5) C(m-5,6),
```

where

```text
X_4=min(floor(R C(N,3)/4), floor(R C(N,4)/(N-B))),
X_5=floor((R C(N,4)-(N-B)X_4)/5).
```

The endpoint is valid because the exact integer weighted envelope is
nondecreasing whenever `K>=g+5`.

## Complete K'=72 replay

The conservative stream evaluated 7,991,221 leaves.  Exactly 36 distinct
defect tuples exceeded the safe premium ceiling; every other conservative
leaf was safe.  Exhaustive pairwise rerouting of those 36 tuples produced
8,057 exact charged leaves, all safe.  Seven disjoint pre-routed geometry
lanes covered another 113,124,235 exact leaves, all safe.

The global completion premium is the largest already-safe conservative leaf:

```text
P_72 = 41089877204729279662874647920595743958596178333,
ceiling-P_72 = 10440735269654784698417860383073117137496667.
```

The exact component payment is positive:

```text
demand-capacity
=52200017935756118667066163970702686810349690944821612538425.
```

Thus `K'=72` is closed and the proved prefix advances to `10..72`.
Primary and independent theorem verifiers pass remotely.  The independent
row audit recomputes all 8,057 exceptional routes; peak RSS is 59 MB.  The
seven larger exhaustive lanes ran separately on Modal at 59--62 MB.
The manifest replay compiles 2,551 nodes and 7,589 edges, passes reference,
acyclicity, reachability, status-propagation, protocol, crosswalk, and orbit
checks, and has generated DAG SHA-256
`ec14ade0991fbd423dfb778a718c97c50014c908c09834e170cc22a7c71d2f7c`.

```text
result:                CLOSED K'=72
newly closed rows:     72
closed prefix:         10..72
remaining rank nine:  73..15528
new nodes:             3 PROVED
new premise:           none
critical status delta: none; exact evidence frontier advanced one row
upstream delta:         none; both generic theorems are candidates for #1170
delta-star movement:   none
compute:               exact bounded Modal lanes, 59--62 MB peak RSS
next route action:     test whether the pairwise atlas and coupled charge
                       close K'=73, or isolate its first exact survivor
```
