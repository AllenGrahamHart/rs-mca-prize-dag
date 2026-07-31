# Audit

1. The new target root is `tau(xi)=2`; the source reconstruction is unchanged.
2. The primary verifies the exact source determinant and both forced roots.
3. Every removed factor is explicitly classified; no generic leading branch
   is divided out.
4. Primary and audit use direct and fraction-free source solves and project
   in opposite variables.
5. Both final support gcds are recomputed modulo the deployed characteristic.
6. Each verifier runs under `timeout 60s` and `ramguard tiny`.
