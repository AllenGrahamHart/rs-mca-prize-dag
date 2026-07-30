# Proof

The six displayed generators in (RC1) have distinct degrees

```text
4980, 4979, 0, 1, 2, 3,
```

so they are linearly independent. Since `1` belongs to `V`, the space has no
common zero anywhere.

For each `a in S minus R0`, the polynomial

```text
J_a=R(X-a)=R X-aR
```

belongs to the two-dimensional subspace `span{R X,R}`. It is monic of degree
`t`, and its root set is the disjoint union `R0 union {a}`. Hence `J_a`
divides `L_S`.

Different `a` give different monic polynomials and therefore different
projective classes. Their number is

```text
|S|-|R0|=m-(t-1)=m-t+1=67449>15413.
```

This proves the route cut. QED.
