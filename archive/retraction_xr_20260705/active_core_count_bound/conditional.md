# active_core_count_bound conditional proof

## Predicate nodes

- `h4_sparse_norm_gate`

## Claim

The fully stripped active-core count is at most `n^3` at the official rows.

## Proof

The proved W4 direct-column rewiring shows that an `n^3` bound on the
fully-stripped split-pair/active-core residue is sufficient for the compiler:
the residue is consumed as one direct compiler column with the verified row
budget.

The proved x83 uniform obstruction gate classifies every finite-row minimal
h-trade in the live windows. After the full strip, a trade is either in a paid
full-fiber class or it is a p-specific norm-gate event: the official row prime
divides the corresponding cleared cyclotomic obstruction norm. Paid full-fiber
events contribute nothing to the fully stripped residue.

The predicate `h4_sparse_norm_gate`, read in its x83-generalized form, excludes
the remaining norm-gate events at the official rows by the row GCD/certificate
tests. Therefore the fully stripped active-core residue is zero in the live
windows, hence certainly at most `n^3`.

The h=3 cubic cap remains a proved base check outside the live campaign trade
range; it is compatible with the same `n^3` compiler budget.
