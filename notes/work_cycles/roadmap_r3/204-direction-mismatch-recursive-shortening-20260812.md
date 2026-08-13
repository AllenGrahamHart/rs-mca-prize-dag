# Cycle 204: direction-mismatch recursive shortening (2026-08-12)

The low-direction residual from Cycle 203 has an exact recursive structure.
In a shortened row `(R+s,s,d+s)`, choose a minimum lift of the nonzero
direction syndrome:

```text
q=r_1-b,       wt(q)=R-j,       E=supp(q).
```

Every size-`(d+s)` pair-noncontained witness meets `E` at least `d-j`
times.  For each `x in E`, conditioning on witness agreement at `x` and
cancelling that coordinate gives an injective slope-preserving child in the
dimension-`s-1` row.  Any child direction residual lifts back to an original
direction residual of the same weight, so its defect satisfies `j_x<=j`.
Double-counting witness-coordinate incidences proves

```text
M_s(j) <= floor((R-j)M_(s-1)(j)/(d-j)),       0<=j<d.
```

The direct direction-distance bound and the recurrence are both monotone in
`j`, so this is a uniform bound for every child defect at most `j`.  Taking
the smaller direct/recursive bound at each dimension and starting at the
last all-defect affine-span payment yields:

```text
KoalaBear:   j<=4330 paid at s=14 and through s=22;
             j<=9 at s=4982, j<=8 at s=4983;
             rank-regular j=0 paid through s=4992.
Mersenne-31: j<=4334 paid at s=6, j<=4333 at s=7;
             j<=1 at s=4978, j=0 at s=4979.
```

Compared with the direct router, the recurrence extends 4,331 KoalaBear
defects by up to ten dimensions and 4,335 Mersenne defects by one dimension.
It does not pay `j>=d` or the complement of the exact recursive envelope.

The primary verifier performs 21,686,730 defect-major transitions and four
mutations.  The independent dimension-major audit performs 21,560,478
transitions and three controls.  Both use bounded integer state under
RAMguard; no Modal compute is used.

```text
start:                   d21366a88
result:                  PROVED direction-mismatch shortening recurrence
DAG delta:               +1 PROVED background node, +3 edges
critical status delta:   none
upstream terminal delta: exact low-direction paid envelope expanded;
                         residual complement remains
delta-star movement:     none
compute:                 bounded local integer loops under RAMguard;
                         no Modal spend
next route action:       seek structure in the high-defect residual
```
