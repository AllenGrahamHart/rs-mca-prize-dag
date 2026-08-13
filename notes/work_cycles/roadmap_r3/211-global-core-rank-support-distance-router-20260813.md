# Cycle 211: global-core rank/support/distance router (2026-08-13)

The preceding MCA compilers bounded rank, low direction support, and high
direction support separately.  They apply to the same selected family after
one whole-line global-core cancellation and one minimum-lift gauge, so their
paid regions can be unioned without adding budgets.

Write the shortened row as `(R+s,s,d+s)`, let `r` be the transformed
explanation rank, and put

```text
e=d_U(y_1)=R-j.
```

The exact common-zero envelope is maximized only over
`x in [R+r,R+s]`, not the all-dimension interval through `2R`.  Exhausting
that actual range gives, uniformly through the recursive frontier:

```text
KoalaBear, 14<=s<=4992:
  r<=13 paid for every e;
  r=14,15,16,17 paid for e<=31768,1576,94,5.

Mersenne-31, 6<=s<=4979:
  r<=5 paid for every e;
  r=6,7,8,9 paid for e<=11847,646,36,2.
```

The recursive direction theorem pays the opposite suffix
`e>=R-J_rec(s)`.  At each first legal dimension `s=r` this leaves, in
particular,

```text
KoalaBear s=14, r=14: e=31769..1044245;
Mersenne s=6, r=6:    e=11848..1044241.
```

Higher transformed ranks have the separately printed middle intervals at
their own first legal dimensions; `r<=s` is enforced.
Thus the old `s>=14`/low-direction bucket is now a joint high-rank,
middle-support cell.  No target status changes: the middle intervals and K3
first-match allocation remain open.

Two independent constant-memory checkers replay 99,490 exact support cells,
9,953 rank cells, 22 recursive frontiers, ten residual intervals, and 96
small support-monotonicity models.

```text
start:                   5d724af27
result:                  PROVED global-core rank/support/distance router
DAG delta:               +1 PROVED background node, +5 edges
critical status delta:   none; the deployed K3 route is sharply localized
upstream terminal delta: first residuals are explicit rank/support intervals
delta-star movement:     none
compute:                 bounded exact arithmetic under RAMguard;
                         no Modal spend
next route action:       attack the surviving middle support through
                         rational/order-32 ownership or a rank-support
                         interaction not visible to scalar incidence
```
