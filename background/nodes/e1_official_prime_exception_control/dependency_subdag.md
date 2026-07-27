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

e1_n256_s16_high_variance_collision_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_proper_conductor_collision_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n256_2adic_cofactor_collision_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n512_four_singleton_collision_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_n512_trinomial_interval_norm_exclusion [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_official_prime_exception_control [TARGET]
    -> e1_fullness [CONDITIONAL]
```

The exact compiler fixes the finite allowance but supplies no collision bound.
The two field reductions prove that the live branch is ambient-generating and
prime-field. Exact folded-norm arguments remove swap distances through four at
`N=256` and through two at `N=512`. The square-mass-16 logarithmic refinement
also reduces one `N=256,s=5` profile to positive even variance at most 134,
while the proper-conductor theorem removes all proper-subfield lifts from both
first-band profiles. The 2-adic cofactor theorem supplies independent
singleton-exponent screens in both profiles. Full-conductor vectors passing
those screens remain, so the surviving ledger is not paid.
The official quantifier pin and named-exhibit certificate subgraph remain in
`background/nodes/` and have `ev`, not `req`, edges into this target. The
unresolved target is a logical leaf, with its route-uniform scope printed
directly.
The evidence nodes do not belong to the mathematical critical orbit without a
theorem transporting their content into a closed route-wide result.
