# Proof

Let the list contain `s` distinct polynomials.  For each polynomial choose
exactly `N` of its agreement positions and call the resulting set `A_i`.
Distinct degree-`<=d` polynomials agree at no more than `d` evaluation points,
so

```text
sum_x C(r_x,2) = sum_(i<j) |A_i intersect A_j| <= d C(s,2),
```

where `r_x` is the number of selected sets containing `x`.  Since every
selected set has size `N`, `sum_x r_x=sN`.  Cauchy-Schwarz gives

```text
sum_x C(r_x,2)
  = (sum_x r_x^2-sN)/2
 >= ((sN)^2/ell-sN)/2.
```

Combining the two displays and cancelling `s/2` yields

```text
s (N^2/ell-d) <= N-d.
```

The assumed strict Johnson inequality makes the left coefficient positive,
so

```text
s <= ell (N-d)/(N^2-d ell).
```

Taking the integer floor proves the exact bound.  Also `N<=ell` and
`N^2>d ell` imply `N>d`; the denominator is a positive integer, so the bound
is at most `ell(N-d)<=ell^2`.  Restricting to a property-filtered sublist can
only decrease `s`.  A G1 chart is precisely such a degree-`<=d` auxiliary RS
list on its petal union `T`, which gives the stated K4 consequence.
