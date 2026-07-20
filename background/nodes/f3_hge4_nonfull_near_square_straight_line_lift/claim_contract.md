# Claim contract

## Proved

- Intermediate coefficients of `S` distinguish non-full from paid full-fiber
  near-square divisors in characteristic zero.
- One selector scheme, or an `h-1` chart cover, captures every non-full-fiber
  finite-field near-square divisor.
- The divisor condition has the exact cubic repeated-squaring presentations
  and sizes in `(NFS7)--(NFS9)`.
- Every fixed selector/chart ideal has a nonzero integer
  bad-characteristic certificate endpoint.

## Consumer

`f3_hge4_norm_gate_count`, before the additional primitive and strip
deletions.

## Falsifier

A non-full near-square divisor omitted by the selector/chart cover, a
characteristic-zero non-full dyadic trade, or a mismatch between the divisor
and repeated-squaring schemes falsifies the theorem.

## Nonclaims

- No integer certificate is computed or factored.
- Selector fibers are not counted as trades.
- No uniform all-row/all-width bound or transfer is proved.
- Sparse cubic systems are not asserted to be computationally cheap.
