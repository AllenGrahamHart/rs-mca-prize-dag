# conditional: petal_excess_induction

## Predicate nodes

- `petal_residue_line_uniformity`
- `petal_mixed_amplification_step`

## Claim

Conditional on residue-line uniformity and the uniform mixed-amplification
step, the fixed-excess petal bound extends to growing excess with polynomial
constants uniform in the corridor range.

## Proof

The existing proved input `l1_coset_chart_residue_bridge` supplies the
coordinate system in which full-petal extras are measured by residue-line
kernel data.

The predicate `petal_residue_line_uniformity` says that the relevant kernel
dimension and realizable extra count do not grow with the excess parameter
`c = d - ell` in the corridor range. Thus the local residue-line obstruction
has a uniform polynomial budget.

The predicate `petal_mixed_amplification_step` supplies the induction step:
assuming the full-petal bound at excess `c`, the excess `c+1` layer is bounded
with no blow-up in the polynomial constant.

Starting from the fixed-excess base supplied to the consumer by
`petal_fixed_excess`, these two predicates give a uniform growing-excess
induction. That is the content required by `petal_excess_induction`.
