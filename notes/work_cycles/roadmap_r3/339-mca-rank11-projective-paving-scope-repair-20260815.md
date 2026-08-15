# Cycle 339: MCA rank-11 projective-paving scope repair (2026-08-15)

This cycle adversarially audited the corank-two and corank-three capacity
promotions from cycles 337 and 338.  Their complete-chart projective counts
are correct, and their finite capacity replays are exact conditional
arithmetic, but the replays promoted the complete caps to every shortening
chart without a uniform theorem.  That logical promotion is retracted.

After rank-`(10-d)` shortening, write

```text
t=K'-10-z,       0<=t<=K'-10,
```

where `z` is the number of global zero normals.  Complete shortening is the
single point `t=0`.  In that chart, support-local transversality makes the
rank-`d+1` incident normal matroid paving.  A new universal leaf proves

```text
b(M)>=C(m-1,d),
```

by deletion-contraction, with equality for one coloop over a uniform
rank-`d` deletion.  It gives the nine exact complete-chart caps

```text
8147918, 84416263, 983902549, 12232092309, 158406193634,
2109949210211, 28689347099870, 396280526311830, 5542092977392141.
```

For `d>=2`, the current pointwise support-local theorem supplies

```text
F_d(t)=(1048576+d+t)_fall_(d+1)
       /((67472+d+t)(67473)_rise_(d-1))
```

on `t>=1`.  Its successive ratio has the sign of

```text
d*t+(d+1)(67472+d)-1048576,
```

so the valid combined envelope is

```text
floor(max(P_d,F_d(1),F_d(K'-10))),
```

not `floor(max(P_d,F_d(K'-10)))`.  The adjacent integer point is decisive.
At `K'=377674` the valid values are

```text
M_2=253238254,       M_3=3935391907,
```

rather than the complete values `84416263` and `983902549`.

Corank one is different.  After deleting zero normals, its full-rank
rank-two matroid has at least `2(w+t)` ordered independent pairs.  The
resulting one-turn ratio and exact official endpoint comparison prove that
`8147918` is uniform.  The green projective-pair capacity cut through
`K'=377673` is therefore repaired to consume this uniform theorem.

The two later capacity nodes now have status `CONDITIONAL`:

```text
uniform M_2<=84416263  => conditional cutoff 568338/568339,
uniform M_2 and M_3    => conditional cutoff 796598/796599.
```

Their old exact Modal replays still pass and prove those implications.  Two
new TARGET leaves isolate the missing uniform corank-two and corank-three
propositions.  A corrected one-container probe, explicitly heuristic, finds
that the valid integer-gap envelope leaves the resource wall at
`377673/377674`.

Focused verification:

```text
MATROID_PAVING_BASIS_FLOOR_PASS checks=216 ranks=9 controls=6/6
MATROID_PAVING_BASIS_FLOOR_AUDIT_PASS dynamic_checks=225 extremizers=9
RATE_HALF_MCA_RANK11_KERNEL_PROJECTIVE_PAVING_RECORD_CAPS_PASS
  complete_caps=8147918,...,5542092977392141 controls=8/8
RATE_HALF_MCA_RANK11_KERNEL_PROJECTIVE_PAVING_RECORD_CAPS_AUDIT_PASS
  dimensions=9
RATE_HALF_MCA_RANK11_KERNEL_PROJECTIVE_PAVING_INTEGER_GAP_FENCE_PASS
  M2=253238254 M3=3935391907 controls=8/8
RATE_HALF_MCA_RANK11_KERNEL_PROJECTIVE_PAVING_INTEGER_GAP_FENCE_AUDIT_PASS
  dimensions=8 checks=80
RATE_HALF_MCA_RANK11_KERNEL_PROJECTIVE_PAIR_CAPACITY_CUT_PASS
  checked=359516 controls=6/6
RATE_HALF_MCA_RANK11_KERNEL_CORANK2_PROJECTIVE_CAPACITY_CUT_PASS
  checked=190666 wall=568339 controls=6/6
RATE_HALF_MCA_RANK11_KERNEL_CORANK3_PROJECTIVE_CAPACITY_CUT_PASS
  checked=228261 wall=796599 controls=8/8
```

```text
DAG delta:             +3 PROVED scope/endpoint nodes,
                       +2 TARGET uniform-cap leaves,
                       2 PROVED capacity promotions -> CONDITIONAL
critical status delta: none
unconditional kernel: K'=10..377673 excluded
conditional intervals:377674..568338 needs uniform M2;
                       568339..796598 also needs uniform M3
remaining kernel:      K'=377674..1048576
delta-star movement:   none
compute:               one corrected 512-MB/60-second Modal probe;
                       6.7 seconds wall time; no large run retained
upstream action:       correct PR #1170 before merge; export complete-chart
                       caps and the scope fence, not unconditional cutoffs
next route action:     attack the t=1 corank-two target first; derive a
                       multiplicity-aware matroid basis floor or construct
                       an RS realization that falsifies the fixed cap
```
