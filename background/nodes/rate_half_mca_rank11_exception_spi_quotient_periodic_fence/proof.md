# Proof

Because the field contains the cyclic evaluation group `mu_N` and `e|N`,
the homomorphism

```text
pi_e:mu_N -> mu_(N/e),       x |-> x^e
```

is surjective with kernel `mu_e`. Every `y in mu_(N/e)` therefore has
exactly `e` preimages, forming one coset of `mu_e`. These are exactly the
roots of `X^e-y` in the field.

The characteristic is coprime to the power-of-two domain order, so it does
not divide `e`. The derivative `eX^(e-1)` is nonzero at every root in
`mu_N`; hence `X^e-y` is squarefree. It is monic of degree `e`, split over
the domain, and divides `X^N-1` because `y^(N/e)=1`.

Fibers of a function are disjoint. Thus the `N/e` values of `y` give
`N/e` pairwise-disjoint split locators in the affine pencil

```text
u+gamma v=X^e+gamma,       gamma=-y.
```

Here `v=1`, so `gcd(u,v)=1`; the scalar multiplying each monic locator is
one and never vanishes. The degrees `1,2,4,8` all lie in the proved
exception interval `1..11`.

At `N=2^21=2097152`, the fiber counts are

```text
2097152, 1048576, 524288, 262144,
```

respectively. All exceed twenty. Hence no argument using only degree at
most 11, coprimality, splitting, squarefreeness, and twenty disjoint fibers
can prove the exception pencil empty or uniformly small. QED.
