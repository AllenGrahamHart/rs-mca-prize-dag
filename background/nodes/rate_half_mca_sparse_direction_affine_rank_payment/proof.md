# Proof

Gauge the line by `b`.  The codeword-direction gauge theorem preserves exact
agreement supports and pair noncontainment.  For every selected slope, the
transformed explanation `a_gamma` agrees with `r_0` on at least `d+K-e`
coordinates outside `E=supp(q)`.

Puncture `E`.  The ambient code remains an injective Reed-Solomon evaluation
of dimension `K`, while the transformed selected explanations lie in an
affine subspace of dimension at most `r`.  The punctured parameters are

```text
n'=R+K-e,       K'=K,       m'=d+K-e,
w'=m'-K'=d-e.
```

The ordinary affine-span list theorem therefore bounds the number of
distinct transformed explanations by

```text
floor(C(n'-K'+r,r)/C(w'+r,r))
 = floor(C(R-e+r,r)/C(d-e+r,r)).
```

As in the full-code special case, pair noncontainment forces every witness
to meet `E`, and for fixed `(a,x)` with `x in E`, the equality

```text
a(x)-r_0(x)=gamma q(x)
```

determines at most one slope.  Each transformed explanation owns at most
`e` slopes, proving `(SR1)`.

For fixed `r` the exact bound is increasing over the legal support-size
range checked in the certificate.  Adjacent evaluation at each contract
wall therefore proves every displayed prefix without a floating-point
comparison.
