# Audit - L1 tangent double-root descent

## Checked axes

1. `P_D` is the polynomial remainder modulo `D^2`, not just value data.
2. The affine parameterization is used only when `2r<=k`.
3. The boundary `2r=k` has the singleton zero reduced code.
4. The rigid range allows zero or one solution, not automatic existence.
5. Agreements at roots of `D` are removed exactly once.
6. Agreements outside `D` are transported using nonvanishing of `D(x)`.
7. The original complement gcd guard is retained.
8. Exact gcd `D` is equivalent to reduced primitivity, not merely reduced
   tangent-freeness on the agreement locator.
9. Cofactor degree falls by `r` and surplus grows by `r`.
10. The punctured domain is not claimed smooth.

## Route effect

Tangency is no longer a recursive singularity: after exact-gcd ownership it
becomes one primitive punctured-domain shell.  The remaining difficulty is
global across owners and domain geometry.
