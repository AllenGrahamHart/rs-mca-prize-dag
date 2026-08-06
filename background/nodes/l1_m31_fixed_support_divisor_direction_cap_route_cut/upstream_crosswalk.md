# Upstream crosswalk - fixed-support divisor-direction route cut

```yaml
workboard_item: M1/L/T
row: Mersenne-31 list at 2^-100
object: OTHER
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: A six-dimensional common-zero-free polynomial space can contain 67449 projective degree-4980 divisors of one degree-72428 split locator.
architecture: DIRECT ROUTE CUT
atom_or_cell: proposed fixed-support divisor-direction successor
quantifier: existential algebraic counterfixture over every sufficiently large field
projection_and_unit: projective polynomial directions, not codewords or slopes
claimed_bound: universal cap 15413 is false under geometry-only hypotheses
status: COUNTEREXAMPLE / PROVED ROUTE CUT
impact: ROUTE_CUT
falsifier: failure of generator independence, common-zero-freeness, divisibility, or projective distinctness
replay: symbolic proof and two static exact verifier sources
```

The route cut belongs with upstream draft PR `#1124`; it prevents the
projective compression from being misread as an unconditional upper theorem.
Export custody is head commit
`0622a5fe3ea7bc34eca4a070b441b244bf579df1`.

## Addendum 2026-08-03 — apparent tension with maelcar #1148, resolved

External evidence, unmerged: PR #1148 (maelcar), head `7b21de0e...`.
#1148 concludes that a 15-dimensional locator hull has only 16 split members.
This node exhibits the opposite phenomenon: a 6-DIMENSIONAL space containing
67,449 SPLIT divisors. THERE IS NO CONTRADICTION — different regimes: ours is
degree 4,980 at `N = 1,053,557` (rank-seven proper-G terminal); theirs is
degree 479 at 1,023, and they concede fixture-specificity.

But the principle recorded here survives and binds: in our M31 lane,
"low-dimensional implies few split members" is FALSE as a dimension-driven
principle. Consequently #1148's rigidity CANNOT BE LIFTED off its fixture, and
must not be generalised into a dimension-based argument anywhere in this lane.
