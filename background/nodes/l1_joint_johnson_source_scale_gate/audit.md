# Audit - L1 joint-Johnson source-scale gate

## Checked axes

1. The variance rewrite uses `c=a+u-ell` exactly.
2. The quarter bounds are applied separately to universe sizes `N` and `b`.
3. Zero background is routed through the core-defect Johnson theorem instead
   of dividing by `b`.
4. The strict remainder `b<ell` supplies `N>=3ell+1` from `N+b>=4ell`.
5. The official source equation uses `N=k-1`, preserving the additive `r`.
6. The gate is strict at `M<3(r-1)`.
7. The arithmetic boundary family `(SG6)` works at all four official rates.
8. Fixed petal polarity is retained in the aggregate claim.
9. No contributor existence is inferred from source arithmetic.

## Remaining attack

On the bounded-polarity branch, only source scales `M>=3(r-1)` and the joint
sub-Johnson region remain. Growing petal polarity remains live at every
scale. A future compute request must enforce the rate-specific scale gate
before generating cells.
