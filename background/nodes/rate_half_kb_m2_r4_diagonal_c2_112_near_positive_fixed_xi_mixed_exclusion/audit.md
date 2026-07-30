# Audit

1. The primary verifies the direct reconstruction determinant and both forced
   residual roots before forming the mixed conditions.
2. Every removed bivariate factor is matched to an explicit collision,
   inversion-fixed label, `z=1` component, or finite-chart boundary.
3. Resultants are used only as necessary conditions; no generic leading
   coefficient is divided out.
4. The primary projects in `c` to a polynomial in `d`. The independent audit
   uses a fraction-free source solve and projects in `d` to a polynomial in
   `c`.
5. Both implementations recompute the final gcd over the deployed
   characteristic rather than inferring it from characteristic zero.
6. Each complete verifier runs under `timeout 60s` and `ramguard tiny`.
