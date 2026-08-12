# Cycle 210: direction-support common-zero envelope (2026-08-13)

Cycle 209 separated the direction-support proportion from the affine-span
envelope.  Retaining the zero-normal count gives a sharper exact scalar
optimization.

For `z=g+c`, the subtracted basis count yields

```text
|Z| <= ((n-z)_(fall r+1)-(n-e-z)_(fall r+1))
       /((m-g)(d+c)_(rise r)).
```

At fixed `z`, the numerator is fixed and the denominator

```text
(m-z+c)(d+c)_(rise r)
```

strictly increases with `c`.  Hence `c=0`, `g=z` is worst.  Setting
`x=R+K-z` proves the exact envelope

```text
|Z| <= floor(max_(x=R+r..R+K)
  ((x)_(fall r+1)-(x-e)_(fall r+1))
  /((x-R+d)d_(rise r))).
```

The interval through `2R` is uniform over all shortened dimensions.  Exact
exhaustion gives

```text
KoalaBear:   r=12 e<=31806; r=13 e<=870; r=14 e<=26;
             r=15 none.
Mersenne-31: r=5 e<=124471; r=6 e<=2973; r=7 e<=83;
             r=8 e<=2; r=9 none.
```

The Mersenne rank-five wall now crosses `e=d=67448`, genuinely entering the
middle-support region where punctured-list payment is unavailable.

Two independent implementations each exhaust 16,777,078 exact official
cells and recover all nine adjacent maxima at `x=2R`.  The recurrence audit
also checks 140 fixed-`z` denominator cells.  Both are constant-memory and
finish in about ten seconds under RAMguard.

```text
start:                   99d52e857
result:                  PROVED direction-support common-zero envelope
DAG delta:               +1 PROVED background node, +3 edges
critical status delta:   none; Mersenne rank-five middle support is cut
upstream terminal delta: shortened residual has an exact one-dimensional
                         support/rank envelope
delta-star movement:     none
compute:                 two bounded constant-memory local scans;
                         no Modal spend
next route action:       combine the surviving high-rank/high-support cell
                         with the direction-distance or rational-owner
                         partition rather than further scalar repricing
```
