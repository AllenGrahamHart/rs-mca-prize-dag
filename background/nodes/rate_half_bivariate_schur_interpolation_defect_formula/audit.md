# Audit

1. The Lagrange weights solve the transposed Vandermonde column problem; the
   factors `c_(1,x)/c_(1,p)` are retained.
2. Formula `(SID3)` excludes the already-eliminated top coefficient
   `j=m+1`.
3. Lower clones have zero top block and are not represented by `(SID3)`.
4. Repeated zero roots in `(SID5)` encode deficiency clones and are a
   multiset, not additional supported slopes.
5. The single-coefficient criterion applies only when `Delta_W=0`.
6. The primary verifier compares direct Schur elimination with the formula
   in saturated and deficient synthetic cases. The independent audit checks
   all ten published `m=1` matrices and recovers their zero residual column.
