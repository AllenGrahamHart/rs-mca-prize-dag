# Audit - L1 cofactor-depth budget cancellation

## Checked axes

1. The theorem is restricted to `e<k`, so `d=w+e<a`.
2. The possible cofactor count is exactly `q^e`, with leading coefficient
   already fixed.
3. Exactness only deletes from the full locator-prefix fiber.
4. Ambient cancellation uses `d=w+e`, not `d=w`.
5. Image normalization retains the exact factor `q^d/L_(a,d)`.
6. The full-image certificate has the correct inequality direction.
7. Integer ceilings introduce an additive term strictly below `q^e`.
8. A route fence is not reported as a mathematical falsifier.
9. The upstream finite Q statement is not silently generalized in depth.
10. F2 tower transfer is not mislabeled as max-fiber depth transfer.

## Route effect

The growing-cofactor obstruction is no longer described as an unavoidable
formal `q^e` loss.  Before image collapse, a uniform ambient row-sharp Q
theorem would pay it exactly.  At the deployed rows, however, collapse and
integer occupation appear after one or two extra coordinates, so the live
problem is transversality of the split-divisor prefix image against the
received-word Pade graph, equivalently a target-sensitive Toeplitz estimate.
The decorated shift-pair route remains relevant precisely there and for
`e>=k`.
