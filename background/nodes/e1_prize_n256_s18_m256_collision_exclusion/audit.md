# Audit

Date: 2026-07-28.

- primary census: Modal app `ap-GLhkTmrhb9jYJYJwyLWxYJ`;
- independent census: Modal app `ap-geY02XirYKUn755jIDegx3`;
- FLINT norm ledger: Modal app `ap-qOUwcG4vpXLacPHsbUgmcn`;
- PARI norm audit: Modal app `ap-ORclHKC4a7qVqguTzELasP`.

The census engines use distinct autocorrelation and partition implementations.
They agree exactly after 10.184942 and 29.095441 aggregate worker-seconds,
respectively. The FLINT ledger evaluates all 20756 residual resultants in
3.662948 aggregate worker-seconds; the PARI replay matches all 32 commitments
in 26.593269 worker-seconds.

The norm result packet deliberately retains commitments, interval counts, and
extremal witnesses rather than 20756 redundant large integers. The local
verifier replays every retained vector's energy, both coverage partitions, all
count sums, the exact interval gap, and one-to-one FLINT/PARI commitment
agreement. Every source, launcher, and result is hash-pinned.
