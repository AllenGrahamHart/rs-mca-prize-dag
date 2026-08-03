# Proof

The single-word rank theorem gives
`rank R_u=rank R_v=d`, hence `d<=rank J_d<=2d`.

A linear dependence among the `2d` rows of `J_d` is a pair of row
coefficient vectors `(a,b)` satisfying `(P)` in every column. This is
exactly the displayed Padé-window relation, proving the equivalence.

If `a=0`, then `b` is a row dependence of `R_v`, contrary to its full
rank; similarly for `b=0`. If `b=z a`, relation `(P)` is a row
dependence of `R_{u+zv}`. The tangent gate applies to every projective
pencil member, so the single-word rank theorem again forces `a=0`.
The projective direction at infinity handles the symmetric case.
Therefore a deficient relation is genuinely two-sided and
nonproportional.

Writing the vectors as polynomials `A,B` of degree `<d`, their
nonproportionality says that the rational direction `A/B` is
nonconstant. We do not cancel a common factor: over a finite coefficient
window that operation requires separate boundary bookkeeping. Full rank
versus deficient rank is exhaustive, proving the router.
