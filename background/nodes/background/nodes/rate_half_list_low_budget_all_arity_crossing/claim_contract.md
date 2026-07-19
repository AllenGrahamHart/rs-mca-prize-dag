# Claim contract: low-budget all-arity rate-half list crossing

- **claim:** the exact `B*=1,2` ordinary-list crossing at `3n/4` is the exact
  crossing for every common-support interleaving arity `m>=1`;
- **scope:** every official rate-half multiplicative-coset row with
  `floor(|F|/2^128) in {1,2}`;
- **safe input:** `rate_half_list_low_budget_exact_crossing` and the proved
  sub-square-root interleaving collapse;
- **unsafe input:** diagonal embedding of the explicit ordinary predecessor
  lists;
- **consumer:** the corresponding field branches of the grand list problem;
- **nonclaim:** no branch with `B*>=3` and no MCA/CA object is determined;
- **falsifier:** an interleaved received word with more than `B*` tuples at
  agreement `3n/4`, or failure of the diagonal predecessor witness.

This is a complete list-prize determination on two field-budget branches,
uniformly in arity. It is not a full closure of `list_grand`.
