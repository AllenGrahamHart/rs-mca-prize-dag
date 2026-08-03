# Proof

Let `A` be the affine hull of the parameter set `Tau`; its direction
dimension is `s`. Every member of `Tau` is a degree-`<K` polynomial agreeing
with the fixed punctured word on exactly `a=K+w` points. Applying the proved
affine-span RS list compiler to `A` gives `(LA1)`. The compiler counts every
listed word in `A`, so dropping maximality, selected blocks, and strip
ownership is safe for this upper bound.

Write one factor of the unfloored ratio as

```text
F_j(d,ell,e)=(R+ell-e+j)/(d+ell+j),       1<=j<=s.       (1)
```

It decreases when `e` increases, so its maximum has `e=2(h-d)`. There it is

```text
F_j=(R-2h+2d+ell+j)/(d+ell+j).                         (2)
```

Increasing `ell` by one decreases `(2)` because

```text
d+ell+j <= R-2h+2d+ell+j.
```

Increasing `d` by one replaces `(A/B)` by `(A+2)/(B+1)`, which is no larger
exactly when

```text
2B<=A,       equivalently ell+j<=R-2h.                   (3)
```

On every official row, `ell<=d-1<=h-3`, `j<=10`, and exact arithmetic gives
`h+7<=R-2h`. Thus `(3)` holds throughout the claimed range. Every factor,
and hence their product and its floor, is maximized by the smallest feasible
`d` and `ell`. With `ell=1`, feasibility of
`2(h-d)<=d-ell-1` is exactly `3d>=2h+2`, proving `(LA2)`.

At that corner put

```text
U=R+1-e_0,       V=d_0+1.
```

The affine cap is the exact integer quotient

```text
floor(C(U+s,s)/C(V+s,s)).                              (4)
```

Evaluating `(4)` gives the three displayed paid caps. Their respective next
values are

```text
rate 1/4,  s=10:  3,791,568,976,987,080,033,655,707,
rate 1/8,  s=10: 17,801,150,181,942,642,789,226,202,
rate 1/16, s= 9: 51,352,312,252,010,783,557,476,583,
```

all strictly above the local budgets. Since `(4)` increases with `s` when
`U>V`, the paid cutoffs are exactly `9,9,8`. This proves `(LA3)`. QED.

For completeness, the payment compares the worst cap to the smallest budget
over the entire active-defect range, not merely to the budget at the same
corner. Indeed `d<=h-2` gives `e>=4`, and the target budget increases with
`e`. Its universal minimum is therefore

```text
floor((17n^2-25(n-4))/25)
 = 3,288,278,229,349,592,331,945,250.
```

Each displayed paid cap is below this number. The first-unpaid caps are
above it (and also above the larger same-corner budgets), so the plain affine
compiler alone does not pay those dimensions.
