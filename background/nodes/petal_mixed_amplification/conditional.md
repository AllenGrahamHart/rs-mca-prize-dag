# petal_mixed_amplification conditional proof

- **status:** CONDITIONAL
- **closure:** proof from predicate nodes

## Predicate nodes

- `pma_aux_list_reduction`
- `pma_johnson_regime`
- `pma_wide_residual`

## Claim

Conditional on the predicate nodes, the mixed-petal sunflower amplification
theorem holds.

## Proof

`pma_aux_list_reduction` proves the structural reduction: after fixing the
defect set and background data, every non-planted mixed-petal extra injects
into a list of degree-`<= d` polynomials agreeing with the auxiliary pieced word
on the shifted petal targets. Thus the amplification problem is an auxiliary
RS list problem one level down.

`pma_johnson_regime` covers the few-petal range: when the agreement parameters
fall inside the Johnson/Guruswami-Sudan inequality, the auxiliary list is
polynomial.

The complementary wide sub-Johnson range is exactly the predicate
`pma_wide_residual`. Its corrected statement strips quotient-pullback and
low-defect families first, then bounds the primitive residual polynomially.

These regimes cover all mixed-petal auxiliary lists. Hence any
super-polynomial amplification is either charged to quotient structure,
low-defect/fixed-excess structure, or excluded in the primitive residual. That
is the mixed-petal amplification theorem.

## Stress Evidence 2026-07-06

`experiments/amber_stress/pma_correlated_target_search.py` attacks the
`pma_wide_residual` premise by varying both the common defect locator and the
petal scalar pattern.  It found the expected structured full-agreement control
when all scalars are constant, but no adversarial nonconstant pattern produced
a large exact primitive-spread residual in the checked `M=6,9` rows.

---

## RE-POSE RECORD (2026-07-16, wave-8 audited; v4 conditional body — why the old implication retired + surviving inputs)


- **status:** TARGET
- **former status:** CONDITIONAL on `pma_wide_residual`

## Why the old implication was retired

The former packet reduced the finite branch to

```text
#Post<=B_post,       B_post<=n^6.
```

That premise is false. The generic defect-four obstruction constructs more
than `n^6` primitive source codewords after every global owner. The Top/Post
partition then forces `#Post>B_post`. Keeping the old packet as an amber
implication would be logically vacuous and would hide the actual proof
obligation from the critical orbit.

## Surviving inputs

The following theorems remain valid and are consumed by the corrected target:

- `pma_aux_list_reduction` and `pma_source_paving_bridge`;
- `pma_johnson_regime` and `pma_b11_first_match_router`;
- `pma_exact_periodic_owner` and `pma_quotient_closure_scope`;
- `pma_sigma_one_dyadic_near_coset_owner`;
- `pma_sigma_one_odd_lift_boundary_owner`;
- the finite `d<=2`, `(3,1)`, and full-petal `(3,0)` payments;
- the diffuse-hyperplane and reciprocal-quadratic route cuts;
- paired-core normalization, abundance, and first-layout domination;
- `pma_sigma_one_d4_generic_source_obstruction` as a mandatory lower floor.
- `pma_sigma_one_variable_defect_exact_hit_floor`, which rules out a uniform
  sigma-one polynomial theorem;
- `petal_reserve_rich_fiber_reduction`, which identifies the distinct
  reserve-scale obstruction.
- `pma_saturated_mixed_support_kernel`, which gives the exact weighted-Hankel
  kernel, maximal rank, coprime-pencil saturation, and canonical fixed-support
  split-locator bound.
- `pma_petal_pattern_root_pinning_ledger`, which sums that bound over petal
  patterns, removes background multiplicity, and closes every bounded petal-
  deficit/root-excess region.
- `pma_full_petal_band_composition`, which pays all `M<=3` sources and the
  `M=4,t=4` full-petal stratum.
- `pma_coset_subtwoell_saturation_exclusion`, which sharply excludes
  `t>=3, ell<d<2ell` on constant-shift locator pencils but does not supply the
  missing below-band source-to-pencil bridge.
- `pma_arbitrary_petal_source_realizability`, which proves that maximal-source
  structure alone cannot supply that bridge, even on a smooth multiplicative
  domain.
- `pma_three_petal_mu_basis_reduction`, which puts every arbitrary-locator
  `t=3, ell<d<2ell` contributor in an exact two-generator syzygy module and
  identifies root excess with its coefficient-degree budget.
- `pma_official_rate_small_source_degree_sieve`, which removes every strict
  `M<=r-2` source scale at rate `1/r` and pays the rate-quarter
  `M=4,t=3` small-background branch.
- `pma_three_petal_projective_johnson_bound`, which pays every rate-quarter
  `M=4,t=3` cell and every positive-denominator rate-half three-petal module.

First-layout domination is still useful: it proves that a single carried
layout contains the whole hard residual up to `M` anchors. What fails is the
chosen `n^6` allowance, not the layout reduction.

## Corrected proof obligation

Under the polynomial-field reserve and lower cutoff, classify every forced
`Omega(n/log^2 n)` source-coupled rational-value fiber into an explicit
natural-scale owner or aggregate the canonical root-pinned locator charges
over exact supports with one fixed polynomial exponent. Then print the literal
consumer comparison showing that the exponent and profile charges imply
`imgfib`.
For the remaining `M=4,t=3` full-petal strip, this means counting the split
monic exact-defect locus in the four fixed mu-basis modules or routing it once
to an existing natural-scale owner, only in the explicit nonpositive-
denominator rate-half top-defect tail.
The aggregate theorem need only treat the residual

```text
(t ell-h)+max(0,2d+1-h) -> infinity.
```

Finite sigma-one ledgers must retain the exact defect-four and variable-defect
floors, but those floors are not part of the reserve-only upper comparison.
