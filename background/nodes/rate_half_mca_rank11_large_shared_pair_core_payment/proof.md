# Proof

Write `Z_hi={gamma:theta_gamma>=388}` and
`Z_lo={gamma:theta_gamma<=387}` after the intrinsic near deletion. The
support-local error-rank router, applied to every affine subrank of the high
family, gives

```text
|Z_hi| <= 274790124064526354.                 (1)
```

It remains to count `Z_lo` under the displayed common-core premise.

## Shortening the common pair core

Put `c=|J|`. If `c>=K`, every two minimizing pairs are identical: both
component differences are degree-below-`K` polynomials with at least `K`
roots. Then the fixed-pair bound already gives at most `n-m+1` low records.

Assume instead that `c<K` and put `d=K-c`, so `1<=d<=4922`. Fix one
minimizing pair `(a_0,b_0)`. Every difference

```text
(a-a_0,b-b_0)
```

vanishes on `J`. After deleting `J` and dividing by its locator, these
differences form a two-fold interleaving of a generalized Reed-Solomon code
of length and dimension

```text
N_d=n-c=(n-K)+d=1048576+d,
dimension=d.
```

A low-margin pair has `|H_(a,b)|>=m-387`. Hence its shortened tuple agrees
with the shortened received tuple on at least

```text
A_d=m-387-c=d+67085
```

common coordinates.

## Ordinary Johnson count

For completeness, consider `L` distinct words of an `[N_d,d]` MDS code,
each agreeing with one received word on at least `A_d` coordinates. Their
agreement sets meet pairwise in at most `d-1` points. If `r_x` is the number
of sets containing coordinate `x`, then

```text
sum_x C(r_x,2) <= C(L,2)(d-1)
```

while Cauchy-Schwarz gives

```text
sum_x C(r_x,2) >= ((L A_d)^2/N_d-L A_d)/2.
```

Therefore, whenever the denominator is positive,

```text
L <= floor(N_d(A_d-d+1)/(A_d^2-N_d(d-1))).       (2)
```

Here `A_d-d+1=67086`, and the denominator simplifies exactly to

```text
D(d)=4501445801-914405d.
```

It is positive through `d=4922`, where

```text
N_d=1053498, A_d=72007, D(d)=744391,
floor(1053498*67086/744391)=94943.
```

At `d=4923` the denominator is `-170014`. Since the numerator increases and
the positive denominator decreases, `94943` is a uniform ordinary-list
bound over the complete stated interval.

The deployed field has size `2130706433^6`, larger than `94943^2`.
The proved sub-square-root common-support interleaving collapse therefore
gives the same `94943` bound for distinct minimizing ordered pairs.

## Fixed-pair multiplicity and budget

For a fixed pair, the exception sets of distinct finite slopes are disjoint.
The rank-eleven pair-core theorem consequently bounds its records by

```text
c_delta=floor((n-m+delta)/delta)<=n-m+1=981105.
```

Thus

```text
|Z_lo| <= 94943*981105 = 93149052015.             (3)
```

Combining (1), (3), and the disjoint near charge gives

```text
134944+274790124064526354+93149052015
  =274790217213713313
  =B_*-190510897681774.
```

This proves the branch payment.
