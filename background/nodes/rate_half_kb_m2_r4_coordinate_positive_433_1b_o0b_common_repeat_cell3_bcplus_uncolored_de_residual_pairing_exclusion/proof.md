# Proof

Fix a root-sign row, outside sign, and residual matching. Away from the five
case guards, the generic-rank node gives the unit ideal. At a guard root `u`,
solve the degree-two torus equation exactly for `r` and replay the original
common guard. A guard zero is outside the stated open locus.

At every remaining lift, reconstruct the six-entry cofactor kernel and the
missing-label equation. If its leading coefficient vanishes, the constant is
nonzero, so the missing product is inconsistent. If the recovered product
`q` is zero, the target coordinates violate the nonzero guard. Otherwise the
two missing endpoints are governed by

```text
x^4 + (2q-s)x^2 + q^2.
```

Exact `gcd(P,x^p-x)` certifies every listed endpoint root. For each of the
1,792 roots, reconstruct the three residual paired-product polynomials in the
last coordinate; their gcd is one. This excludes all 120 `DE+` cases. The
proved `d -> -d` involution bijects these with the 120 `DE-` cases. QED.
