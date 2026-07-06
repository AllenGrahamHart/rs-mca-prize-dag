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
