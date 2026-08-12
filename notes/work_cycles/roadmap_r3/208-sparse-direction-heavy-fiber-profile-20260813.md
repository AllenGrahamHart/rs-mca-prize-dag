# Cycle 208: sparse-direction heavy-fiber profile (2026-08-13)

Cycle 207 charged every transformed explanation for all `e` possible
slopes.  The actual charge depends on its outside-agreement deficit.

For a gauged direction `q` supported on `E`, `|E|=e<d`, put

```text
O(a)=|{x outside E:a(x)=r_0(x)}|,       h_a=m-O(a).
```

Same-support pair noncontainment gives `h_a>=1`; existence of a bad slope
assigned to `a` gives `h_a<=e`.  Every such slope is a fiber of
`(a-r_0)/q` on `E` of size at least `h_a`, so one explanation owns at most
`floor(e/h_a)` slopes.

For explanations of deficit at most `h`, the punctured affine-list theorem
at agreement threshold `m-h` gives the cumulative cap

```text
B_h=floor(C(R-e+r,r)/C(d-h+r,r)).
```

Optimizing the decreasing fiber weights under these nested caps yields

```text
|Z| <= sum_(h=1)^e (B_h-B_(h-1))*floor(e/h),       B_0=0.
```

Exact adjacent boundaries improve the paid prefixes to

```text
KoalaBear:   r=12 -> e<=1407; r=13 -> e<=89;
             r=14 -> e<=5;    r=15 -> none.
Mersenne-31: r=4  -> e<=287;  r=5  -> e<=18;
             r=6  -> e<=1;    r=7  -> none.
```

The primary exact-binomial checker scans 1,815 prefix cells.  An independent
gcd-product implementation checks all 14 nonempty/first-unpaid boundary
values and brute-forces 125 small cumulative-cap allocation problems.

```text
start:                   a62dfeb19
result:                  PROVED sparse-direction heavy-fiber profile
DAG delta:               +1 PROVED background node, +3 edges
critical status delta:   none expected; this sharpens one live MCA route
upstream terminal delta: the scalar direction-fiber charge is replaced by
                         a cumulative outside-deficit profile
delta-star movement:     none
compute:                 bounded exact arithmetic under RAMguard;
                         no Modal spend
next route action:       seek an interaction theorem constraining affine
                         rank inside the weighted ratio-fiber shells
```
