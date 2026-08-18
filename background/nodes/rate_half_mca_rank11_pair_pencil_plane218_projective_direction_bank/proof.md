# Proof

Fix 218 selected types in one affine scalar plane. They span the plane
because an affine line contains at most 15 selected types. Factor the gcd of
the two-dimensional difference space and let `J_A` be the common
received-pair core, of size `c`.

Outside `J_A`, every coordinate has owner multiplicity at most 15. Counting
the 218 cores of size `s=m-2=1116046` gives

```text
218s<=218c+15(n-c),
c>=ceil((218s-15n)/(218-15))=1043551.                (1)
```

Two distinct pair codewords give `c<=K-1`. Shorten by the actual core and
write `k'=K-c`. Then initially

```text
1<=k'<=K-1043551=5025,
n'=1048576+k',       s'=67470+k'.                   (2)
```

Every residual coordinate still has multiplicity at most 15. The exact
deficit from full 15-fold occupancy is

```text
Delta=15n'-218s'=1020180-203k'.                     (3)
```

Thus the number `F` of multiplicity-15 coordinates satisfies

```text
F>=n'-Delta=28396+204k'.                             (4)
```

Each full coordinate fiber is an affine line containing 15 selected scalar
points. Through one point there are at most
`floor(217/14)=15` such lines, because distinct lines through it use
disjoint sets of 14 other points. Double-counting point-line incidences
therefore gives at most

```text
floor(218*15/15)=218                                 (5)
```

full affine lines.

Group those lines by projective direction. For one represented direction
choose its nonzero residual scalar direction polynomial `T_eta`. Every
coordinate realizing any full line of that parallel class is a root of
`T_eta`, whose degree is at most `k'-1`. Hence

```text
z_eta<=k'-1.                                         (6)
```

Every full coordinate has one fiber and one direction, so `sum z_eta=F`.
If `r` is the number of represented directions, `(4)` and `(6)` give

```text
r>=ceil((28396+204k')/(k'-1)).                       (7)
```

Since `r<=218`, equations `(4)`--`(7)` imply

```text
28396+204k'<=218(k'-1),
k'>=ceil(28614/14)=2044.                             (8)
```

For every `k'<=5025`, one also has

```text
28396+204k'>209(k'-1),
```

because the difference `28605-5k'` is at least 3480. Thus `r>=210`.
There are at least `r` full lines and at most 218 by `(5)`, proving both
line and direction ranges.

The aggregate unused degree capacity obeys

```text
sum_eta((k'-1)-z_eta)
 =r(k'-1)-F
 <=218(k'-1)-(28396+204k')
 =14k'-28614
 <=41736.                                            (9)
```

The ratio in the statement is minimized at the largest `k'=5025`:

```text
(28396+204*5025)/(218*(5025-1))
 =1053496/1095232=131687/136904>0.9618.              (10)
```

Finally dualize the 218 scalar points. Every full 15-secant becomes a point
where 15 of the 218 dual lines meet. At least 210 such points consume
`210*binom(15,2)=22050` of the `binom(218,2)=23653` line pairs, leaving at
most 1603 line-pair intersections elsewhere. QED.
