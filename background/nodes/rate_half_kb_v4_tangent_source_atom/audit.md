# Audit

## Independent replay

The upstream PR `#1049` artifact was extracted at exact head
`c15927c90091602035f617226da9ecf03cfc7316` into a fresh temporary directory.
Its structural checker passed with

```text
partition_sha256=4fade91abc408264989babcff6f8f9bbd80bcec52545a5db15ac376bf17d88fc
U_paid=981104
remaining_budget=274980728110413983
```

The local proof does not trust that checker for semantics. It derives the
translation from the already PROVED local exact-sparsification node and the
tangent cap from the elementary cardinality of a coordinate image. The local
verifier reconstructs the upstream partition digest, checks the deployed row
arithmetic, tests the set-difference chronology, and audits the DAG edges.

## Scope audit

The number `981104` is an upper budget for the first cell, not its exact
cardinality on each received line. Equality is used only in the chosen ledger
charge. The exact set identity concerns actual cell cardinalities; replacing
the first one by its upper bound yields an inequality.

The reserve is therefore conditional on separately proving valid uniform caps
for `U_Q`, `U_BC`, and `U_new`. No legacy owner total is combined with the new
chronology.
