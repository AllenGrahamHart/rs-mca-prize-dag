# paid_quot_fn proof

The quotient paid column is partitioned into zones `(a)`, `(b)`, and `(c)`.

The node `qfloor_exact` supplies the exact floor rule above the norm
threshold, so zones whose quotient representatives lie above that threshold
are point-valued computable counts. The node `acl_count` supplies the
characteristic-zero aligned-class count used for the ACL quotient zone.

In zone `(b)` the value-set collision question is not closed in this DAG.
Accordingly this node proves the interval-valued quotient function, not a
point-valued quotient function:

```text
Paid_quot(A) in [lower_quot(A), upper_quot(A)].
```

The lower endpoint is the certified count supplied by the exact floor and ACL
rules; the upper endpoint is the recorded collision-safe envelope for the
unresolved zone. This is the exact object consumed by `paid_closure` and by
the downstream `zone_b` branch. No point-valued zone-(b) conclusion is claimed
here.
