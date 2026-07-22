# W3 paid/residual first-match partition adapter

- **status:** PROVED
- **dependency:** `stratification_partition_thm`
- **consumer:** `ww_row_envelope_clause` (evidence only)

Fix an admissible row and received word `U`. Let `X(U)` be its finite set of
list words at the binding agreement threshold, and let
`P_0,...,P_m` be any ordered paid predicates. Define

```text
G_0 = P_0,
G_i = P_i and not(P_0 or ... or P_(i-1)),
R   = not(P_0 or ... or P_m).
```

Then `G_0,...,G_m,R` are a disjoint partition of `X(U)`. If
`|G_i|<=u_i(U)` and the residual is partitioned into cells with
`N_chal^o(U,c)<=b_c(U)`, then

```text
|X(U)| <= sum_i u_i(U) + sum_c b_c(U).
```

In particular, with

```text
B_chal(U) = B* - sum_i u_i(U) >= 0,
```

the W3 residual condition `sum_c b_c(U)<=B_chal(U)` implies
`|X(U)|<=B*`.

This closes the abstract coverage, disjointness, and budget-composition
bookkeeping. It does not define the paid predicates, prove the paid upper
allocations `u_i`, construct the residual cells, or prove their bounds.
