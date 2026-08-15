# Proof

Represent the selected affine explanation family by parameter points in
`F^2`.  At each coordinate, agreement is an affine line with a normal in
`F^2`.  Every selected point lies on the `m=67473` lines indexed by its
exact support.

The common-zero bound from support-local transversality gives

```text
z <= K-s = 1-1 = 0,
```

so every incident normal is nonzero.  Same-support pair noncontainment gives
full incident rank, hence the `m` normals incident with any selected point
occupy at least two projective classes.

Let the nonempty projective-class sizes be `a_1,...,a_c`, where `c>=2` and
their sum is `m`.  The ordered pairs with dependent normals are exactly the
pairs lying in one class, so the number of ordered independent pairs is

```text
m^2-sum_i a_i^2.
```

For at least two nonempty classes, convexity gives

```text
sum_i a_i^2 <= (m-1)^2+1.
```

Thus every selected point owns at least `2(m-1)=134944` ordered independent
coordinate pairs.  Two independent affine lines in `F^2` meet in at most
one point, so one ordered coordinate pair can be owned by at most one
selected point.  There are `n(n-1)=1099512676352` ordered pairs of distinct
coordinates.  Double counting yields

```text
|Z| <= floor(1099512676352/134944)=8147918,
```

with remainder `29760`.
