# Proof

On one block, the equation `U=0` says that the first pair and second pair
have equal Hamming weight. The possible common weights are `0,1,2`, so

```text
#{U=0}=binom(2,0)^2+binom(2,1)^2+binom(2,2)^2=6.
```

The same count applies to `V=0` after permuting the coordinates. Subtracting
the two equations gives `2(X_2-X_3)=0`; over the integers this is equivalent
to `X_2=X_3`. Substitution then gives `X_1=X_4`. Thus the joint event has
four assignments.

Different four-bit blocks use disjoint independent coordinates. Requiring
the corresponding equation in every block therefore tensors all three
counts:

```text
P(A_r)=(6/16)^r,
P(B_r)=(6/16)^r,
P(A_r intersect B_r)=(4/16)^r.
```

Their quotient is `(16/9)^r`.

Within a block the coefficient vectors are

```text
u=(1,1,-1,-1),       v=(1,-1,1,-1).
```

Both have coordinate sum zero and `u dot v=0`. Rows from different blocks
have disjoint support, so every `U` row is orthogonal to every `V` row.

At `r=3`, squaring the desired comparison gives

```text
(16/9)^6 > 24 = 2(4r),
```

which the exact integer inequality `16^6 > 24*9^6` verifies. Finally,
`r log(16/9)` grows linearly while `C log(4r)` grows logarithmically, so the
ratio exceeds `(4r)^C` for every fixed `C` once `r` is large enough. QED.
