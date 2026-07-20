# Dependency sub-DAG

```text
rate_half_list_budget_three_antipodal_pure_quartic_degree_rigidity [PROVED]
  --> rate_half_list_budget_three_antipodal_pure_harmonic_fermat_router [PROVED]
      --> rate_half_list_budget_three_antipodal_harmonic_torsion_characteristic_sieve [PROVED]
          --ev--> rate_half_list_adjacent_crossing [TARGET]
              --req--> list_adjacency_closing [CONDITIONAL]
```

The new node removes characteristic zero and replaces the first official
finite obstruction by an integer characteristic sieve. It does not promote
the red consumer until that sieve is computed and checked.
