# Conditional packet

The implication is

```text
f3_h3_direct_floor_conditional_close
and f3_hge4_aggregate_budget
imply R_min<16n^3.
```

The exact partition and payments are

```text
R_min = R_1^min + R_2^min + R_3^min + sum_(h=4)^H_max R_h^min,
R_1^min = 0,
R_2^min < n^3,
R_3^min < n^3,
sum_(h=4)^H_max R_h^min <= 14n^3.
```

The open transitive leaves remain the h=3 C36 successor chain and
`f3_hge4_norm_gate_count`.  Closing them proves this minimal-record budget;
it does not close primitive exact-list coverage.
