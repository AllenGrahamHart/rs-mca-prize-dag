# Refutation

Take

```text
F=F_17,
D=mu_8=(1,2,4,8,16,15,13,9),
C=RS[F_17,D,2],
A=3,
u=(0,0,0,0,0,0,1,1),
v=(0,0,0,0,0,0,1,2).
```

The pair agrees jointly with the zero codeword pair on the first six
coordinates, so it is globally tangent at agreement `A`. Here `r=n-A=5`,
the advertised tangent slot is `r+1=6`, and the deep hypothesis fails:

```text
3r=15>n-K=6.
```

Direct interpolation of degree-below-two polynomials on every three-point
support gives the exact support-wise MCA-bad slopes

```text
1, 2, 4, 8, 9, 13, 15, 16.
```

Thus there are eight bad slopes, exceeding `r+1=6`. Lexicographically first
bad supports are, in the same order,

```text
(2,6,7), (1,6,7), (0,6,7), (0,1,7),
(3,6,7), (4,6,7), (5,6,7), (0,1,6).
```

They are distinct, have pairwise intersections of size at most `K=2`, and
each has trivial stabilizer under cyclic rotation of `mu_8`. The pair is not
a pullback through the only nontrivial divisor of `gcd(n,K)`: its values are
not constant on the `x -> x^2` fibers. Hence neither a high-overlap rung nor
the elementary quotient strip removes the witness family.

For every listed support, the line word has a degree-below-two explanation
but `u` and `v` do not both have degree-below-two explanations on that same
support. This is the support-wise MCA condition checked by `verify.py`.
