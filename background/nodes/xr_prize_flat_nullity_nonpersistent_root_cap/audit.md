# Audit

- The proof bounds the real envelope before flooring, so no favorable
  rounding is hidden.
- Convexity uses `R-h-k+1>0`, checked on every prize row; it is not asserted
  for arbitrary rates.
- Both `u` endpoints are retained. Which endpoint determines the ceiling
  changes between the three rows.
- The printed survivor ceiling is `V-1`, while `V` itself is paid.
- The effective-core diagonal and the nonpersistent-root ceiling are
  necessary conditions only; their intersection is not asserted nonempty.
- No Modal or large local computation is used.
