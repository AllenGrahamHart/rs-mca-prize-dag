# proof: xr_triangular_minor_certificate_soundness

Let `A` be the specialized square minor matrix named by the certificate.
Because the specialization is admissible, the entries of `A` live in the
coefficient field of the profile chart.

If `A` is upper or lower triangular, its determinant is the product of its
diagonal entries:

```text
det(A) = prod_i A_{ii}.
```

This is the standard Leibniz determinant formula: every permutation except the
identity uses at least one entry on the zero side of the triangular matrix and
therefore contributes zero.

The certificate asserts that every diagonal entry is nonzero. Since the
coefficient ring after admissible specialization is a field, the product of
nonzero diagonal entries is nonzero. Hence `det(A) != 0`.

Therefore a triangular certificate with nonzero diagonal is a valid
nonzero-minor specialization certificate.
