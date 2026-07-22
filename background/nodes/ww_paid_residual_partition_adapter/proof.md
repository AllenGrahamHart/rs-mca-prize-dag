# Proof

Apply the general first-match-with-catch-all lemma proved in
`stratification_partition_thm` to the universe `X(U)` and the predicates
`P_0,...,P_m`. Every word with at least one matching predicate enters the
least-index matching guard, and a word with none enters `R`. A later guard
contains the negation of every earlier predicate, so two guards cannot hold at
once. This proves totality and pairwise disjointness.

Now partition `R` into residual cells `R_c`. Finiteness and disjointness give

```text
|X(U)| = sum_i |G_i| + sum_c |R_c|.
```

By the assumed upper allocations, the right side is at most
`sum_i u_i(U)+sum_c b_c(U)`. Substituting
`B_chal(U)=B*-sum_i u_i(U)` proves the final implication.

No structural assertion about a paid predicate is used. That is deliberate:
the catch-all preserves every unpaid word, so an omitted or too-narrow paid
predicate enlarges the residual rather than silently dropping mass. An
overbroad predicate remains invalid unless its claimed upper allocation is
proved for the corresponding first-match guard.
