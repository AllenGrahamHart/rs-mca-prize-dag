# Dependency sub-DAG

The theorem is proved directly and has no open requirements.

```text
identity_prefix_flexible_budget_unsafe_floor [PROVED]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
    --ev--> deployed_identity_prefix_owner_scope_audit [PROVED]

deployed_identity_prefix_owner_scope_audit [PROVED]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

The evidence edges are deliberate: the universal target still needs exact
row arithmetic at every proposed predecessor.
