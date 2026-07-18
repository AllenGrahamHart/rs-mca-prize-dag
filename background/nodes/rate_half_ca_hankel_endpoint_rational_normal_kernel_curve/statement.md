# Rational-normal kernel curve at the strict endpoint

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`

Use the official first strict `A=3` endpoint

```text
m=2^37,       N=16m,       T=4m+1,
r=rho=4m-1,   e=m.
```

Thus the syndrome Hankel pencil has size `(4m+1) x 4m`, generic rank
`4m-1`, and a primitive degree-`rho` apolar kernel generator of parameter
degree `m`.  In homogeneous parameter coordinates, write

```text
Q(U,V;X)=sum_(j=0)^m Q_j(X) U^(m-j)V^j.               (RNC1)
```

Then the `m+1` forms

```text
Q_0(X),...,Q_m(X) in F[X]_(<=rho)                     (RNC2)
```

are linearly independent.  Consequently the separation rank of the full
biform `Q` is exactly `m+1`, the largest value allowed by its parameter
degree, and

```text
nu_Q:P^1_(U:V) -> P(span_F{Q_0,...,Q_m}),
(U:V) |-> [Q(U,V;X)]                                  (RNC3)
```

is a degree-`m` rational normal curve over `F`.  Evaluation on the domain
`D` is injective on forms of degree at most `rho<N`, so the same curve is
rational normal in the evaluation-vector space.

The endpoint defect ledger gives the following incidence structure on this
curve.  For `x in D`, let

```text
H_x={ [P] : P(x)=0 }
```

inside the projective coefficient span.  There are at least `3m+2`
supported parameters at which `nu_Q` represents a squarefree degree-`rho`
form split over `D`, hence lies on `rho` distinct hyperplanes `H_x`.  There
are at least `15m` domain points `x` for which the hyperplane section

```text
H_x intersect nu_Q(P^1)
```

consists of exactly `m` distinct supported parameter points.  At least
`3m+1-O` of the split supported points are parameter-transverse in all their
`rho` domain hyperplane sections.

This theorem strengthens the former separation-rank lower bound from three
to the exact maximum.  It does not exclude the endpoint: the remaining gate
is a rigidity theorem for this rational normal kernel curve together with
its Hankel/apolar origin, the multiplicative-domain evaluation hyperplanes,
and the already-proved norm/Bezout identities.
