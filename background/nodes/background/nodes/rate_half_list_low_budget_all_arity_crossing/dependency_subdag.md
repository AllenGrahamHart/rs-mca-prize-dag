# Dependency sub-DAG

```text
rate_half_list_low_budget_exact_crossing [PROVED] --+
list_subsqrt_interleaving_collapse [PROVED] --------+-> rate_half_list_low_budget_all_arity_crossing [PROVED]
                                                        +-> list_grand [evidence: B*=1,2 branches]
                                                        +-> list_large_m_scope_closure [evidence]
```

Both incoming edges are requirements. The outgoing edges are evidence because
the grand and transport nodes retain larger-budget row scope.
