# conditional: generator_economy (Pro Brief F, target A — construction verified)
## Predicate node
- `generator_size_budget_check`
## Claim
An explicit poly(N)-base-certified family of half-size l'-subsets exists
(antipodal zero-sum padding); it certifies generator_economy provided its size
meets the cluster budget.
## Proof
Construction verified (notes/pro_construction.md): |F| = N C(N/2-2, N/4-1),
differences in the semigroup of <= N+1 cyclotomic bases, admissibility guard
respected. Remaining: the size |F| >= B*/2^33 at the prize rows (the budget
match) — the predicate generator_size_budget_check.

## Addendum (2026-08-07, forced): the stated obligation is UNSOUND as written

"Remaining: the size |F| >= B*/2^33 at the prize rows" assumed the
Pro-Brief-F family's banked size; by the collision catch (statement
addendum, item 1) that predicate is unsatisfiable for the banked
family and the route decides zero prize rows. The obligation of
record is the GE-WEAK (b)-form (statement addendum, item 4).
