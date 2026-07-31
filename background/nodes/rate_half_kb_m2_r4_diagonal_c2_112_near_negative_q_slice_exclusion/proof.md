# Proof

Use the notation of the two parent nodes. Put

```text
P=cd-2c-2d+1,       Q=2cd-c-d+2,
B=bP+Q,              C=bQ+P.
```

The negative factor theorem leaves `B=0` in the fixed-moving template and
`BC=0` in the moving-moving template. Since `C(b)=bB(1/b)`, inversion of
the unordered moving edge pair carries `C=0` to the represented `B=0`
case, including the other relative-`xi` orbit. Also `P!=0` on an admissible
retained locus, so put `b=-Q/P`.

## Reconstruction and its exceptional minor

Direct exact reconstruction on `B=0` gives the same incidence label `z`
and the same odd vector `V` in the two templates, while

```text
U_moving-moving = -U_fixed-moving.                 (1)
```

Thus both templates give the same `G=U^2-WV^2`. The convenient three-row
reconstruction minor is

```text
3(c-2)(2c-1)(d-2)(2d-1)(w-1)^3(w+1)^3
  *(cd-1)(cd+1)(5cd-4c-4d+5) / E^4.              (2)
```

The parent gates prove every factor in `(2)` nonzero on an admissible
candidate except possibly `cd+1`. On the near constant branches below,
`cd=-1` forces respectively `c=2`, `c=1/2`, or `c=b`, all label
collisions. Hence the rational reconstruction covers every admissible near
passer; no full-matrix exceptional fiber is omitted.

## Constant gate

After dividing the forced `(W-w)^4`, the monic observed quartic has constant
coefficient exactly one. The near target is

```text
((W-1/xi)(W-1/d))^2,
```

whose constant coefficient is `1/(xi^2 d^2)`. Passage therefore requires

```text
(xi*d)^2=1.                                        (3)
```

If `xi*d=1`, then `d=tau(xi)` is already a label of `J_0`, so the q-root
collides with `J_0`. Retain only `xi*d=-1`.

## The three minus branches

For `xi=2`, substitute `d=-1/2`. If `m_1,m_2,m_3` are the remaining
primitive mismatch numerators, then

```text
gcd(Res_w(m_1,m_3),Res_w(m_1,m_2))
  = (c+2)^4(13c-14)^4.                             (4)
```

At `c=-2` their common `w` gcd is `(w+1)^2`; at `c=14/13` it is
`(w-1)^2`.

For `xi=1/2`, substitute `d=-2`. The corresponding identities are

```text
projection = (2c+1)^4(14c-13)^4,                  (5)
c=-1/2:  gcd_w=(w+1)^2,
c=13/14: gcd_w=(w-1)^2.
```

For `xi=b`, equation `(3)` and `B=0` give `bd=-1` and

```text
2cd^2-2cd+2c-d^2+4d-1=0.                          (6)
```

The coefficient of `c` in `(6)` is `2(d^2-d+1)`. It cannot vanish together
with the remaining coefficient because their gcd divides `3d`, and the
deployed characteristic is neither `3` nor compatible with `d=0` there.
Thus substitute

```text
c=(d^2-4d+1)/(2(d^2-d+1)).                        (7)
```

The same two-resultant projection is

```text
d^2(d-1)^6(d+1)^6(d+2)^4
  *(d^3-6d^2+3d-2)^4.                             (8)
```

The complete common fibers are

```text
d=0:                         w^2,
d=-2,+1,-1:                  (w-1)^2,
d^3-6d^2+3d-2=0:             (w+1)^2.             (9)
```

Here `d=0,+/-1` are forbidden endpoint labels, and `d=-2` together with
`bd=-1` gives the forbidden collision `b=1/2`. Every other fiber has
`w=+/-1`, forbidden by the fixed-point-free source orbit.

Finally, direct Groebner saturation over `F_2130706433` is the unit ideal
for `(4)`, `(5)`, and `(8)` after adjoining the inverse of exactly the
forbidden products just listed. This prevents bad-prime factor growth and
proves the claim over `F_(2130706433^6)`. QED.
