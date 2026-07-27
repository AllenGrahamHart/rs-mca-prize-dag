# dependency sub-DAG: e1_official_prime_exception_control

Edges are directed from dependency to consumer.

```text
official_row_primes_pinning [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_clean_anchor_exact_collision_allowance [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_pair_feasible_ambient_generation [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_pair_feasible_ambient_generation [PROVED]
    --requirement--> e1_pair_feasible_prime_field_reduction [PROVED]

e1_pair_feasible_prime_field_reduction [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_prime_field_l2_norm_collision_radius [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_official_prime_exception_control [TARGET]
    -> e1_fullness [CONDITIONAL]
```

The exact compiler fixes the finite allowance but supplies no collision bound.
The two field reductions prove that the live branch is ambient-generating and
prime-field. The folded L2 norm theorem removes swap distances through four at
`N=256` and distance one at `N=512`, without paying the surviving ledger.
The official quantifier pin and named-exhibit certificate subgraph remain in
`background/nodes/` and have `ev`, not `req`, edges into this target. The
unresolved target is a logical leaf, with its route-uniform scope printed
directly.
The evidence nodes do not belong to the mathematical critical orbit without a
theorem transporting their content into a closed route-wide result.
