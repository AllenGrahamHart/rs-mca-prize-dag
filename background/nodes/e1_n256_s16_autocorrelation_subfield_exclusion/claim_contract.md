# Claim contract

## Inputs

- `e1_n256_s16_sparse_l1_variance_exclusion`, including the folded profile,
  chord ledger, and exact low-slack recurrence;
- `collision_norm_criterion`, including nonzero characteristic-zero norm and
  the lower row-prime endpoint.

## Output

At variance 76, no collision candidate has every nonzero positive-half
autocorrelation distance divisible by four.

## Guards

1. The divisibility condition concerns support of the autocorrelation
   coefficients `A_d`, not support of `F` itself.
2. The theorem uses `V=76` and its exact `L<=22` ceiling; it is not stated
   uniformly for all lower variances.
3. The subfield element is `F(zeta) conjugate(F(zeta))`, not `F(zeta)`.
4. The full norm may be large; the proof controls its prime divisors through
   `|R|=|N|^2`.
5. Autocorrelation supports containing a distance not divisible by four
   remain open.

## Falsifier

A pair-feasible `V=76` collision whose nonzero autocorrelation distances are
all divisible by four.
