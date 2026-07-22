# Audit - L1 raw support-ledger exponential route fence

## Checked axes

1. `j` is a power of two, so `ell=n/j`, `M=j/2`, and `ell/2` are integral.
2. The source partition uses `N=k-1`; the `b=1` term is not dropped.
3. The list-threshold inequality is met at equality.
4. The non-planted cap `a_i<=d` holds with wide slack.
5. The root-pinning lower bound uses only its printed numerical right-hand
   side, not existence of a compatible locator.
6. The background-anchor lower bound concerns its assigned allowance, not the
   actual cardinality of an exact cell.
7. Exponential looseness of an upper bound is not called a counterexample to
   L1.
8. The route fence leaves algebraic emptiness and cross-pattern injections
   available.

## Route effect

Raw support enumeration has zero closure value even with unlimited compute.
The next theorem must reduce the feasible support family or inject many
support cells into one common polynomial-size currency before summation.
