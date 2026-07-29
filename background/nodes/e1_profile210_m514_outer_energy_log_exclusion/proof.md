# Proof

Write

```text
y_u=|F(zeta_256^u)|^2=18+x_u,
E=sum_(d=1)^63 A_d^2.
```

Over the 64 positive-half conjugate pairs,

```text
sum_u x_u=0,
sum_u x_u^2=128E,
Norm(F(zeta_256))=product_u(18+x_u).                 (1)
```

Since every `A_d` is integral,

```text
|x_u|<=2 sum_d |A_d|<=2E.                           (2)
```

If `E=0`, `(1)` gives `Norm=18^64`, whose 2-adic valuation is `64`, not the
local valuation one of cofactor `514`. Thus energy zero is impossible.

## Energies one through four

For `-8<=x<=8`,

```text
log(1+x/18)>=x/18-x^2/446.                          (3)
```

Indeed, if `h` is the left side minus the right side, then

```text
h'(x)=x(1/223-1/(18(18+x))).
```

The only nonzero critical point is `-101/18`, so the minimum is at `-8` or
`0`. For the negative endpoint, the positive atanh series with parameter
`2/7` gives

```text
log(9/5)<45364/77175<1180/2007=4/9+32/223.          (4)
```

The first bound keeps the first two series terms and bounds the remaining
geometric tail; its rational margin in `(4)` is `776/5736675`. This proves
`(3)`.

For `1<=E<=4`, equations `(1)--(3)` give

```text
log Norm>=64 log(18)-128E/446
        >=64 log(18)-256/223.                       (5)
```

Put `z=256/223`. Since `z/4=64/223<1`, the positive exponential series gives

```text
exp(z)<(1-z/4)^(-4)=(223/159)^4
      <18^64/(514*p_max).                           (6)
```

The last comparison is exact integer arithmetic. Equations `(5)--(6)` imply
`Norm>514*p_max`, excluding energies one through four.

## Energies fourteen through seventeen

For a fixed energy `E`, put `M=2E` and

```text
c_E=(M/18-log(1+M/18))/M^2.
```

The endpoint-tangent calculus used above gives, for `-18<x<=M`,

```text
log(1+x/18)<=x/18-c_E x^2.                          (7)
```

The derivative has one positive turning point: the elementary integral
bounds

```text
M^2/(2*18*(18+M))<M/18-log(1+M/18)<M^2/(2*18^2)
```

place it strictly between `0` and `M`; `(7)` is zero at both endpoints
`0,M` and negative elsewhere.

The quantity `E c_E` increases with `E`, because
`log(1+t)/t` decreases for `t>0`. At `E=14`, the atanh parameter `7/16`
gives

```text
log(23/9)<994931/1059840
           <3598/3825=14/9-784/1275.               (8)
```

The rational margin in `(8)` is `56987/30028800`; hence `c_14>1/1275`.
For every `14<=E<=17`, summing `(7)` now gives

```text
log Norm<64 log(18)-128*14/1275
        =64 log(18)-1792/1275.                      (9)
```

With `w=1792/1275`, the positive exponential series gives

```text
exp(w)>1+w+w^2/2+w^3/6+w^4/24
      >18^64/(514*p_min),                           (10)
```

where the final comparison is an exact cross-multiplication. Equations
`(9)--(10)` imply `Norm<514*p_min`, excluding energies fourteen through
seventeen. Only energies five through thirteen remain. QED.
