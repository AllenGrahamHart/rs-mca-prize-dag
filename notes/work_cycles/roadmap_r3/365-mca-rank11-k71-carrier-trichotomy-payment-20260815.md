# Cycle 365: MCA rank-11 K'=71 carrier-position payment (2026-08-15)

Cycle 364 closed `K'=60..70` with one attaining carrier at a time.  At the
new wall, the support-two, support-three, and support-four maxima coexist.
Their projective positions cannot be chosen independently.

## Cycle pins

```text
our start:       b484010bbcf39a7cc7daf7240c4ed1c08c4c9663
our end:         cycle commit containing this record
canonical prize: 69c14c8bc
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   #1170 at 6ea448fbb6fca01998a1915cb8450cd968a94587
```

## Fixed-union collision theorem

If a fixed (g)-dimensional subspace of the ten-dimensional correction
space vanishes on a fixed (u)-point union, then its intersection with a
target support-(d) deletion space has dimension at least

```text
r_d=g+1-d.
```

For (r_d>0), the target carrier has at most (R_d=K'-r_d-u) points
outside the union.  Exact outside-deletion exposure therefore bounds the
number of target circuits by

```text
C(u,d)+sum_(j=1)^d floor(
  C(u,d-j) C(m-u,j-1) max(0,R_d-j+1) / j
).
```

This separates the reusable count from the carrier geometry.

## Carrier-position trichotomy

An attaining support-two carrier is a full nonzero parallel class.  Relative
to an attaining support-three or support-four deletion, its projective point
is transverse, lies in a proper deletion span, or supplies every parallel
point as an exact completion.  The last position forces
(M_c>=M_2+1).

Thus (M_3<=M_2) leaves only the transverse and proper-span cases and
excludes every defect pair with (s_2+s_3<q).  At (K'=71), 961 pairs are
impossible.  When (M_3=M_4=M_2+1), exact minimal-circuit geometry gives
six fixed-union cases:

```text
T23, A23, T24, A24, N34, N34A.
```

The payment retains these as alternatives; it never intersects their caps.

## Singleton-row payment

Exact defects at supports two through five retain their position provenance
until support four is known.  Every old sparse cap, the
support-four/support-five joint charge, all 120 high-support branches, every
kernel corank, and every rank-nine mark remain present.

The old unsafe one-step branch is safe in all six geometry cases.  The new
maximizer is

```text
s2=33/s3=31/s4=31/s5=31/c6F/c7F/c8F/c9F,
```

and the exact (K'=71) gap is

```text
118872281099445772155993127155914865045379156488810154591370.
```

At (K'=72), the active support-three maximum is two above the support-two
maximum.  The complete replay first fails there by capacity excess

```text
4821537739796415753639473905341364357966460110033651367468100.
```

Primary and independently coded replays agree on the pruning census, every
position case, the exact premium, floor-sensitive payment, and adjacent
wall.

```text
result:                PROVED K'=71 component-row closure
newly closed rows:     71
closed prefix:         10..71
remaining rank nine:  72..15528
new nodes:             3 PROVED
new premise:           none
critical status delta: none; exact evidence frontier advanced one row
upstream delta:         cycle-364 K'=60..70 packet exported to #1170
delta-star movement:   none
compute:               exact local arithmetic under 1 GiB cap; no Modal spend
next route action:     classify the M3=M2+2 carrier position at K'=72
```
