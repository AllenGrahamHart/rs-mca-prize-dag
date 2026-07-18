# Dependency sub-DAG

```text
rate_half_cyclic_rotated_prefix_floor [PROVED, unsafe evidence] --+
rate_half_list_integer_johnson_safe_anchor [PROVED, safe evidence]+--> rate_half_list_adjacent_crossing [TARGET]
rate_half_list_low_budget_exact_crossing [PROVED, B*=1,2] -------+
list_crossing_localization [PROVED, monotonicity] ----------------+
matching adjacent upper/lower pair [OPEN CONTENT] ----------------+

rate_half_list_adjacent_crossing [TARGET]
  -> list_adjacency_closing [CONDITIONAL]
  -> list_large_m_scope_closure [CONDITIONAL, transitively]
  -> list_grand [CONDITIONAL]
```

The new leaf is not a decomposition into speculative propositions. It names an
already-admitted missing premise in the existing conditional packet.

The cyclic prefix floor is also a direct proved requirement of
`list_adjacency_closing`, keeping the lower-bracket provenance on the critical
path. Its edge into this red leaf is evidence because critical TARGETs must
remain logical leaves. The Johnson anchor is likewise evidence: it proves a
safe endpoint but not predecessor unsafety in the remaining `B*>=3` branches.
The low-budget theorem is evidence because it closes only `B*=1,2`.
