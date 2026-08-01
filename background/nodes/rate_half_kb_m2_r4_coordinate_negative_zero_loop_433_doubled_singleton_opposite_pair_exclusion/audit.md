# Audit

1. Raw q determinants are divided only by even label/denominator factors;
   no `r` or `t` division is allowed before the affine solve.
2. Cramer ratios preserve relative constants.
3. The common square factor is exactly `X_den(y^2-1)`.
4. Every projected base-field root is replayed in the original equations.
5. All three lost branches are checked in every root-sign row.
6. Four verifier processes keep each replay below the 60-second cap.
