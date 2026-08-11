# Provenance

The mathematical input is
`haboeck_quadratic_johnson_mca_import`, sourced to IACR ePrint 2025/2110.
The official-row parameters and crossing convention come from
`critical/nodes/rate_half_band_crossing_location` in this DAG.

All numerical values are regenerated from `(RHJ1)--(RHJ2)` by exact Python
integer arithmetic. No field enumeration, numerical square root, or Modal
computation is used.

The supplier theorem and its upstream proof audit were checked for a retained
support parameter. Its stated estimate is constant after the threshold is
met, so `(RHJ7)--(RHJ8)` are optimizer consequences of the imported theorem,
not an additional literature claim.
