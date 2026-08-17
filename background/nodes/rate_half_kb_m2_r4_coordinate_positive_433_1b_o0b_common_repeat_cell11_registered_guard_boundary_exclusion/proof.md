# Proof

The sealed generic rank atlas contains 15 distinct construction guards for
`BC+` and 27 for `BC-`. Factor every guard over the deployed base field. A
guard root on `x*y*(x-1)*(x+1)=0` is excluded by the symmetric tower chart
coverage theorem. At every other root, specialize the exact `y`-plane and
quadratic `r` tower, recover `b,c`, and test the original six common equations
and original common guard. This gives exactly 160 guarded source points:
32 on the four `BC+` towers and 128 on the four `BC-` towers.

At each point, recompute the six common-kernel cofactors directly over the
base field. The interpolation checks vanish and the missing-label cofactor is
nonzero, so the missing product `q` and squared sum `s^2` are defined. For
colored missing `BE` and `CF`, substitute `q/b` or `q/c`; none of the 320
necessary squared-sum identities vanishes.

For an uncolored missing record, every first endpoint is a base-field root of

```text
X^4 + (2q-s^2)X^2 + q^2.
```

For each root, missing record, outside sign, and residual matching, form the
three universal paired-product polynomials in the remaining endpoint. Their
common divisor has no base-field root in every one of the 34,560 cases. Thus
no colored or uncolored missing packet lies on a registered construction
guard. QED.

The primary computation uses FLINT only for base-field root extraction. The
independent verifier uses a separate modular Gaussian determinant and pure
Python polynomial Euclidean arithmetic. It proves root lists exhaustive by
computing `gcd(f,X^p-X)` and replays every paired-product system.
