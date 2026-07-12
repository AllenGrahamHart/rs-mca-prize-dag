# petal_g3_profile_conversion_identity

- **status:** PROVED
- **closure:** proof

Partition an `n=MN` point domain into `N` fibers of size `M`. For a support
`R` of size `A=hM+b`, where `0<=b<M` and `0<=h<N`, call `R` scale-`M`
admissible when the points outside its fully contained `M`-fibers have size
less than `M`. Let `raw_M(A)` be the number of admissible supports and put

```text
H_M(x) = sum_{j=0}^{M-1} C(M,j)x^j,
Q_M(A) = C(N-1,h).
```

Then

```text
raw_M(A)
  = C(N,h) [x^b] H_M(x)^(N-h)
  = Q_M(A) * N/(N-h) * [x^b] H_M(x)^(N-h).
```

Thus the canonical-support weight is one per support class, and its exact
conversion to the fixed-tail quotient-coset convention is the displayed
factor. No unspecified integer or scale-only multiplicity is used.
