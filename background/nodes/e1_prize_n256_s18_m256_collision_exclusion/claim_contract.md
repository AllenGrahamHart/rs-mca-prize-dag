# Claim contract

## Input

`e1_prize_n256_s18_variance_cofactor_windows`, including the nine residual
variances for `m=256` and the singleton-separation order.

## Output

Cofactor `256` is impossible for a prize-envelope `N=256`, profile `(4,2,0)`
collision.

## Guards

1. Normalized-vector counts are not class-pair or weighted-edge counts.
2. The exact norm ledger covers every retained vector; it is not a sample.
3. SHA-256 commitments are integrity devices. The mathematical values are
   independently produced by FLINT and PARI before commitment comparison.
4. No floating-point conjugate product or primality test is load-bearing.
5. The cofactors `2,4,16`, later profiles, and all RowC cofactors remain open.

## Falsifier

A normalized residual vector omitted by either census, a FLINT/PARI shard
commitment mismatch, or an exact quotient `Norm/256` in the prize interval.
