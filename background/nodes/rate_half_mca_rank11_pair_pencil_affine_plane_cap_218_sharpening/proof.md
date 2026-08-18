# Proof

## Exclude 219 points in an affine plane

Assume an affine scalar plane contains at least 219 selected types and retain
exactly 219. They cannot lie on an affine line because the line cap is 15,
so their affine span has dimension two. Factor the gcd of the plane's
two-dimensional difference space and let `J_A` be the corresponding common
received-pair core. Put `c=|J_A|`.

At a coordinate in `J_A`, all 219 cores occur. At a nonmatching gcd root no
core occurs. At every other coordinate, the owners lie in one affine line
and their number is at most 15. Since two distinct pair codewords agree on
at most `K-1` coordinates, `c<=K-1`. Counting the 219 cores of size
`s=m-2=1116046` gives

```text
219s<=219c+15(n-c),
c>=ceil((219s-15n)/(219-15))=1043906.                (1)
```

Shorten the 219-type family by its actual common core. This is the same
reversible pair shortening proved earlier. Write

```text
k'=K-c,       1<=k'<=4670,
n'=n-c=1048576+k',
s'=s-c=67470+k'.                                    (2)
```

Every residual coordinate has multiplicity at most 15. Therefore the total
deficit from full 15-fold occupancy is

```text
Delta=15n'-219s'=952710-204k'>=0.                   (3)
```

Every nonfull coordinate contributes at least one unit to `Delta`, so the
number `F` of coordinates with multiplicity exactly 15 satisfies

```text
F>=n'-Delta=95866+205k'.                             (4)
```

A full coordinate fiber is an affine line containing 15 of the 219 scalar
points. Through one selected point there are at most

```text
floor((219-1)/(15-1))=15
```

such lines, because their other 14-point sets are disjoint. Double-counting
point-line incidences therefore bounds the number of full lines by 219.

One fixed full line can occur at at most `k'-1` coordinates. Indeed, choose
two selected points on it. Their nonzero residual scalar difference has
degree at most `k'-1`, and it vanishes at every coordinate realizing that
line. Hence

```text
F<=219(k'-1).                                        (5)
```

But `(4)` and `(5)` would require

```text
95866+205k'<=219(k'-1),
0>=96085-14k'>=96085-14*4670=30705,
```

a contradiction. Thus 219 points cannot lie in an affine plane, proving
the cap 218.

## Dimension three

Factor the gcd of the complete three-dimensional scalar space and let `J`
be its common received-pair core. Every coordinate outside `J` belongs to at
most 218 cores: a non-gcd evaluation fiber is an affine plane, while a
nonmatching gcd root has multiplicity zero. Thus

```text
520(m-2)<=520|J|+218(n-|J|),
|J|>=ceil((520*1116046-218*2097152)/(520-218))
   =407831.                                          (6)
```

The reversible shortening preserves first ownership, quotient deficiency
two, and `m-K=67472`. At the minimum floor, direct subtraction gives

```text
n'=1689321, K'=640745, m'=708217, s'=708215,
218n'-520s'=178.                                     (7)
```

## Dimension four

At a non-gcd coordinate, owners lie in an affine three-space. If every
coordinate outside the common core has multiplicity at most 218, the same
incidence calculation `(6)` forces `|J|>=407831` and shortening applies.
Otherwise some actual noncommon coordinate has at least 219 owners. The
plane cap shows that these owners cannot lie in an affine plane, so their
affine span is exactly three. The 29-record selected-type floor and disjoint
first-owner currencies give at least `219*29=6351` records, all containing
the exhibited coordinate in their exact supports. QED.
