# conditional: dli_odd_evaluation_discrepancy

## Predicate nodes

- `dli_truncated_log_transfer`
- `dli_peak_mass_discrepancy`

## Claim

Conditional on peak-mass discrepancy for the odd-evaluation sequence, the DLI
odd-evaluation discrepancy predicate holds.

## Proof

The proved transfer predicate is deterministic: once a sequence satisfies the
required truncated-log discrepancy bounds and peak-mass tail bounds near the
Dirichlet singular peaks, it supplies exactly the geometric-mean discrepancy
needed by this node, with total error `sum_j eps_j=o(t)`.

The remaining peak-mass predicate supplies those bounds for the actual
low-degree odd evaluations `P_lambda(sigma(y))` on the square-root section.
Composing the two statements gives the discrepancy control away from
Dirichlet peaks required here.
