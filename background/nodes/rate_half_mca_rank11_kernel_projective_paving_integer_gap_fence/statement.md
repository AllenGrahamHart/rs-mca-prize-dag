# Integer-gap envelope for projective paving

Put `R=1048576` and `w=67472`.  In a corank-`d` chart obtained from an
official rank-eleven row `K'`, let `z` be the number of global zero normals
after rank-`(10-d)` shortening and set

```text
t=K'-10-z,                 0<=t<=K'-10.
```

For `d>=2`, define

```text
P_d = (R+d)_fall_(d+1)/((d+1)(w+d-1)_fall_d),
F_d(t) = (R+d+t)_fall_(d+1)
         /((w+d+t)(w+1)_rise_(d-1)).
```

The valid record envelope is

```text
M_d(K') = floor(max(P_d,F_d(1),F_d(K'-10))).       (IG)
```

The first term applies only at complete shortening `t=0`; the other two
control all remaining integer charts.  Corank one has the stronger uniform
projective-pair cap `M_1=8147918`.

At `K'=377674`, `(IG)` gives

```text
M_2=253238254,       M_3=3935391907,
```

so the complete values `84416263` and `983902549` cannot be substituted
uniformly on the strength of the current transversality theorem.
