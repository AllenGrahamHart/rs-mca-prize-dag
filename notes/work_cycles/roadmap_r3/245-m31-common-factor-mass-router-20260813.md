# Cycle 245: M31 common-factor mass router (2026-08-13)

The capped size-two bank at `e=130237` forces all 7,583 distinct
polynomial-pair cores before its threshold drops to one.  Let `P` be the
full common interpolation factor and `d=deg_(Y,Z)P`.  Dividing the kernel by
`P` leaves a gcd-one family of degree at most `52-d`, so cofactor Bezout
permits at most `(52-d)^2` selected pairs off `P`.  Consequently

```text
on-factor pairs >= 7583-(52-d)^2 >= 4982.
```

Each captured pair has an inside core of size at least 807, and distinct
pair cores intersect in at most five coordinates.  A second-moment/Cauchy
union bound gives

```text
factor points
 >= ceil(t*807^2/(807+5(t-1)))
 >= 126188.
```

Thus the received pair lies on `P` at all but at most 4,049 inside
coordinates.  This is substantially narrower than an arbitrary common-
factor exception: the next theorem should exploit a degree-at-most-52
curve relation holding on 96.89% of the inside support and carrying at least
4,982 degree-five polynomial sections.

```text
start:                   e4b717f91
canonical prize:         fdfb20a42
upstream frontier:       #1163-#1166; #1165 @ 862fcaf1
result:                  NARROWED; common-factor mass router PROVED
DAG delta:               +1 PROVED node, +4 edges
critical status delta:   none; replacement target remains TARGET
Mersenne residual:       130237<=e<=1044241
first-support residual:  deg_YZ<=52 factor, <=4049 inside exceptions,
                         >=4982 polynomial sections
delta-star movement:     none
compute:                 exact arithmetic under RAMguard; no Modal
next route action:       classify/charge the near-total factor relation
export target:           extend przchojecki/rs-mca PR #1165 after review
```
