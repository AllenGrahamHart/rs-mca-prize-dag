# Dependency sub-DAG

```text
v13_2_near_rational_supportwise_two_anchor_payment [PROVED]
  --> rate_half_mca_two_anchor_reserve_repricing [PROVED]

deployed_identity_prefix_owner_scope_audit [PROVED]
  --> rate_half_mca_two_anchor_reserve_repricing [PROVED]
        --ev--> mca_safe [CONDITIONAL]
```

The first supplier owns the `2w` theorem.  The second owns the exact
full-owner average ceilings used only for the viability comparison.  This
node has an evidence edge, never a requirement edge, into the safe-row claim:
it proves a corrected conditional interface, not its open large-owner
premise.
