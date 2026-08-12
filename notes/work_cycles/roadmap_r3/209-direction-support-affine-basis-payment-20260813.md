# Cycle 209: direction-support affine-basis payment (2026-08-13)

The gauged affine-incidence proof contains a support/rank interaction not
used by its original all-coordinate numerator.  If

```text
q=r_1-b,       E=supp(q),       |E|=e<=R,
```

then every incident normal outside `E` has zero slope component.  Let `z`
be the number of zero normals.  All zero normals also lie outside `E`, so
the candidate ordered full-basis count sharpens exactly from

```text
(n-z)_(fall r+1)
```

to

```text
(n-z)_(fall r+1)-(n-e-z)_(fall r+1).
```

Factoring this subtraction out of the existing affine-span endpoint
envelope gives

```text
|Z| <= floor(P(R,r,e) M(K,r)),

P(R,r,e)=1-(R+r-e)_(fall r+1)/(R+r)_(fall r+1),
```

where `M(K,r)` is the proved two-endpoint rank envelope.  The support factor
is increasing.  The existing one-turn dimension calculation shows that the
ambient endpoint `K=R` owns all displayed ranks, producing uniform walls
over every shortened dimension:

```text
KoalaBear:   r=11 all e; r=12 e<=15903; r=13 e<=435;
             r=14 e<=13; r=15 none.
Mersenne-31: r=4 all e; r=5 e<=62235; r=6 e<=1486;
             r=7 e<=41; r=8 e<=1; r=9 none.
```

Unlike punctured-list payment, this theorem is valid for `e>=d`.  The
primary checker validates every rational endpoint and adjacent wall.  The
independent checker recomputes products by recurrence/gcd and exhaustively
checks 239 small tuple-subtraction models and 189 support monotonicity cases.

```text
start:                   4d2c9d3a5
result:                  PROVED direction-support affine-basis payment
DAG delta:               +1 PROVED background node, +3 edges
critical status delta:   none; one live MCA residual is substantially cut
upstream terminal delta: middle-support cells now carry explicit rank-wise
                         support floors, not only sparse-list constraints
delta-star movement:     none
compute:                 bounded exact arithmetic under RAMguard;
                         no Modal spend
next route action:       use the actual common-zero count instead of its
                         uniform worst case, or force a high-rank/high-
                         support residual into another owner
```
