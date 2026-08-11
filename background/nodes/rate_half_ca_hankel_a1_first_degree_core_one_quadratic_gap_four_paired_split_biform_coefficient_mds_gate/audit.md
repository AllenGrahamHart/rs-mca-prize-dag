# Audit

1. `X` contains only rows already proved to have exact parameter degree;
   the possible extremal exceptional row and strict both-endpoint rows are
   omitted rather than assigned invented root sets.
2. The row scalar is nonzero because the specialized row has exact degree
   `m`; it is the value of the leading coefficient polynomial `g_m`.
3. The RS dimension is `n+1`, so the dual exponent ends at `R-n-2`.
   Replacing it by `R-n-1` would add one false parity check.
4. Formula `(CMG5)` uses a shared denominator `g_m`, not independently
   chosen rational interpolants for each elementary-symmetric profile.
5. A nonzero kernel is insufficient: the geometric biform requires every
   row scalar to be nonzero. The gate therefore records full support.
6. Matrix dimensions count all coefficient blocks even when some rows are
   linearly dependent; no rank claim is inferred from the raw row count.
7. The `e=7` rank probe is exact for each printed finite instance, but its
   500 switched designs are evidence rather than an all-design theorem.
