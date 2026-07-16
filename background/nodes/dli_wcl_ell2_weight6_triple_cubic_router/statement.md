# DLI ell-two weight-six triple-cubic router

- **status:** PROVED
- **closure:** proof
- **dependency:** `dli_wcl_ell2_weight3_ambient_exclusion`

Let `F` have characteristic different from `2,3`, and let `H<=F^*`
have power-of-two order `M`. Suppose that `H` has no reduced
antipodal-free three-set of sum zero. Then a reduced antipodal-free six-set
`R<=H` satisfying

```text
sum_(r in R) r = sum_(r in R) r^3 = 0
```

exists if and only if the following guarded router succeeds.

Scale one selected root to `1`, select two further roots `x,y`, and select
`d in H`. Put

```text
u = 1+x+y,       A=x+y+xy,       B=xy,
W = uA-B-d,      C=W/u,
Q(T)=T^3+uT^2+CT-d.
```

The three-set hypothesis gives `u!=0`. Starting at `m=1`, define

```text
S_1=-u^2,              T_1=uW,             P_1=u^3 d,
S_(2m)=S_m^2-2T_m,
T_(2m)=T_m^2-2P_m S_m,
P_(2m)=P_m^2.
```

The two membership equations are

```text
S_M=3u^M,              T_M=3u^(2M).          (W6-R)
```

The guards are that `{1,x,y}` is reduced and antipodal-free and that the
three roots of `Q` are distinct, disjoint from it, and make the union
antipodal-free. Under these guards, `(W6-R)` is equivalent to all three
roots of `Q` lying in `H`.

For the official slot `M=1024`, the proved weight-three ambient exclusion
supplies the three-set hypothesis. There are `1,514` legal `(x,y)` orbits
under odd dilation, so this gives an exact finite obstruction with at most

```text
1514*1024 = 1,550,336
```

pair-product candidates. For each candidate, the two sides of `(W6-R)`
are cyclotomic integers. Any supporting split characteristic divides both
of their norms. Moreover, it does not divide `Norm(u)`: such a divisor
would produce an official weight-three zero sum at a conjugate order-`1024`
root. Thus one may remove from the norm gcd every prime factor shared with
`Norm(u)`. This is a router and saturated norm-gcd interface, not an
exclusion of the `(ell,w)=(2,6)` slot.
