# Proof

Shorten by the complete common received-pair core `J`. The 520 residual pair
cores have size `s'=67470+K'` in a residual domain of size
`n'=1048576+K'`. Scalar dimension three survives, so `K'>=3`.

For distinct selected types `p,q`, their residual scalar-polynomial
difference is nonzero and has degree below `K'`. Every coordinate in both
residual pair cores is a root of this difference. Therefore

```text
|H'_p intersection H'_q|<=K'-1.                    (1)
```

Let `d_x` count residual pair cores containing coordinate `x`. Counting
incidences and pair incidences gives

```text
I:=sum_x d_x=520(67470+K'),                         (2)
sum_x C(d_x,2)
 =sum_(p<q)|H'_p intersection H'_q|
 <=C(520,2)(K'-1).                                  (3)
```

For integers with fixed sum `I` over `n'` slots, convexity of `C(d,2)` shows
that the minimum is attained when all multiplicities differ by at most one.
Write

```text
I=a n'+r,       0<=r<n'.
```

Then

```text
sum_x C(d_x,2)
 >=(n'-r)C(a,2)+rC(a+1,2)
 =aI-C(a+1,2)n'.                                   (4)
```

For `3<=K'<=4835`, exact division gives three intervals:

```text
a=33  for 3<=K'<=1167,
a=34  for 1168<=K'<=3331,
a=35  for 3332<=K'<=4835.                          (5)
```

On an interval with fixed `a`, pair capacity minus the lower bound `(4)` is
affine in `K'`, with slope

```text
C(520,2)-520a+C(a+1,2).
```

The three slopes are respectively 118,341, 117,855, and 117,370, all
positive. Direct evaluation at the two interval transitions gives

```text
gap(1167)=-431565057,       gap(1168)=-431447180,
gap(3331)=-176526815,       gap(3332)=-176409220.
```

Thus the gap increases throughout the complete range. At its final point,

```text
gap(4835)=-2110.                                    (6)
```

Every `K'<=4835` therefore violates `(3)`--`(4)`. At the adjacent row the
same exact calculation gives

```text
gap(4836)=115260,                                   (7)
```

so this moment argument first permits `K'=4836`.

The parent rich-plane theorem gives `K'<=595763`. Finally `K=1048576` and
`|J|=K-K'`, so the two dimension bounds are equivalent to

```text
452813<=|J|<=1043740.
```

QED.
