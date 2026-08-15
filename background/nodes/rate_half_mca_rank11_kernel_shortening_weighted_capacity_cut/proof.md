# Proof

The shortening-weighted parent bounds decorated record/extension incidences
over one rank-`(10-d)` basis by `U_d(K')`.  There are
`C(n',10-d)` possible bases, while every undecorated incidence has at least
`d+2` basis decorations.  Therefore the displayed sum is a valid capacity
upper bound.  No hierarchy or shared-resource optimization is needed.

Let `G(K')` be the rational demand minus this unfloored capacity.  Every
factor is a binomial polynomial in `K'`, so `G` has degree at most eleven.
Put `K_0=796599`.  Exact forward differencing gives

```text
Delta^j G(K_0) > 0,       0<=j<=11.
```

Newton interpolation now gives, for every integer `s>=0`,

```text
G(K_0+s)=sum_(j=0)^11 C(s,j) Delta^j G(K_0) > 0.
```

This covers the complete remaining official interval.  The proof uses the
unfloored rational capacity, so subsequent integer floors only strengthen
the strict inequality.  An independent audit expands the same polynomial
in ordinary powers of `s=K'-K_0`; all twelve coefficients are positive.

The corank-three capacity parent already excludes `10<=K'<=796598`.
Combining the adjacent intervals removes the fixed-kernel branch on every
official row.
