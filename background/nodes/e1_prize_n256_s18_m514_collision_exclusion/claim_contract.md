# Claim contract

## Input

`e1_prize_n256_s18_variance_cofactor_windows`, including the six residual
variances for `m=514` and the odd singleton-separation conclusion.

## Output

Cofactor `514` is impossible for a prize-envelope `N=256`, profile `(4,2,0)`
collision.

## Guards

1. The normalized-vector counts are not class-pair or weighted-edge counts.
2. Normalization is used for surjective coverage only; stabilizer sizes are not
   inferred from the 320292000 total.
3. The 257 test is only a necessary divisor sieve. Exact whole norms decide the
   184 surviving vectors.
4. Both exact norm engines use the integral resultant, not floating-point
   conjugate products.
5. The four other prize cofactors and all RowC cofactors remain open.

## Falsifier

A normalized residual vector omitted by either complete census, a mismatch
between the FLINT and PARI resultants, or an exact quotient `Norm/514` in the
prize interval.
