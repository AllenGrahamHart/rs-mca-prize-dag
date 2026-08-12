# Cycle 207: sparse-direction affine-rank payment (2026-08-13)

The punctured-list payment from Cycle 205 used the entire shortened code as
its affine explanation space.  After the gauge router, it can instead use
the actual transformed explanation rank `r`.

For a codeword gauge `b`, put

```text
q=r_1-b,       e=|supp(q)|<d,
a_gamma=c_gamma-gamma b,
r=rank_aff{a_gamma}.
```

Puncturing the support of `q` produces an ordinary list in parameters

```text
(n',K',m')=(R+K-e,K,d+K-e),       w'=d-e.
```

The transformed explanations retain affine rank at most `r`, so the
affine-span list theorem gives at most

```text
floor(C(R-e+r,r)/C(d-e+r,r))
```

distinct explanations.  Pair noncontainment again gives slope fiber at most
`e`.  Therefore

```text
|Z| <= e*floor(C(R-e+r,r)/C(d-e+r,r)),
```

independently of the ambient shortened dimension `K`.

The exact paid support prefixes are:

```text
KoalaBear:   r=12 -> e<=1144; r=13 -> e<=87;
             r=14 -> e<=5;    r=15 -> no e>=1.
Mersenne-31: r=4  -> e<=282;  r=5  -> e<=18;
             r=6  -> e<=1;    r=7  -> no e>=1.
```

Every boundary is adjacent and exact.  For example:

```text
KB r=13: 272256895343216442 <= B* < 275435997743171320
M31 r=5: 16363584 <= B* < 17273869.
```

The primary exact-binomial checker and independent gcd-product checker each
scan 539,672 rank/support cells and reject four mutations / three controls.

```text
start:                   60db12dc5
result:                  PROVED sparse-direction affine-rank payment
DAG delta:               +1 PROVED background node, +3 edges
critical status delta:   none
upstream terminal delta: residual is now joint middle-rank/middle-support,
                         not merely low direction distance
delta-star movement:     none
compute:                 bounded integer scans under RAMguard;
                         no Modal spend
next route action:       attack the joint residual with rank/support
                         interaction rather than another scalar bound
```
