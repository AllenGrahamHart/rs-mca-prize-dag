# Shortening-weighted kernel extension cap

Put `R=1048576`, `w=67472`, and `S=K'-10`.  For every kernel corank
`1<=d<=9`, every fixed rank-`(10-d)` basis chart, and every official row
`10<=K'<=R`, the number of decorated `(record,T)` extensions over that
basis is at most

```text
P_d C(S,d+1)                                      for d=1,2,3,
F_d(1) C(S-1,d+1)                                for d=4,...,9,
```

where `P_d` is the proved complete-chart integer cap and

```text
F_d(t)=(R+d+t)_fall_(d+1)
       /((w+d+t)(w+1)_rise_(d-1)).
```

The second line is a rational upper bound.  It may be floored after
multiplication.  The result couples a chart's record cap to its actual
number of zero-normal extensions; it does not assert that `P_d` is a
uniform per-chart record cap for `d>=4`.
