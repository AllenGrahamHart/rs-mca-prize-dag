# Audit

- Two complete census engines agree on all `320292000` normalized vectors,
  every variance count, and every `(E,L)` cell.
- Candidate generation is repeated independently inside each norm worker;
  neither exact engine reads a stored witness list.
- FLINT and PARI compute all `540332` residual resultants and independently
  check the exact 2-adic valuation four.
- All 64 multiset-fingerprint buckets agree on count, xor, sum, and square-sum.
- Both engines report zero prize-interval quotients and the same numeric
  maximum-below and minimum-above values. Two symmetry-related vectors attain
  the minimum-above value, so the retained representative need not match.
- Primary Modal app: `ap-6Mx4ggc8xnWQiKXHn8Nin3`.
- PARI audit app: `ap-iL2Um5gs93niNlF87WvgLp`.
- Aggregate exact-norm worker time was about 138 FLINT CPU-seconds and 876
  PARI CPU-seconds; each container stayed at 512 MB or less.
