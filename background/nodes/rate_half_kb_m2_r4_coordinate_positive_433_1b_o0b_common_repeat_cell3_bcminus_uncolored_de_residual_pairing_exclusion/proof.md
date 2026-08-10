# Proof

Fix a root-sign row, outside sign, and residual matching. Away from its exact
case guards, the generic-rank node gives the unit ideal. The guard-lift atlas
exhausts every deployed-field root and supplies all guarded `(q,y,r)` common
points above it.

At every remaining lift, reconstruct the six-entry cofactor kernel and the
missing-label equation. If its leading coefficient vanishes, the constant is
nonzero, so the missing product is inconsistent. If the recovered product
`q` is zero, the target coordinates violate the nonzero guard. Otherwise the
two missing endpoints are governed by

```text
x^4 + (2q-s)x^2 + q^2.
```

Exact `gcd(P,x^p-x)` certifies every listed endpoint root. For each of the
512 roots, reconstruct the three residual paired-product polynomials in the
last coordinate; their gcd is one. This excludes all 120 `DE+` cases. The
proved `d -> -d` involution bijects these with the 120 `DE-` cases. QED.
