# conditional proof: mca_safe

- **status:** CONDITIONAL
- **closure:** proof from predicate nodes

## Predicate nodes

- `counting_frame`
- `fm1`
- `strip`
- `paid_closure`
- `ext_lift`
- `safe_assembly_uniformity`
- `r2_clean_rates`
- `rate_half_band_closure`

Evidence/support:

- `r2_rigidity`
- `mca_from_ca_reduction`
- `deep_safe_all_linear`

## Claim

Conditional on the predicate nodes, the certified safe agreement satisfies

```text
B_C(a_safe) <= B*.
```

## Proof

`counting_frame` supplies the stratified count convention.  `paid_closure`
handles the already-paid tangent/quotient branches, `strip` decomposes the
periodic contribution into quotient columns plus the GAP-1 residual, and
`ext_lift` handles the extension-lift branch.  `fm1` and `r2_clean_rates`
control the aperiodic residual at the clean-rate corridor points in the
compiled `R_post <= 16 n^3` form.  `safe_assembly_uniformity` verifies that
the first-match/dedup convention and constants compose uniformly across the
admissible rows.

The rate-`1/2` safe-side top slice is not supplied by the clean-rate R2 node;
it is included only through the strong `rate_half_band_closure` premise.  Once
that premise and the clean-rate predicates hold, every stratum in the safe
side is either paid, stripped into a priced column, or bounded by the compiled
aperiodic residual.  Summing the first-match strata gives the displayed
`B_C(a_safe) <= B*`.

The evidence edges record stronger or historical routes, but the live
predicate package above is the logical surface consumed by `mca_grand`.
