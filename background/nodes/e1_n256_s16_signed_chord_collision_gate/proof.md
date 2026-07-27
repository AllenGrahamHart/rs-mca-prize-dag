# Proof

Put `T={i:c_i!=0}`. For profile `(3,4,0)`, the seven nonzero
coefficient magnitudes are

```text
2,2,2,1,1,1,1.
```

Hence

```text
S=sum_i c_i^2=16,
sum_i c_i^4=3*16+4=52,
sum_(i<j) (c_i c_j)^2=(S^2-sum_i c_i^4)/2=102.       (3)
```

For `1<=d<=63`, each unordered pair at circular distance `d`
contributes exactly one signed product `w_e` to the positive-half
negacyclic autocorrelation coefficient

```text
A_d=sum_(d(e)=d) w_e.
```

A pair at distance 64 contributes zero: its two ordered correlation terms
cancel because `X^64=-X^-64` modulo `X^128+1`. The
antisymmetry `A_(128-d)=-A_d` therefore gives

```text
V=2 sum_(d=1)^63 A_d^2.
```

Expand the squares and use (3):

```text
V/2
 = sum_(d=1)^63 sum_(d(e)=d) w_e^2
   +2 sum_(d=1)^63 sum_(e<f, d(e)=d(f)=d) w_e w_f
 =102-D_64+2C.
```

This proves (1).

The diameter map `i -> i+64` is an involution without fixed points,
so diameter chords among seven support points form a matching. Their squared
endpoint weights are drawn from `4,4,4,1,1,1,1`. The maximum matching
weight is obtained by pairing two heavy vertices, the remaining heavy vertex
with a light vertex, and two light vertices:

```text
D_64<=4*4+4*1+1*1=21.                                 (4)
```

Since the surviving variance is even and at most 134, `V/2<=67`.
Equations (1) and (4) imply

```text
2C=V/2-102+D_64 <= 67-102+21=-14,
```

so `C<=-7`.

The negative total forces at least one negative product `w_e w_f`
between two distinct chords of the same non-diameter circular length. If the
two chords share a vertex, equality of their unoriented differences gives a
three-term progression modulo 128. If they are disjoint, it gives one of the
two four-point parallelogram equations. The negative product records the
required orientation-and-coefficient sign cancellation.
