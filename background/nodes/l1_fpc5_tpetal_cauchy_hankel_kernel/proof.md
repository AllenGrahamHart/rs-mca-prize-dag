# Proof: FPC5 Cauchy-Hankel kernel

For any polynomial `P=sum_a p_a X^a`, linearity of the weighted moments
gives

```text
M_j(P)=sum_a p_a M_j(X^a)
      =sum_a p_a mu_(j+a).                            (1)
```

Applying `(1)` to the `c=h-d-1` equations of the owner-free Cauchy chart
proves `(HK3)`. The matrix is Hankel because its entry depends only on
`j+a`.

The incoming theorem identifies `ker H_mu` with the complete locator image
of the pair slice. Under a saturated primitive monic anchor, the
saturated-slice dimension theorem gives this image dimension `e+1`.
Rank-nullity therefore gives

```text
rank H_mu=(d+1)-(e+1)=d-e=h-d-1=c,
```

proving `(HK4)`.

Lagrange interpolation for `chi` gives

```text
chi(X)/Lambda(X)
 =sum_(z in T)c(z)/(Lambda'(z)(X-z)).                 (2)
```

Expanding `(2)` at infinity proves `(HK5)`. Multiply `(HK5)` by `Lambda`.
The result is the polynomial `chi`, so every negative-power coefficient
vanishes. The coefficient of `X^(-s-1)` is exactly the left side of
`(HK6)`, proving the recurrence.

The incoming theorem already proves that the split locator predicate is
`G|L_Core`, while its low-numerator predicate is the moment system. This
gives `(HK7)`. It also gives the primitive condition

```text
M_0(G/(X-x))!=0.
```

Equation `(1)` at `j=0` is exactly `(HK8)`. QED.
