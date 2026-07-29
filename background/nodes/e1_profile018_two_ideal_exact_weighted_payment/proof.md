# Proof

The proved profile-`(0,18)` router leaves ten pure ideal families and the
cofactor-514 split families. Under the named class-orbit certificate,
`e1_profile018_qzeta128_class_descent_two_ideal_bound` permits at most two
occupied split ideals. The common-ideal height theorem and occupancy
dictionary assign at most one 256-vector shift/sign orbit to each family.
Therefore

```text
T_018 <= 10+2 = 12,
|D_018| <= 256*12 = 3072.                           (1)
```

The exact dictionary weight is

```text
M_33(0,18)=1117325838856821897682125205459304448.   (2)
```

Equations (1)--(2) give charge

```text
M_33(0,18)*3072/2
=1716212488484078434839744315585491632128.          (3)
```

Before profile `(0,18)`, the proved serial residual is

```text
R_before=2231339193048374054995899432498611923367.   (4)
```

Subtracting (3) from (4) gives

```text
R_after=515126704564295620156155116913120291239.     (5)
```

The next dictionary profile is `(4,4,S=20)`, of weight

```text
M_next=522452937039935372855706187881128712.         (6)
```

Exact integer arithmetic yields

```text
2R_after-M_next*1971
 =498670222878620413713337512535891126 >=0,

M_next*1972-2R_after
 =23782714161314959142368675345237586 >0.            (7)
```

Thus `floor(2R_after/M_next)=1971`, and the adjacent cap 1972 is not
certified by this inference. QED.
