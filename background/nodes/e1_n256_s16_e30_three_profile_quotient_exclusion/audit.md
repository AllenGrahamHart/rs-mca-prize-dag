# Audit

- Modal app: `ap-6rqImRUb2uMS1GmFe1rVMT`.
- 128 workers cover eight profiles, two quotient orders, and eight shards.
- Aggregate worker time: 106.631015954 seconds at 512 MiB per worker.
- The packet marks all 128 tasks complete and checkpoints every completed row.
- The independent checker recomputes 24,124,690 total allocations, every
  per-profile/order total, and every maximizing objective.
- The three claimed profiles account for 1,939,590 allocations and are below
  the cutoff in both quotient orders.
- Hostile checks reject an omitted shard, a changed capacity, a malformed
  maximizing allocation, a cutoff of 1057, or omission of the `4Z` chamber.

The earlier failed launcher app `ap-Y3PyxbL9jWc8vSqM0zXKQe` performed zero
mathematical tasks and emitted an explicit incomplete checkpoint; it is not a
source of evidence.
