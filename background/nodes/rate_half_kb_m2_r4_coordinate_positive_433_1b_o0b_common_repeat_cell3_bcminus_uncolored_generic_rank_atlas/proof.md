# Proof

Represent the genus-two function field as the tower

```text
F_p(q) subset F_p(q)(y) subset F_p(q)(y)(r),
y^2=N(q)/D(q),
r^2=epsilon_1(iota+epsilon_2)(c-b)/(bc-1)r-epsilon_2 iota,
```

with `b=(qy+1)/(qy-1)` and `c=(y+1)/(y-1)`. Exact tower arithmetic first
replays `F(b,c)=0` and the quadratic relation. It then constructs the common
kernel, missing-product quartic extension, and all residual record values.

For each formal case, take each pair of the three residual pairing equations
in increasing degree-sum order. Flatten its Sylvester matrix through the
quartic extension and compute rank by exact Gaussian elimination over the
tower. In all 360 cases the first tested matrix is `16 x 16` and has rank 16.
A nonzero determinant proves the two equations have no common missing
residual coordinate over the generic function field.

Every inverted numerator and the determinant norm down to `F_p(q)` is
recorded. There are 47 distinct normalized guards. Away from their zeros all
constructions are defined and the selected determinant is nonzero, so no
outside solution exists. QED.
