# Proof

Let

```text
U(y)=y^hP(1/y)=1+ay+...+P(0)y^h.
```

After the normalization `P(0)=1`, the reciprocal of `Q` is
`U+d y^h`. Substitute these expressions and the pinned linear defect

```text
G=d^2(a-(h/m)X)
```

into the differential identity and eliminate `R` using `PQR=X^m-1`. The
exact reciprocal equation is

```text
(hU-yU')(1-y^m)
 =(h-may)U^2(U+dy^h)^2
  +(m/d^2)y^(h+1)U(U+dy^h)(2U+dy^h).                (1)
```

Modulo `y^h`, this becomes

```text
hU-yU'=(h-may)U^4.                                  (2)
```

Put `Z=U^(-3)`. Dividing `(2)` by `U^4` gives

```text
yZ'+3hZ=3h-3may.                                    (3)
```

Since `m=3h+1`, comparison of coefficients in `(3)` gives

```text
Z=1-3ay mod y^h.
```

All integers `j+3h`, `0<=j<h`, are invertible under the characteristic
hypothesis. Therefore

```text
U=(1-3ay)^(-1/3) mod y^h
 =sum_(j=0)^(h-1) C_j a^j y^j mod y^h,              (4)
```

which proves `(LBO1)` because the final coefficient is the normalized
constant `P(0)=1`.

For completeness, retain the coefficient of `y^h` in `(1)`. The final two
terms begin at `y^(h+1)`, except that replacing
`(U+dy^h)^2` by `U^2+2dUy^h` contributes `2dh`. If

```text
F=(1-3ay)^(-1/3),
```

then `U` and `F` agree below degree `h`, while their degree-`h` coefficients
are `1` and `C_h a^h`. Since

```text
F^4=(1-3ay)^(-4/3)
```

and its consecutive coefficients satisfy

```text
[y^h]F^4=(m/h)[y^(h-1)]F^4,
```

the degree-`h` equation reduces to

```text
2+d=2C_h a^h.                                       (5)
```

Substitute `d=x-1` and the boundary trace value for `a`. If `x!=-1`, clearing
the invertible denominators in `(5)` gives `(LBO3)`.

It remains to justify the orbit count and the omitted value. The constants
of `P,Q` lie in `mu_m`, and `gcd(h,m)=1`. Hence the scaling action has a
unique representative with `P(0)=1`; its invariant ratio is `x=Q(0)/P(0)`.
For fixed `x`, equations `(LBO1)` and the pinned values of `a,d` determine
both locators uniquely. Thus ordered scaling orbits inject into possible
values of `x`.

The value `x=1` would give `d=0`. If `x=-1`, then `a=0`, so `(LBO1)` gives
`P=X^h+1` and `Q=X^h-1`. But `Q|X^m-1` would imply `h|m`; this contradicts
`gcd(h,m)=1` when `h>1`. At most `m-2` ratios remain, proving `(LBO2)`.
Primitivity and exact-level filtering can only decrease that count. QED.
