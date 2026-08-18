# Quotient-periodic fence for the exception SPI

- **status:** PROVED
- **scope:** the algebraic hypotheses of the bounded exception split-pencil
  normal form

Let the smooth evaluation domain be the cyclic group `mu_N`, where `N` is a
power of two. For

```text
e in {1,2,4,8},       e|N,
```

put

```text
u=X^e,       v=1.
```

For every `y in mu_(N/e)`, the slope `gamma=-y` gives

```text
u+gamma v=X^e-y.
```

This is a split squarefree degree-`e` domain locator. Its root set is one
coset of `mu_e` in `mu_N`; different `y` give disjoint cosets. Hence the
pencil has `N/e` pairwise-disjoint split fibers, while `gcd(u,v)=1` and the
locator scalar is the nonzero constant one.

For the official domain length `N=2097152`, the smallest count among these
four degrees is

```text
N/8=262144>20.
```

Therefore twenty disjoint split fibers do not force emptiness, bounded
fiber count, or a fixed locator. The quotient-periodic power-map class must
be identified and priced, or additional branch semantics must be used.

This is not an actual MCA counterexample and does not prove that the
quotient-periodic model lifts to the complete heavy-ruling packet.
