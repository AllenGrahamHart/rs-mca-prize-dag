# Cycle 203: global-core direction-distance router (2026-08-12)

Cycle 202 left only the large shortened dimensions in the whole-line
global-core route.  This cycle composes that one shortened family with the
proved direction-distance ray theorem.

For shortened parameters

```text
(N,K,m)=(R+s,s,d+s),       t=R-d,
```

let `d_U(y_1)` be the minimum weight of a lift of the line-direction
syndrome and put `j=R-d_U(y_1)`.  Pair noncontainment forces `y_1!=0`.
Every selected slope has a `t`-sparse lift on the same full shortened
domain, so the entire family obeys

```text
|Z| <= floor((R+s)(d-j) /
             (d^2-(R-2d)s-(R+s)j))
```

whenever the denominator is positive.  Solving both denominator positivity
and the exact floor comparison with the row budget gives a pointwise defect
threshold `J_B(s)`.

Combined with the support-wise affine-span compiler, the paid region is:

```text
KoalaBear:   every j for s<=13;
             0<=j<=J_B(s) for 14<=s<=4982.
Mersenne-31: every j for s<=5;
             0<=j<=J_B(s) for 6<=s<=4979.
```

For KoalaBear the budget never cuts before denominator positivity.  The
largest paid value over all 4,969 dimensions is only `168818566`, attained
at `(s,j)=(1356,3156)`, against budget `274980728111395087`.

For Mersenne-31 the largest paid value is `16131678`, attained at
`(s,j)=(1970,2617)`, below budget `16777215`.  At thirteen isolated
dimensions the final positive-denominator defect is over budget, and the
threshold drops by one; the exact triples `(s,j_positive,J_B)` are pinned in
the source contract.

The residual is now the explicit low-direction cell:

```text
s>=4983 or j>J_B(s) on KoalaBear;
s>=4980 or j>J_B(s) on Mersenne-31.
```

The primary checker scans all 9,943 official dimensions and four mutations.
The independent audit directly enumerates 21,505,828 positive defect
candidates, reproducing the maxima and all thirteen spike cells without
using the threshold formula.

```text
start:                   3a13f2dcd
result:                  PROVED global-core direction-distance router
DAG delta:               +1 PROVED background node, +4 edges
critical status delta:   none
upstream terminal delta: large-dimension branch replaced by an exact
                         low-direction-distance cell
delta-star movement:     none
compute:                 bounded local integer loops under RAMguard;
                         no Modal spend
next route action:       attack LOW_DIRECTION_DISTANCE_GLOBAL_CORE
```
