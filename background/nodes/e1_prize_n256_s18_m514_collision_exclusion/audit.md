# Audit

Date: 2026-07-28.

- primary census: Modal app `ap-F9OHvyBufk7R438gPvcJt1`;
- independent census: Modal app `ap-3WkMulO32Zeoqs4U19PRBS`;
- FLINT norms: Modal app `ap-WpzlLsJtyHMAqRXNX4zt5K`;
- PARI norm audit: Modal app `ap-BGNiOCyf6mVdcovdSsUgS0`.

The primary folded-pair census used 12.406914 aggregate worker-seconds. The
full-convolution audit used 28.285508. Both covered `10009125` support choices,
`320292000` signed vectors, and returned the identical six energy and divisor
count vectors.

The corrected primary packet retains all 184 distinct normalized vectors that
pass the 257 sieve. FLINT and PARI agree entry by entry on all 184 resultants;
there are 46 distinct norms and zero candidate quotient in the prize interval.

The local verifier independently reconstructs both shard partitions, replays
all 184 autocorrelation energies and finite-field roots, and checks every
printed norm quotient and exact endpoint comparison. Every source, launcher,
and result packet is hash-pinned. No floating-point estimate or primality
decision is load-bearing.
