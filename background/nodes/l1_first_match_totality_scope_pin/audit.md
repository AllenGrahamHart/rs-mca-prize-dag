# Audit - L1 first-match totality scope pin

## Checked axes

1. The theorem assigns distinct image contributors, not raw support witnesses.
2. Every contributor must have a nonempty carrying-chart set.
3. A total order makes the least owner unique.
4. Owner cells are disjoint and exhaustive.
5. Fiber totality and first-match payment are stated as separate obligations.
6. No polynomial chart count or owner-cell budget is inferred.
7. The upstream Lean theorem is used only for the matching total-key scope;
   the multivalued least-owner form is proved directly here.

## Remaining attack

Maximal source-layout composition is retired by
`l1_general_first_layout_domination`. Prove a polynomial bound for the sum of
internal contributor-dependent quotient/Forney rechart owner-cell payments in
the fixed first source, or give a complete finite normal form reducing that
sum to a certified residual computation.
