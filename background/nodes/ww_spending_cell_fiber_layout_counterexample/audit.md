# Audit - unsafe spending-cell fiber-layout counterexample

The scope counterexample was derived from the exact spending-cell formulas,
not found by a broad search. The crucial checks are:

1. the Proth witness proves the printed field order is prime;
2. `N*=8` is the first quotient scale above `B*=6`;
3. the cell has exactly six petals and one background point;
4. all selected fibers, the missed-core fiber, and the zero fiber are
   disjoint;
5. the six labels are distinct and nonzero;
6. the factored witness has degree `<k` and enough agreements; and
7. it is not any printed plant.

`verify.py` checks these facts without expanding a degree-2047 polynomial or
enumerating the field. It also checks the repaired DAG wiring and proves by
required-edge reachability that W3 cannot reach the prize. `verify_audit.py`
changes the field, defect, fiber classes, rate data, statuses, and edge kinds;
every mutation must invalidate at least one required check.

The cell is intentionally the unsafe spending cell. That is why the
counterexample threatens neither the prize statement nor literal safe-side
W3. It refutes the stronger auxiliary assertion that every planted receiver
at the lower endpoint is individually safe, and thereby validates removing
W3 from that consumer route.
