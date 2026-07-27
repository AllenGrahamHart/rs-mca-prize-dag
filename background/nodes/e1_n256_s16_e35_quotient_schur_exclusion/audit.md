# Audit

- Recomputed the E=35 L1 ceiling from the exact slack table.
- Re-enumerated all 21 integer magnitude profiles.
- Recounted all 2,946,287 quotient allocations independently.
- Re-evaluated every displayed shard, objective, and chamber maximum.
- Enumerated all 104,750 odd order-128 outer allocations and all 32,346
  divided outer allocations independently.
- Recovered exactly four outer allocations above 458 and replayed all 276
  compatible middle/top allocations, with maximum 2054.
- Kept the low-outer, exceptional-outer, divided-support, and full-`4Z` cases
  separate.
- Replayed the exact rational margins at 2162 and 2163.
- Injected incomplete-packet, missing-shard, and altered-maximum mutations;
  all were rejected.
- No incomplete solver status or floating-point comparison supports the
  claim.

The complete Modal run was `ap-Gwlrl9cLfJsa2bS83BFw4k`. Setup-only runs
`ap-0FGvj92aNnIyFpLCOoTJKC` and `ap-9dJHjobg5LNfcSK5vU3HWf` failed before any
census result because of launcher path hydration and are not evidence.
