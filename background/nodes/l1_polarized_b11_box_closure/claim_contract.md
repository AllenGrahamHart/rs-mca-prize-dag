# Claim contract - L1 polarized B11 box closure

## Inputs

- `l1_polarized_petal_entropy_ledger` for the exact polarized coordinate and
  sparse/full support convention;
- `petal_reserve_rich_fiber_reduction` for `h>=ell` and the non-planted
  per-petal defect cap;
- `pma_b11_first_match_router` for polynomial payment of the automatic gate.

## Output

Every fixed `(p,d-ell)` box is polynomial. The honest residual has only two
unbounded coordinates: polarized support entropy or cofactor excess.

## Consumer Rule

Use `(PB3)` as a necessary condition, not as two separately proved counts.
An attack that assumes both coordinates bounded is attacking a paid class.

## Falsifier

A maximal-chart word in `(PB1)` with both `G_2>2P` and `G_R>P`, or a failure
of the B11 payment under the exact fixed gate parameters.
