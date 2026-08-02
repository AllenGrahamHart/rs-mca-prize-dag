# Audit

The computation is deliberately split at each logical boundary.

1. FLINT factors and reconstructs each scale before any roots are exported.
   Irreducible cubic factors are retained in the ledger and excluded only
   from the deployed-base-field root list.
2. Exceptional fibers are recomputed in the original guarded common lex
   ideal.  No denominator-cleared or pseudo-reduced equation is used to
   decide them.
3. The sole proper fiber is not called a point until its quadratic is split
   explicitly.  Both resulting points are substituted into the recorded
   affine basis.
4. All eight kernel coefficients are evaluated independently from the sealed
   compact expressions.  Their nonzero projective vector and
   `b10+b11=0` are checked at both points.
5. The outside calculation uses only necessary `DE+/DE-` equations.  A unit
   ideal excludes a point even though the two-equation system is not claimed
   sufficient for a full packet.
6. Source roots are saturated away from zero, poles, equal squared labels,
   and all five common squared labels.  Omitting target guards only enlarges
   the tested variety, so a unit result remains a valid exclusion.

Mutation controls alter the exceptional root set, common-fiber unit pattern,
quadratic lift, and signed-pair unit verdict; each mutation must fail.
