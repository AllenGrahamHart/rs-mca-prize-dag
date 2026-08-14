# Audit

1. Exactly the eighteen dense slopes are removed before division by `q`.
2. The ten nonzero deviation-basis anchors remain, so scalar normalization
   preserves the full ten-dimensional span.
3. The normalized equation has degree 18, not 31: the quotient interpolant
   is absorbed into the varying normalized vector.
4. The isolated-point bound remains valid in the presence of excess
   components by generic perturbation and local intersection multiplicity.
5. Incidences, not tuples or records, are counted; each record contributes
   exactly `C(m',11)`.
6. The endpoint at `K'=10` follows factor by factor and is rounded upward.
7. The exact near charge and all eighteen removed records are deducted in
   `N_min`.
8. A rank-deficient point is automatically nonisolated in its kernel fiber;
   this does not make the fiber slope-dominating.
9. The final half-density dichotomy makes no disjointness or aggregation
   inference.

Only constant-size exact integer arithmetic is used; no Modal run is needed.
