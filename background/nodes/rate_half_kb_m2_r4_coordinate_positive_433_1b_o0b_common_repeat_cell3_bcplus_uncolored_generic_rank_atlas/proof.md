# Proof

Work over `K=F_p(u)[r]/(H_epsilon)`, where `H_epsilon` is the proved cell-3
`BC+` torus equation. The cofactor construction gives the exact common
coefficient kernel. For each missing record, its product and squared sum give
the endpoint relation

```text
x^4 + (2q-s)x^2 + q^2 = 0.
```

Adjoin this quartic without assuming it irreducible. Each residual record is
then affine in one coordinate `y`, and each matching gives three polynomials
in `y` over the four-dimensional quotient algebra. Flatten the regular
representation of the Sylvester matrix for equations zero and one to `K`.
Exact fraction-free function-field elimination gives full rank in all 360
cases: rank 16 in 248 cases and rank 24 in 112 cases.

Every inversion pivot and the residual determinant norm is recorded as a
guard. Hence the two selected equations generate the unit ideal whenever the
five case guards are nonzero. The resulting 1,800 guard incidences deduplicate
to 54 exact polynomials. Exceptional roots are explicitly outside this
claim. QED.
