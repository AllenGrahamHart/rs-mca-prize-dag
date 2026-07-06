# petal_growth proof status

- **status:** TARGET
- **closure:** proof from predicate nodes

There is no active conditional proof of this critical target.

The sub-frontier named below was cut by the 2026-07-05 retraction; see
`RETRACTION_MANIFEST.md`.  `petal_fixed_excess` and the mixed-amplification
materials remain evidence and attack structure, but the live DAG keeps
`petal_growth` as the honest open uniform full-petal growth obligation.

## Archived Predicate Route

- `petal_fixed_excess`
- `petal_excess_induction`

Alternate route:

- `petal_mixed_amplification`

## Archived Claim

Conditional on the predicate nodes, full-petal extras at cofactor excess
`d - ell = c` are bounded by `poly(n)` uniformly in `c`.

## Advisory Proof Sketch

`petal_fixed_excess` proves the base statement for every fixed excess: at fixed
`c`, the full-petal extras inject into a bounded-dimensional kernel object, so
their count is polynomial in `n` in the generated-field window.

The remaining issue is uniformity as `c` grows. The predicate
`petal_excess_induction` is exactly the bridge from fixed excess to growing
excess: it supplies the mixed-amplification induction with polynomial
constants controlled uniformly over the corridor range.

Combining the fixed-`c` base with that uniform induction proves the stated
full-petal growth bound and closes the Thm 21/B11 escape route.

The refuted `route_exact_rank` alternative is not used. The separate
`petal_mixed_amplification` node remains an alternate way to prove the same
uniform bridge.

## Stress Evidence 2026-07-06

`experiments/amber_stress/petal_excess_local_scan.py` runs a local
coset-chart residue scan derived from the archived Modal petal-excess script.
It separates three surfaces:

- below-top Lemma-13 applicability;
- ambient kernel growth as `c = d - ell` grows;
- exact realizable squarefree locator counts.

The bounded exact run checked `16` coset-chart configurations and `76` rows.
It found no below-top Lemma-13 violations.  It did find ambient `dim K` growth
in `c`, so the old flat-kernel induction premise should not be revived.  Exact
realizable counts were sharply concentrated at or beyond the top-defect band:
below top, the maximum exact count in this local sweep was `1`; at/top beyond,
the maximum was `5005`.  This supports the current retraction note's shape:
off-band survives the local stress tests, while the top band still needs a
parameterized paid-family classification.
