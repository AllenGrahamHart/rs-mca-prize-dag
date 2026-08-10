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

---

## WAVE-9 PREDICATE-ROLE ADDENDUM (2026-07-17, pin body)


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

The rate-`1/2` safe side is not supplied by the clean-rate R2 node; it is the
safe half of the rowwise adjacent certificate in `rate_half_band_closure`.
The proved cyclic simple-pole theorem is an unsafe lower bracket and is not an
upper input. Once the rate-half rowwise premise and the clean-rate predicates
hold, every stratum in the safe side is either paid, stripped into a priced
column, or bounded by the compiled aperiodic residual. Summing the first-match
strata gives the displayed `B_C(a_safe) <= B*`.

The evidence edges record stronger or historical routes, but the live
predicate package above is the logical surface consumed by `mca_grand`.

---

## ROUND-28 QUANTIFIER AUDIT (2026-08-10): THE NAMED PREMISE-WEAKENING
## FOLLOW-UP IS RETIRED AS UNSOUND (bodies above preserved)

The wave-10 / round-27 lead — "this node's rate-1/2 bar is dischargeable by
the PROVED half-distance bracket because `a_safe` is textually free at this
level" — is CORRECT ABOUT THE TEXT AND WRONG ABOUT THE LOGIC. The rewire is
not applied, and `rate_half_band_closure` stays in the predicate list.

**(1) `a_safe` is unbound in this node's prose and bound by its consumers.**
No line of this node's statement or proof binds `a_safe`. The symbol is
shared: the unsafe-side node's claim of record is `B_C(a_safe - 1) > B*` —
stated at this node's index minus one — and `mca_grand`'s claim is to
EXHIBIT an `a` with `B_C(a-1) > B* >= B_C(a)`. The assembly's `a` is the
crossing index; `a_safe` is that index, not a free choice.

**(2) The reductio.** If `a_safe` were genuinely free, this node's rate-1/2
instance would be discharged with NO field restriction at all by the PROVED
`mca_full_agreement_endpoint`: (FA1) `B_mca(n) = 1`, hence `B_mca(n) <= B*(q)`
at every admissible `q > 2^128`. That is strictly stronger than the proposed
half-distance route, which needs `q >= 2^169` and reaches only `3n/4`. A
claim discharged by a wave-6 triviality would not need eight premises; the
eight premises are the evidence that `a_safe` is pinned.

**(3) What the half-distance bracket actually supplies.** `B_C(a)` is
nonincreasing in `a` (`crossing_localization`, PROVED), so a safe point at
`3n/4` bounds nothing at any smaller index. The half-distance result is an
upper BRACKET END for the crossing, not the safe half AT the crossing.
Substituting it here would silently re-point this node's claim from the
crossing to `3n/4`, and would turn the unsafe-side claim into
`B_C(3n/4 - 1) > B*` — precisely the open endpoint question (-hi tight vs
-lo tight). The open content would be transferred, not discharged.

**(4) Field-range map of the rate-1/2 safe inputs (for the record).** The
wave-10 staircase determines the crossing at admissible `q < 2^167`; the
residual budgets `{2^39, 2^39+1}` occupy `q` in `[2^167, 2^167 + 2^129)`;
above that only brackets exist — top `n` (FA1, every admissible `q`) and top
`3n/4` (half-distance, `q >= 2^169`). The band `2^167 < q < 2^169` recorded
as "the gap" is a gap in the BRACKET TOP only. There is no safe-half input
at the crossing anywhere above `2^167`, the razor slice included, so the gap
is not the boundary of this node's rate-1/2 exposure.
