# Result

For `R=log m` and `x=4(d+1)R/m<=1`, the first cyclotomic norm estimate and
the cubic Taylor lower bound for `exp(-x)` give

```text
L<Y_3=4((d+1)R-d)-8(d+1)^2R^2/m
        +(32/3)(d+1)^3R^3/m^2.
```

for the squared antipodal defect of a primitive width `h=m/4-d` pair.
Meanwhile, the consecutive even moments form a Vandermonde system on the
nonzero defect coordinates. A nonzero defect therefore satisfies

```text
L>=floor((h-1)/2)+2.
```

Whenever the upper expression is at most the lower one, the defect is zero.
The pair is antipodal-swap, and the proved swap-norm theorem excludes it.
Thus the complete primitive width is empty.

The band starts with `1<=d<=2` at `m=2^9`. At `m=2^41` it deletes exactly
`1<=d<=2,677,220,820`, and it contains `5,501,420,621` dyadic cells through
the official top level. The former linear ceiling is a sufficient sub-band.
HGE4 remains open below the cubic band.
